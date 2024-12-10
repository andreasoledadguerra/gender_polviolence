
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, date
from pol_violence.plots import plot_fatalities_per_region, plot_region_event_ondemand, plot_all_region_event_highlight,plot_stacked_bar
from pol_violence.data_loaded import load_dataframe

def get_count_by_region_event(counts_dict: dict, region: str, event: str) -> int:
    return f"The number of {event} in {region} is {counts_dict[(region, event)]}"


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
st.write(f'{fatalities_per_region}')


# 'region' and 'sub_event_type' are related
grouped_counts = df_gpv.groupby('region')['sub_event_type'].value_counts()

# We grouped region and events to see counts
counts_dict = grouped_counts.to_dict()

        


# Create two selectboxes to perform fatalities per region
col1,_ = st.columns(2)

with col1:
    # Selectbox for choosing the variable 'region'
    option_region = st.selectbox(
    "Select region for explore fatalities",
    (df_gpv['region'].unique())
)

st.write("You selected:", option_region)

get_your_data = []
## A button to perform analysis is created
if st.button('Get your data'):     
    #st.write(f'{type(option_region)}')    
    st.write(f'The numbers of fatalities of {option_region} is {fatalities_per_region[option_region]}')


#Plot fatalities
fig, ax = plt.subplots()
ax.bar(fatalities_per_region.keys(), fatalities_per_region.values())
ax.set_xlabel('Region')
ax.set_ylabel('Fatalities')
ax.set_title('Region vs Fatalities')

plt.xticks(rotation=45)

if st.button('Get your plot'):
    st.write('This is a plot visualization of Region vs Fatalities')
    st.pyplot(fig) 

#Stacked Bar Chart of Sub-event Counts by Region
if st.button('Get your stacked plot'):
    st.write('This is a plot visualization of events counts by region')
    st.pyplot(plot_stacked_bar(grouped_counts))




# Variables for plot event-per-region on demand
col_1,col_2, = st.columns(2)

with col_1:
    #Selectbox for choosing the variable 'region'
    region_1 = st. selectbox(
        "Select region",
        (df_gpv['region'].unique())
)
    
with col_2:
    # Selectbox for choosing the variable 'event'
    event_1 = st.selectbox(
    "Select event",
    (df_gpv['sub_event_type'].unique())
)    

st.write("You selected:", region_1, event_1)

#A button to perform analysis is created
if st.button('Get your plot region/event colored on demand'):     
    
    st.write(f'This is a plot of {event_1} in {region_1}')
    st.pyplot(plot_region_event_ondemand(counts_dict, region_1,event_1))



col1_,col2_, = st.columns(2)

with col1_:
    #Selectbox for choosing the variable 'region'
    the_region = st. selectbox(
        "Select the region",
        (df_gpv['region'].unique())
)
    
with col2_:
    # Selectbox for choosing the variable 'event'
    the_event = st.selectbox(
    "Select the event",
    (df_gpv['sub_event_type'].unique())
)    

st.write("You selected:", the_region, the_event)


#A button to perform analysis is created
if st.button('Get your plot region/event highlighted'):     
    
    st.write(f'This is a plot of {the_event} in {the_region} highlighted')
    st.pyplot(plot_all_region_event_highlight(counts_dict, the_region,the_event))




