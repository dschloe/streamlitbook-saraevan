# -*- coding:utf-8

import pandas as pd
import streamlit as st


def showMap(total_df):
    st.dataframe(total_df.head())