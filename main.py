
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

def plot_counts_events_per_region(df_same_region: dict, EVENT: str) -> object :
    # Create a color list based on the event type
    colors = ['r' if event == EVENT else 'darkslategray' for event in df_same_region['Event type']]
    
    # Plot the bar chart
    fig = plt.figure(figsize=(10, 6))
    plt.bar(df_same_region['Event type'], df_same_region['Count'], color=colors)
    plt.xlabel('Event type')
    plt.ylabel('Values')
    plt.title("Events type vs Values") 
    plt.xticks(rotation=90)
    plt.tight_layout()
    return fig

def same_event(df_same_event: pd.DataFrame, EVENT: str, REGION: str) -> object:

    colors = ['red' if region == REGION else 'darkslategray' for region in df_same_event['Region']]
    fig, ax = plt.subplots(figsize=(8,6))
    plt.bar(df_same_event['Region'], df_same_event['Count'], color=colors)
    ax.set_title(f"{EVENT} count in all regions", fontsize=16)
    ax.set_xlabel(EVENT,fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    return fig

def plot_counts_events_per_region(df_same_region: dict, EVENT: str) -> object :
    # Create a color list based on the event type
    colors = ['r' if event == EVENT else 'darkslategray' for event in df_same_region['Event type']]
    fig = plot_counts_events_per_region(df_same_region, EVENT)
    return fig 


def bifunction_event_region():
    valid_choices = ["A", "B", "Q"]
    is_input_ok = False
    
    while not is_input_ok:
        user_choice = input(" Choose an option:\n"
                          "'A' if you want to see same event across regions,\n"
                          "'B' if you want to see event counts per region,\n"
                          "'Q' if you want to quit\n")
                          
        if user_choice.upper() in valid_choices:
            if user_choice.upper() == 'A':
                process_same_event_option()
                is_input_ok = True
                
            elif user_choice.upper() == 'B':
                process_region_count_option()
                is_input_ok = True
                
            elif user_choice.upper() == 'Q':
                print("Outer function has finished executing.")
                is_input_ok = True
        else:
            print("Invalid choice. Please try again.")

def process_same_event_option():
    # Only work with df_same_event when option A is chosen
    event = input(f"Choose {EVENT}: ")
    region = input(f"Choose {REGION}: ")
    print(same_event(df_same_event, EVENT, REGION))

def process_region_count_option():
    # Only work with df_input_region when option B is chosen
    event = input(f"Choose {EVENT}: ")
    print(plot_counts_events_per_region(df_input_region, EVENT))

# Usage
if __name__ == "__main__":
    bifunction_event_region() 

        
fig = bifunction_event_region()
    




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

        

#events per region are grouped
event_per_region = df_gpv.groupby('sub_event_type')['region'].value_counts()

#we convert counts_event_per_region in a  dictionary
counts_event_per_region = event_per_region.to_dict()

# we convert our dictionary 'counts_event_per_region' into a Pandas DataFrame
df = pd.DataFrame.from_dict(counts_event_per_region, orient='index', columns=['Count'])

#we transform the tuple-based index into a MultiIndex
df.index = pd.MultiIndex.from_tuples(df.index, names=['Event type', 'Region'])

# index is reseted
df = df.reset_index()

#we grouped 'sub_event_type' and 'region' in a variable
event_per_region = df_gpv.groupby('sub_event_type')['region'].value_counts()

#we convert 'event_per_region' in a dictionary
counts_event_per_region = event_per_region.to_dict()

#We define the main variables 'REGION' and 'EVENT'
    #crear un input del usuario para el uso de estas dos variables

EVENT = 'zarasa'
REGION = ''
df_same_event = df[df['Event type'] == EVENT] 
df_same_region = df[df['Region'] == REGION] 

#Our function for plot events per region
fig = plot_counts_events_per_region(df_same_region, EVENT)

#Our function for plot same event
fig = same_event(df_same_event, EVENT, REGION)

#Our function for choose plot ('plot_counts_events_per_region' or 'same_event')
fig = bifunction_event_region(user_choice)


    


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


col_1_,col_2_, = st.columns(2)

with col_1_:
    REGION =st.selectbox(
        "Select the region",
        (df_gpv['Region'].unique())
)


with col_2_:
    EVENT =st.selectbox(
        "Select the event",
        (df_gpv['Event type'].unique())
)

st.write("You select:", REGION, EVENT)

if st.button('Get your plot of event in a region highlighted'):

    st.write(f'This is a plot of {EVENT} in {REGION} highlighted')
    st.pyplot(plot_counts_events_per_region(df_same_region, EVENT))


#Creating selectboxes for choose 'plot_counts_events_per_region' or 'same_event' using 'bifunction_event_region'
colA, ColB, ColQ = st.columns(3)

with colA:
    #Selectbox for choosing the variable A ("Plot same event per region")
    option_A =st.selectbox(
        "Select A for plot same event per region",
        (bifunction_event_region("A")) #?

)   

with ColB:
    #Selectbox for choosing the variable B ("Plot all events per region")
    option_B =st.selectbox(
        "Select A for plot all events per region",
        (bifunction_event_region("B"))#?

)

with ColQ:
    #Selectbox for choosing the variable Q ("Quit")
    option_Q =st.selectbox(
        "Select A for quit",
        (bifunction_event_region("Q"))#?

)
    
#A button to perform analysis is created
if st.button('Get your plot'):     
    
    st.pyplot(bifunction_event_region(user_choice))