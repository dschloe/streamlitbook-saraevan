# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

def main():
    with st.sidebar:
        st.header("Sidebar")
        day = st.selectbox("Select a day", ["Thur", "Fri", "Sat", "Sun"])

    tips = sns.load_dataset("tips")
    filtered_tips = tips[tips["day"] == day]
    top_bill = filtered_tips["total_bill"].max()
    top_tip = filtered_tips["tip"].max()

    tab1, tab2, tab3 = st.sidebar.tabs(["Total Bill", "Tip", "Size"])

    with tab1:
        fig, ax = plt.subplots()
        st.header("Total Bill Amounts")
        sns.histplot(filtered_tips["total_bill"], kde=False, ax=ax)
        st.pyplot(fig)
    with tab2:
        fig, ax = plt.subplots()
        st.header("Tip Amounts")
        sns.histplot(filtered_tips["tip"], kde=False, ax=ax)
        st.pyplot(fig)
    with tab3:
        fig, ax = plt.subplots()
        st.header("Table Sizes")
        sns.boxplot(data=filtered_tips, x="sex", y="tip", ax=ax)
        st.pyplot(fig)

    container = st.container()
    col1, col2 = container.columns([1, 2])

    with col1:
        st.metric("Top Bill", f"${top_bill:.2f}")

    with col2:
        st.metric("Top Tip", f"${top_tip:.2f}")

    with container:
        with st.expander("Data Frame"):
            st.dataframe(filtered_tips)
        st.write("This is the footer1")

    st.write("This is the footer2")

    with container:
        st.write("This is the footer3")

    with container:
        st.empty()

    st.write("This is the footer4")


if __name__ == "__main__":
    main()