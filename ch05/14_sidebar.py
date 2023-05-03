# -*- coding:utf-8 -*-
import streamlit as st
import matplotlib.pyplot as plt
def main():
    value1 = st.sidebar.slider('Select a Value object notation', 0, 100)
    st.sidebar.write(value1)

    with st.sidebar:
        value2 = st.slider('Select a Value with notation', 0, 100)
        st.write(value2)
    value3 = st.slider('Select a Value just slider, 0, 100')
    st.write(value3)

    with st.sidebar:
        st.markdown('### Matplotlib Added on Sidebar')
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        st.pyplot(fig)

if __name__ == "__main__":
    main()

