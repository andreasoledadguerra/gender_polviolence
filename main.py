import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, date
from pol_violence.plots import plot_fatalities_per_region, plot_region_event_ondemand, plot_all_region_event_highlight,plot_stacked_bar
from pol_violence.data_loaded import load_dataframe

st.title('Political Violence across the world Data Explorer')
st.text('This is a web app to explore political violence data')

# dataframe is loaded
df_gpv = load_dataframe()

st.dataframe(df_gpv)




# A dictionary is created
region_map = {
    'africa': ['Southern Africa', 'Northern Africa', 'Middle Africa', 'Western Africa', 'Eastern Africa'],
    'middle east': ['Middle East'],
    'asia':['Caucasus and Central Asia', 'Sotheast Asia', 'South Asia', 'East Asia'],
    'america and caribbean' :[ 'South America', 'North America', 'Central America', 'Caribbean'],
    'europe': ['Europe'],
    'oceania': ['Oceania']
}

# Flatten the mapping to map each element to its group

flattened_map = {}
for key, values in region_map.items():
    for item in values:
        flattened_map[item] = key


#new_column = {'region': ['america', 'middle east', 'asia', 'america and caribbean', 'europe', 'oceania']}
df_gpv['region'] = df_gpv['region'].map(flattened_map)


#'region' and 'fatalities' are related 
group_region_fatalities = df_gpv.groupby('region')['fatalities'].sum()

# We convert that columns in a dictionary for plotting manipulation
fatalities_per_region = group_region_fatalities.to_dict()

# 'region' and 'sub_event_type' are related
grouped_counts = df_gpv.groupby('region')['sub_event_type'].value_counts()

# We grouped region and events to see counts
counts_dict = grouped_counts.to_dict()

# A function that gives the number of event per region is created
region = df_gpv['region'].any()
event = df_gpv['sub_event_type'].any()

def get_count_by_region_event(counts_dict: dict, region: str, event: str) -> int:
    for (region,event), counts in counts_dict.items():
        return f"The number of {event} in {region} is {counts_dict[(region, event)]}"
    
# A variable for exploring 'notes' is created
explore_notes = df_gpv[df_gpv['fatalities']== 750].iloc[0]['notes']


#fig, ax = plt.subplots(1,1)
#ax.plot([0,1.1,2,0.7])
#st.pyplot(fig)