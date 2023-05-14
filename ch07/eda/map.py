# -*- coding:utf-8

import pandas as pd
import streamlit as st
import geopandas as gpd
import io
import json

import matplotlib.pyplot as plt
import plotly.express as px


def mapMatplotlib(merge_df):
    fig, ax = plt.subplots(ncols=2, sharey=True, figsize=(15, 10))
    merge_df[merge_df['month'] == 3].plot(ax=ax[0], column="mean", cmap="Pastel1", legend=False, alpha=0.9,
                                          edgecolor='gray')
    merge_df[merge_df['month'] == 4].plot(ax=ax[1], column="mean", cmap="Pastel1", legend=False, alpha=0.9,
                                          edgecolor='gray')

    patch_col = ax[0].collections[0]
    cb = fig.colorbar(patch_col, ax=ax, shrink=0.5)
    for i, row in merge_df[merge_df['month'] == 3].iterrows():
        ax[0].annotate(row['SIG_KOR_NM'], xy=(row['lon'], row['lat']), xytext=(-7, 2),
                       textcoords="offset points", fontsize=8, color='black')

    for i, row in merge_df[merge_df['month'] == 4].iterrows():
        ax[1].annotate(row['SIG_KOR_NM'], xy=(row['lon'], row['lat']), xytext=(-7, 2),
                       textcoords="offset points", fontsize=8, color='black')

    ax[0].set_title('2023-3월 아파트 평균(만원)')
    ax[1].set_title('2023-4월 아파트 평균(만원)')
    ax[0].set_axis_off()
    ax[1].set_axis_off()

    st.pyplot(fig)


def mapPlotly(merge_df):
    with open('eda/data/seoul.geojson', encoding='UTF-8') as f:
        data = json.load(f)

    month = st.sidebar.radio("월", [3, 4])
    result = merge_df[merge_df['month'] == month]
    mapbox_style = st.sidebar.selectbox('지도스타일', ["white-bg", "open-street-map", "carto-positron", "carto-darkmatter",
                                                  "stamen-terrain", "stamen-toner", "stamen-watercolor"])
    st.sidebar.caption("Site : https://plotly.com/python/mapbox-layers/#mapbox-basemap-style-references")
    fig = px.choropleth_mapbox(result,
                               geojson=data,
                               locations='SIG_KOR_NM', color='mean',
                               color_continuous_scale="Viridis",
                               featureidkey='properties.SIG_KOR_NM',
                               mapbox_style=mapbox_style,
                               zoom=9.5,
                               center={"lat": 37.563383, "lon": 126.996039},
                               opacity=0.5
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_traces(hovertemplate='<b>%{location}</b><br>아파트 평균 가격: %{z:,.0f}(만원)')
    fig.update_coloraxes(colorbar_tickformat='000')
    st.plotly_chart(fig)


def showMap(total_df):
    st.markdown("### 병합 데이터 확인 \n"
                "- 컬럼명 확인")
    seoul_gpd = gpd.read_file("eda/data/seoul_sig.geojson")
    seoul_gpd = seoul_gpd.set_crs(epsg='5178', allow_override=True)
    seoul_gpd['center_point'] = seoul_gpd['geometry'].geometry.centroid
    seoul_gpd['geometry'] = seoul_gpd['geometry'].to_crs(epsg=4326)
    seoul_gpd['center_point'] = seoul_gpd['center_point'].to_crs(epsg=4326)
    seoul_gpd['lon'] = seoul_gpd['center_point'].map(lambda x: x.xy[0][0])
    seoul_gpd['lat'] = seoul_gpd['center_point'].map(lambda x: x.xy[1][0])
    seoul_gpd = seoul_gpd.rename(columns={"SIG_CD": "SGG_CD"})

    total_df['month'] = total_df['DEAL_YMD'].dt.month
    total_df = total_df[(total_df['HOUSE_TYPE'] == '아파트') & (total_df['month'].isin([3, 4]))]
    total_df = total_df[['DEAL_YMD', 'month', 'SGG_CD', 'SGG_NM', 'OBJ_AMT', 'HOUSE_TYPE']].reset_index(drop=True)

    summary_df = total_df.groupby(['SGG_CD', 'month'])['OBJ_AMT'].agg(['mean', 'std', 'size']).reset_index()
    summary_df['SGG_CD'] = summary_df['SGG_CD'].astype(str)
    merge_df = seoul_gpd.merge(summary_df, on='SGG_CD')

    buffer = io.StringIO()
    merge_df.info(buf=buffer)
    df_info = buffer.getvalue()
    st.text(df_info)
    st.markdown("- 일부 데이터만 확인")
    st.write(merge_df[['SIG_KOR_NM', 'geometry', 'mean']].head(3))
    st.markdown("<hr>", unsafe_allow_html=True)
    selected_lib = st.sidebar.radio("라이브러리 종류", ["Matplotlib", "Plotly"])
    if selected_lib == "Matplotlib":
        st.markdown("### Matplotlib Style")
        mapMatplotlib(merge_df)
    elif selected_lib == "Plotly":
        st.markdown("### Plotly Style")
        mapPlotly(merge_df)
    else:
        pass
