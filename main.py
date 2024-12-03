"""TODO Challenge: armar un main.py nuevo llamado 'main2.py' , que debe ser muy simple. COndicion 1: 
1.Crear dos páginas (la ilusión de que son dos páginas). Debe contener: pag 1 y pag 2 debe tener un st.write diferente 
(estoy en la página 1/estoy en la página 2)
2. Debe haber una lista desplegable que me permita cambiar de página."""

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

def plot_stacked_bar(grouped_counts: pd.DataFrame) -> object:
    stacked_df = grouped_counts.unstack(fill_value=0)  

    plt.figure(figsize=(12, 6))
    fig_1 = stacked_df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))

    plt.title('Stacked Bar Chart of Sub-event Counts by Region')
    plt.xlabel('Region')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()


    return fig_1

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


# A variable for exploring 'notes' is created
#col3,col4 = st.columns(2)

#with col3:
    # Selectbox for choosing the variable 'region'
    #region = st.selectbox(
    #"Select region",
    #(df_gpv['region'].unique())
#)
    
#with col4:
    #Selectbox for choosing the variable 'event'
    #event = st. selectbox(
        #"Select event",
        #(df_gpv['sub_event_type'].unique())
#)

## A button to perform analysis is created
#if st.button('Get your number of event per region'):    
    #st.write(get_count_by_region_event(counts_dict, region, event))     
    #st.write(f'The numbers of fatalities of {option_region} is {fatalities_per_region[option_region]}')

#The output is ALWAYS "The number of Attack in africa is 3036"
#for call function we need 'counts_dict', and user put 'region' and 'event' and it must to be related with the counts of event
#st.write({df_gpv[df_gpv['region']== option_region].iloc[0]['notes']})



#Stacked Bar Chart of Sub-event Counts by Region

def plot_stacked_bar(grouped_counts: pd.DataFrame) -> plt.Figure:
    stacked_df = grouped_counts.unstack(fill_value=0)
    plt.figure(figsize=(12, 6))
    stacked_df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))
    plt.title('Stacked Bar Chart of Sub-event Counts by Region')
    plt.xlabel('Region')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()  # Return the current figure

if st.button('Get your stacked plot'):
    st.write('This is a plot visualization of events counts by region')
    st.pyplot(plot_stacked_bar(grouped_counts))



#Plot Region-Event on Demand

def plot_region_event_ondemand(counts_dict: dict, region: str, event: str) -> object:
    
    filtered_data = {(region, event): counts_dict.get((region, event), 0)}# Returns the value if found, and 0 if not found (default value)

    x_labels = [f"{region} - {event}"]  # Single bar for the specified region-event
    colors = ['mediumslateblue']  # Highlight color for the bar

    fig, ax = plt.subplots(figsize=(6, 4))

    bars = ax.bar(x_labels, filtered_data.values(), color=colors)

    ax.set_xlabel('Event per Region', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Counting Events per Region', fontsize=14)
    ax.tick_params(axis='x', rotation=0)

    plt.close()
    return fig

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



#The higlighted one button
def plot_all_region_event_highlight(counts_dict: dict, region: str, event: str) -> object:

    colors = []
    x_etiquette = []
    values = []

    for (key, value) in counts_dict.items():
        x_etiquette.append(f"{key[0]} - {key[1]}")
        values.append(value)
        
        # Highlight selected region-event
        if key == (region, event):
            colors.append('c')
        else:
            colors.append('darkslategray')
    
    # Create figure and axes
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create bars
    bars = ax.bar(x_etiquette, values, color=colors)
    
    # Add value labels on top of bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,}',
                ha='center', va='bottom')
    
    ax.set_xlabel('Events per Region', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title(f'Event Counts by Region (Highlighting {region} - {event})', 
                 fontsize=14)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90, ha='right')
    
    # Add grid
    ax.grid(True, linestyle='--', alpha=0.7, axis='y')
    
    # Adjust layout
    plt.tight_layout()
    plt.close()
    return fig

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




