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


def plot_stacked_bar(grouped_counts: pd.DataFrame) -> object:
    stacked_df = grouped_counts.unstack(fill_value=0)  

    plt.figure(figsize=(12, 6))
    fig = stacked_df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))

    plt.title('Stacked Bar Chart of Sub-event Counts by Region')
    plt.xlabel('Region')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

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
    return plt.gcf()  # Return the current figure

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
