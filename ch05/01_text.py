# -*- coding:utf-8 -*-
import streamlit as st

def main():
    st.title("This is Text Elements")
    st.header("This is Header")
    st.subheader("This is sub Header")
    st.markdown("This text is :red[colored red], and this is **:blue[colored] ** and bold.")
    st.write("-" * 50)
    st.markdown("""
    ### SubChater 1
     - :red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:
    """)
    st.write("-" * 50)
    st.markdown("## Chapter 1. \n"
                "- Streamlit is **_really_ cool**.\n"
                "   * This text is : blue[colored blue], and this is **:red[colored] ** and bold.")


if __name__ == "__main__":
    main()