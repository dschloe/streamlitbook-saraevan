# -*- coding:utf-8

import pandas as pd
import streamlit as st
import geopandas as gpd
import io

def showMap(total_df):

    st.markdown("### 병합 데이터 확인")
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
    st.write(merge_df[['SIG_KOR_NM', 'geometry', 'mean']].head())



