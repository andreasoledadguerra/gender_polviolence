import pandas as pd
import matplotlib.pyplot as plt

def plot_fatalities_per_region(fatalities_per_region: dict)-> object:

    fig = plt.bar(fatalities_per_region.keys(), fatalities_per_region.values())
    plt.xlabel('Region')
    plt.ylabel('Fatalities')
    plt.title('Region vs Fatalities')
    plt.xticks(rotation=45)

    plt.show()

    return fig

def plot_stacked_bar(grouped_counts: pd.DataFrame) -> plt.Figure:
    stacked_df = grouped_counts.unstack(fill_value=0)
    plt.figure(figsize=(12, 6))
    stacked_df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))

    plt.title('Stacked Bar Chart of Sub-event Counts by Region')
    plt.xlabel('Region')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig = plt.gcf()  # Return the current figure
    return fig



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
    
    # Plot the bar chart
    fig = plt.figure(figsize=(10, 6))
    plt.bar(df_same_region['Event type'], df_same_region['Count'], color=colors)
    plt.xlabel('Event type')
    plt.ylabel('Values')
    plt.title("Events type vs Values") 
    plt.xticks(rotation=90)
    plt.tight_layout()
    return fig

def bifunction_event_region(user_choice):
    valid_choices = ["A","B","Q"]
    is_input_ok = False

    while not is_input_ok:
        user_choice = input(" Choose an option:\n"
        "'A' if you want to see same event across regions,\n"
        "'B' if you want to see event counts per region,\n"
        "'Q' if you want to quit\n")
        
        if user_choice.upper() in valid_choices:
            #choose event and region
            if user_choice.upper() == 'A':
                df_same_event
                input_event = input(f"Choose {EVENT}")
                input_region = input(f"Choose {REGION}")
                print(same_event(df_same_event, EVENT, REGION))
                is_input_ok =True
                
            #choose event
            elif user_choice.upper() == 'B':
                df_input_region
                input_event = input(f"Choose {EVENT}")
                print(plot_counts_events_per_region(df_input_region, EVENT))
                is_input_ok = True
                

            elif user_choice.upper() == 'Q':
                print("Outer function has finished executing.")
                is_input_ok = True
        else:
            print("Invalid choice. Please try again.")