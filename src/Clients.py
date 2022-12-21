#!/usr/bin/env python3

import streamlit as st
import DataManager as dm


def load():	
	# title
	st.markdown("# Clients")
	
	dm.display_table()

