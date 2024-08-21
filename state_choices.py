"""from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px
from faicons import icon_svg
from shinywidgets import render_plotly


from shiny import reactive
from shiny.express import input, render, ui

df = pd.read_csv("Metro_new_listings_uc_sfrcondo_sm_month.csv")
for_sale_inventory_df2 = df["StateName"].fillna("United States")
for_sale_inventory_df2 = df["StateName"].drop_duplicates()
for_sale_inventory_df2 = for_sale_inventory_df2.sort_values().tolist()
STATE_CHOICES = for_sale_inventory_df2
print(STATE_CHOICES)
"""
STATE_CHOICES = [
'United States', 
'AK', 
'AL', 
'AR', 
'AZ', 
'CA', 
'CO', 
'CT',
'DC', 
'DE', 
'FL', 
'GA', 
'HI', 
'IA', 
'ID', 
'IL', 
'IN', 
'KS', 
'KY', 
'LA', 
'MA', 
'MD', 
'ME', 
'MI', 
'MN', 
'MO', 
'MS', 
'MT', 
'NC', 
'ND', 
'NE', 
'NH', 
'NJ', 
'NM', 
'NV', 
'NY', 
'OH', 
'OK', 
'OR', 
'PA', 
'RI', 
'SC',
'SD', 
'TN', 
'TX', 
'UT', 
'VA', 
'VT', 
'WA', 
'WI', 
'WV', 
'WY'
]