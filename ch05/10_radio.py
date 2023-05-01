# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

# 데이터 불러오기
iris = sns.load_dataset('iris')

def plot_matplotlib():
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(iris['sepal_length'], iris['sepal_width'])
    st.pyplot(fig)

def plot_seaborn():
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(iris, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig)

def plot_plotly():
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = iris['sepal_length'],
                   y = iris['sepal_width'],
                   mode='markers')
    )
    st.plotly_chart(fig)

def main():
    st.title("Choose a plotting library")
    plot_type = st.radio(
        "어떤 스타일의 산점도를 보고 싶은가요?",
        ("Matplotlib", "Seaborn", "Plotly"))

    if plot_type == "Matplotlib":
        plot_matplotlib()
    elif plot_type == "Seaborn":
        plot_seaborn()
    elif plot_type == "Plotly":
        plot_plotly()

if __name__ == '__main__':
    main()
