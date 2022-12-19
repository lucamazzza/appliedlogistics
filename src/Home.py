#!/usr/bin/env python3
import streamlit as sl
import Automatic_Fetching as af 
import Clients as c
import Fetching as f
import Inventory as i
import Tickets as t
import Dashboard as d
import Sidebar as sb


#sl.markdown(""" <style>
#MainMenu {visibility: hidden;}
#footer {visibility: hidden;}
#</style> """, unsafe_allow_html=True)
sl.set_page_config(layout="wide")
sb.load()

	