# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd

def main():
    tips = sns.load_dataset('tips')
    tip_max = tips['tip'].max()
    tip_min = tips['tip'].min()

    st.metric(label="Max Tip", value=tip_max,
              delta=tip_max - tip_min)
    st.metric(label="Min Tip", value=tip_min,
              delta=tip_min - tip_max)
    st.table(tips.describe())

if __name__ == "__main__":
    main()