import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import pandas as pd
import folium
from PIL import Image

# Page setting
st.set_page_config(layout="wide", page_title="공항 이상행동 탐지 솔루션")


# Markdown을 사용한 스타일링 타이틀
st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        color: #1B365C;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Welcome!</p>', unsafe_allow_html=True)


with st.sidebar: 
    st.markdown("""
    <style>
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100px;
    }
    </style>
    <img src=r'C:/Users/user/aivle school/빅프로젝트/대시보드/logo4.png'/>""", unsafe_allow_html=True)

    image = Image.open(r'C:\Users\user\aivle school\빅프로젝트\대시보드\logo4.png')
    st.sidebar.image(image, width=100, use_column_width=True)
    selected = option_menu("공항 이상행동 탐지 솔루션", ["Home", 'NewsMap', 'Donation'], 
        icons=['house', 'bi bi-globe', 'bi bi-currency-exchange'], menu_icon="airplane")
        
    selected