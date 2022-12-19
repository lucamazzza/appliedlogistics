#!/usr/bin/env python3

import streamlit as sl
import pandas as pd
from streamlit_option_menu import option_menu

import Automatic_Fetching as af 
import Clients as c
import Fetching as f
import Inventory as i
import Tickets as t
import Dashboard as d

def load():	
	with sl.sidebar:
		selected = option_menu("Applied Logistic", ["Dashboard", 'Inventory', 'Clients', 'Fetching', 'Automatic Fetching', 'Tickets'],
			icons=['speedometer', 'box-seam', "person", 'arrow-down', 'arrow-repeat', 'ticket'],
			menu_icon="boxes", default_index=0,
			styles={
				"container": {"padding": "0!important", "background-color": "transparent"},
				"icon": {"color": "grey", "font-size": "15px"}, 
				"nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#222"},
				"nav-link-selected": {"background-color": "#111"},
			})
	if selected == 'Dashboard':
		d.load()
		
	if selected == 'Inventory':
		i.load()
	
	if selected == 'Clients':
		c.load()
		
	if selected == 'Fetching':
		f.load()
	
	if selected == 'Automatic Fetching':
		af.load()
		
	if selected == 'Tickets':
		t.load()
		