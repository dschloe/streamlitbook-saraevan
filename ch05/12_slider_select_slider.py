# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error
import plotly.graph_objects as go
@st.cache_data
def load_data():
    # 데이터 불러오기
    tips = sns.load_dataset('tips')

    return tips

@st.cache_resource
def run_model(data, max_depth, min_samples_leaf):
    # 특성과 타겟 분리
    y = data['tip']
    X = data[['total_bill', 'size']]

    # 훈련, 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    st.write('선택된 max_depth:', max_depth, '& min_samples_leat:', min_samples_leaf)

    random_search = {'max_depth': [i for i in range(max_depth[0], max_depth[1])],
                     'min_samples_leaf': [min_samples_leaf]}

    clf = RandomForestRegressor()
    model = RandomizedSearchCV(estimator = clf, param_distributions = random_search, n_iter = 10,
                                   cv = 4, verbose= 1, random_state= 101, n_jobs = -1)
    return model.fit(X_train,y_train), X_test, y_test

def prediction(model, X_test, y_test):
    # 예측
    y_test_pred = model.predict(X_test)

    # 성능 평가
    test_mae = mean_absolute_error(y_test, y_test_pred)
    r2 = r2_score(y_test, y_test_pred)

    return y_test_pred, test_mae, r2

def prediction_plot(X_test, y_test, y_test_pred, test_mae, r2):
    # 그래프 그리기
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=X_test['total_bill'], y=y_test, mode='markers', name='test', marker=dict(color='red'))
    )
    fig.add_trace(
        go.Scatter(x=X_test['total_bill'], y=y_test_pred, mode='markers', name='prediction', marker=dict(color='green'))
    )

    fig.update_layout(
        title='Tip Prediction with RandomForestRegressor',
        xaxis_title='Total Bill',
        yaxis_title='Total',
        annotations=[go.layout.Annotation(x=40, y=1.5,
                                            text=f'Test MAE: {test_mae:.3f}<br>R2 Score: {r2:.3f}',
                                            showarrow=False)]
    )

    st.plotly_chart(fig)

def main():
    # Hyperparameters
    max_depth = st.select_slider("Select max depth", options=[i for i in range(2, 30)], value=(5, 10))
    min_samples_leaf = st.slider("Minimum samples leaf", min_value=2, max_value=20)

    tips = load_data()
    model, X_test, y_test = run_model(tips, max_depth, min_samples_leaf)
    y_test_pred, test_mae, r2 = prediction(model, X_test, y_test)
    prediction_plot(X_test, y_test, y_test_pred, test_mae, r2)

if __name__ == "__main__":
    main()
