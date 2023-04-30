# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df

def main():
    st.title("Data Display st.dataframe()")
    st.checkbox("Use container width", value=False, key = 'use_container_width')

    iris = load_data()
    st.dataframe(iris, use_container_width=st.session_state.use_container_width)

    # pandas style
    st.dataframe(iris.iloc[:5, 0:3].style.highlight_max(axis=1))

if __name__ == "__main__":
    main()