# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Check Box Control")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    show_plot = st.checkbox("시각화 보여주기")

    fig, ax = plt.subplots()
    ax.plot(x, y)

    if show_plot:
        st.pyplot(fig)

if __name__ == '__main__':
    main()