# -*- coding:utf-8 -*-
import streamlit as st

def main():
    st.title("Hello World")
    x = st.slider('x')
    st.write(x, "x 2 = ", x * 2)

if __name__ == "__main__":
    main()