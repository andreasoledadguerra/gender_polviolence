import pandas as pd
import matplotlib.pyplot as plt


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



def plot_region_event_ondemand(counts_dict: dict, region: str, event: str) -> object:
    filtered_data = {(region, event): counts_dict.get((region, event), 0)}
    x_labels = [f"{region} - {event}"]
    colors = ['mediumslateblue']

    fig, ax = plt.subplots(figsize=(6, 4))

    bars = ax.bar(x_labels, filtered_data.values(), color=colors)

    ax.set_xlabel('Event per Region', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Counting Events per Region', fontsize=14)
    ax.tick_params(axis='x', rotation=0)

    plt.close()
    return fig



def plot_fatalities_per_region(fatalities_per_region: dict, region: str) -> object:

    colors = []
    for reg in fatalities_per_region.keys():
        if reg == region:
            colors.append('darkslategray')
        else:
            colors.append('m')

    the_plot_bar_fpr = plt.bar(fatalities_per_region.keys(), fatalities_per_region.values(), color=colors) 
    print(type(the_plot_bar_fpr))
    
    plt.xlabel('Region')
    plt.ylabel('Fatalities')
    plt.title('Fatalities per region')  
    
    plt.xticks(rotation=45)
    
    return the_plot_bar_fpr


def plot_all_region_event_highlight(counts_dict: dict, region: str, event: str) -> object:

    colors = []
    x_etiquette = []
    values = []
    
    for (key, value) in counts_dict.items():
        x_etiquette.append(f"{key[0]} - {key[1]}")
        values.append(value)
        
        if key == (region, event):
            colors.append('c')
        else:
            colors.append('darkslategray')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars = ax.bar(x_etiquette, values, color=colors)
    

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,}',
                ha='center', va='bottom')
    
    ax.set_xlabel('Events per Region', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title(f'Event Counts by Region (Highlighting {region} - {event})', 
                 fontsize=14)
    
    plt.xticks(rotation=90, ha='right')
    
    ax.grid(True, linestyle='--', alpha=0.7, axis='y')
    

    plt.tight_layout()
    plt.close()
    return fig


def plot_stacked_bar(grouped_counts: pd.DataFrame, 
                     figsize= (10,6),
                     colormap= 'viridis',
                     title= 'Stacked Regions vs Events ',
                     xlabel= 'Regions',
                     ylabel= 'Events count',
                     rotation=45)-> object:
    
    stacked_df = grouped_counts.unstack(fill_value=0)
    
    plt.figure(figsize=figsize)
    stacked_df.plot(kind='bar', stacked=True, colormap=colormap, figsize=figsize)
    
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.tight_layout()
    
    return plt
