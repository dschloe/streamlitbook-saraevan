# -*- coding:utf-8 -*-
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Streamlit with Matplotlib")
    tips = sns.load_dataset('tips')
    m_tips = tips.loc[tips['sex'] == 'Male']
    f_tips = tips.loc[tips['sex'] == 'Female']
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x = m_tips['total_bill'], y = m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x = f_tips['total_bill'], y = f_tips['tip'])
    ax[1].set_title('Female')
    fig.supxlabel('Total Bill($)')
    fig.supylabel('Tip($)')
    st.pyplot(fig)

if __name__ == "__main__":
    main()