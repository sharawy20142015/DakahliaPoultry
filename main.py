import pandas as pd 
import streamlit as st
from streamlit_option_menu import option_menu  
import PuchAndSales
import HomePage
class MultiPage:
    def __init__(self) :
        pass
    def run():
        with st.sidebar:
            page=option_menu(
            menu_title='',
            options=['HomePage','PuchAndSales'],
            default_index=1)
        if page=='PuchAndSales':
            PuchAndSales.app()
        if page=='HomePage':
            HomePage.app()

    run()