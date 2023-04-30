# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Streamlit with Seaborn")
    tips = sns.load_dataset('tips')
    m_tips = tips.loc[tips['sex'] == 'Male']
    f_tips = tips.loc[tips['sex'] == 'Female']
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    sns.scatterplot(data=m_tips, x = 'total_bill', y = 'tip', ax=ax[0])
    ax[0].set_title('Male')
    sns.scatterplot(data=f_tips, x = 'total_bill', y = 'tip', ax=ax[1])
    ax[0].set(xlabel=None, ylabel=None)
    ax[1].set_title('Female')
    ax[1].set(xlabel=None, ylabel=None)
    fig.supxlabel('Total Bill($)')
    fig.supylabel('Tip($)')
    st.pyplot(fig)

if __name__ == "__main__":
    main()