#!/usr/bin/env python3

import Dashboard as d
import Inventory as i
import Clients as c
import Fetching as f
import Automatic_Fetching as af
import Tickets as t

from st_on_hover_tabs import on_hover_tabs
import streamlit as st
def load():
	st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
	
	with st.sidebar:
		tabs = on_hover_tabs(tabName=["Dashboard", 'Inventory', 'Clients', 'Fetching', 'Automatic Fetching', 'Tickets', 'Logout'], 
							iconName=['dashboard', 'inventory', 'groups', 'change_circle', 'arrow_circle_down', 'confirmation_number', 'account_circle'], 
							styles = {
								'navtab': {'background-color':'#111', 'color': '#818181', 'font-size': '18px', 'transition': '.3s', 'white-space': 'nowrap', 'text-transform': 'uppercase'},
								'tabOptionsStyle': {':hover :hover': {'color': 'red', 'cursor': 'pointer'}},
								'iconStyle':{'position':'fixed', 'left':'7.5px', 'text-align': 'left'}, 
								'tabStyle' : {'list-style-type': 'none', 'margin-bottom': '30px', 'padding-left': '30px'}},
							default_choice=0)
		
	if tabs =='Dashboard':
		d.load()
		
	elif tabs == 'Inventory':
		i.load()
		
	elif tabs == 'Clients':
		c.load()
		
	elif tabs == 'Fetching':
		f.load()
		
	elif tabs == 'Automatic Fetching':
		af.load()
		
	elif tabs == 'Tickets':
		t.load()
		
	elif tabs == 'Logout':
		i.load()