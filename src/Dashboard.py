#!/usr/bin/env python3

import pandas as pd
import streamlit as st
import numpy as np
import DataManager as dm

def load():
	# title
	st.markdown("# Dashboard")
	dm.display_metrics(6, ["Items", "Active processes", "Clients", "Automatic processes", "Tickets", "Errors"], ["103423", "32", dm.fetch_data(), "12", "1", "2"], ["-12", "30", "-11", "1", "-10", "-11"])

		