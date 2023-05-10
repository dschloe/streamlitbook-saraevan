# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu

from home import run_home
from eda.eda_home import run_eda

def main():
    with st.sidebar:
        selected = option_menu("대시보드 메뉴", ['홈', '탐색적 자료분석', '부동산 예측'],
            icons=['house', 'file-bar-graph', 'graph-up-arrow'], menu_icon="cast", default_index=0)
    if selected == "홈":
        run_home()
    elif selected == "탐색적 자료분석":
        run_eda()
    elif selected == "부동산 예측":
        pass
    else:
        print("error..")

if __name__ == "__main__":
    main()