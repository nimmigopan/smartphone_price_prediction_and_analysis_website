import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# A website for Smartphones")


st.markdown(
    """
    This website will provide you with informations related to smartphones available in market.
    There are 2 modules in this website:-
    
    ### Analytics Module:
    This module provides graphical analysis of different factors such as phone brand name, processor brand, ram, rom, refresh rate,
    resolution, speed of processor with price of phones
    
    ### Price Prediction Module
    This module will predict the price of phones according to different specifications
    
"""
)