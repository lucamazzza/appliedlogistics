#!/usr/bin/env python3
from st_aggrid import AgGrid
from distutils import errors
from distutils.log import error
import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
from itertools import count
from datetime import datetime
from pymongo import MongoClient

def get_database(dbname = 'AppliedLogistics'):
	
	# Provide the mongodb atlas url to connect python to mongodb using pymongo
	CONNECTION_STRING = "mongodb+srv://admin:Hus.lmamma04@appliedlogistics.op6cp7l.mongodb.net/test"
	
	# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
	client = MongoClient(CONNECTION_STRING)
	
	# Create the database for our example (we will use the same database throughout the tutorial
	return client[dbname]

def display_time():
	st.metric("",datetime.today().strftime("%H:%M:%S"),"")
	
def display_metrics(colnum = 4, indexes = ["Items", "Active processes", "Clients", "Tickets"], values = ["10000", "3", "110", "21"], deltas = ["-144", "+3", "0", "+2"]):
	cols = st.columns(colnum)
	for c in range(colnum):
		with cols[c]:
			if deltas[c] == "0":
				st.metric(indexes[c], values[c], deltas[c], delta_color="off")
			else:
				st.metric(indexes[c], values[c], deltas[c])

def display_table(grid_height = 347, data_amount = 30, return_mode = "FILTERED", update_mode = "GRID_CHANGED", enable_pagination = True):
	np.random.seed(42)
	
	return_mode_value = DataReturnMode.__members__[return_mode]
	update_mode_value = GridUpdateMode.__members__[update_mode]
	
	#enterprise modules
	enable_selection = True
	if enable_selection:
		selection_mode = 'multiple'
		groupSelectsChildren = True
		groupSelectsFiltered = True
		
	
	
	df = fetch_data()
	
	#Infer basic colDefs from dataframe types
	gb = GridOptionsBuilder.from_dataframe(df)
	gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
	
		
	if enable_selection:
		gb.configure_selection(selection_mode)
		gb.configure_selection(selection_mode, use_checkbox=True, groupSelectsChildren=groupSelectsChildren, groupSelectsFiltered=groupSelectsFiltered)
		
	if enable_pagination:
		#gb.configure_pagination(paginationAutoPageSize=True)
		gb.configure_pagination(paginationAutoPageSize=False)
		
	gb.configure_grid_options(domLayout='normal')
	gridOptions = gb.build()
	grid_response = AgGrid(
		df, 
		gridOptions=gridOptions,
		height=grid_height, 
		width='100%',
		data_return_mode=return_mode_value, 
		update_mode=update_mode_value,
		fit_columns_on_grid_load= True,
		allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
		enable_enterprise_modules=True,
		)
	
	df = grid_response['data']
	selected = grid_response['selected_rows']
	selected_df = pd.DataFrame(selected).apply(pd.to_numeric, errors='coerce')
	
def configure_table(cols = ["col1", "col2"], types=[["dateColumnFilter", "customDateTimeFormat"], ["numericColumn","numberColumnFilter","customNumericFormat"]]):
	for c in range(len(cols)):
		#customize gridOptions
		gb.configure_column(cols[c], type=types[c], custom_format_string='yyyy-MM-dd', pivot=True)
		gb.configure_column("date_tz_aware", type=["dateColumnFilter","customDateTimeFormat"], custom_format_string='yyyy-MM-dd HH:mm zzz', pivot=True)
		gb.configure_column("apple", type=["numericColumn","numberColumnFilter","customNumericFormat"], precision=2, aggFunc='sum')
		gb.configure_column("banana", type=["numericColumn", "numberColumnFilter", "customNumericFormat"], precision=1, aggFunc='avg')
		gb.configure_column("chocolate", type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"], custom_currency_symbol="R$", aggFunc='max')
		
	#configures last row to use custom styles based on cell's value, injecting JsCode on components front end
	cellsytle_jscode = JsCode("""
	function(params) {
		if (params.value == 'A') {
			return {
				'color': 'white',
				'backgroundColor': 'darkred'
			}
		} else {
			return {
				'color': 'white',
				'backgroundColor': 'transparent'
			}
		}
	};
	""")
	gb.configure_column("group", cellStyle=cellsytle_jscode)
	
# Data fetching, to be integrated with DB
@st.cache(allow_output_mutation=True)
def fetch_data():
	dbname = get_database()
	collection_name = dbname['clients']
	items = collection_name.find()
	items_df = pd.DataFrame(items)
	return items_df