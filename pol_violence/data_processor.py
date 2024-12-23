from typing import Tuple
import pandas as pd
from pol_violence.const import COL_REGION, COL_FATALITIES, COL_SUB_EVENT_TYPE


def get_fatalites_per_region(df_gpv: pd.DataFrame) -> dict:
    """ Convert columns in a dictionary, key=region, value=total_sum_of_fatalities."""
    return df_gpv.groupby(COL_REGION)[COL_FATALITIES].sum().to_dict()

def get_counts_dict_and_df_stacked(df_gpv: pd.DataFrame) -> Tuple[dict, pd.DataFrame]:
    # COL_REGION and COL_SUB_EVENT_TYPE are related.
    grouped_counts = df_gpv.groupby(COL_REGION)[COL_SUB_EVENT_TYPE].value_counts()
    df_stacked = grouped_counts.unstack(fill_value=0)

    # We grouped region and events to see counts.
    counts_dict = grouped_counts.to_dict()
    return counts_dict, df_stacked

def get_df_same_event_and_region(df_gpv: pd.DataFrame, event_input: str, region_input: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    # We grouped COL_SUB_EVENT_TYPE and COL_REGION in a variable.
    event_per_region = df_gpv.groupby(COL_SUB_EVENT_TYPE)[COL_REGION].value_counts()

    # We convert 'event_per_region' in a dictionary.
    counts_event_per_region = event_per_region.to_dict()

    # We convert our dictionary 'count_event_per_region' into a Pandas DataFRame.
    df_same_aux =pd.DataFrame.from_dict(counts_event_per_region, orient='index', columns=['Count'])

    # We transform the tuple-based index into a MultiIndex.
    df_same_aux.index = pd.MultiOndex.from_tuples(df_same_aux.index, names=['Event type', 'Region']) #FIXME: 'Region'

    # Index is reseted.
    df_same_aux = df_same_aux.reset_index()

    # We define the main variables 'REGION' and 'EVENT'
    df_same_event = df_same_aux[df_same_aux['Event type'] == event_input]
    df_same_region = df_same_aux[df_same_aux['Region'] == region_input]
    return df_same_event, df_same_region



def plot_fatalities_per_region(self) -> object:

    the_plot_bar_fpr = plt.bar(self.fatalities_per_region.keys(), self.fatalities_per_region.values()) #color= colors) 
    return the_plot_bar_fpr 


def plot_region_event_ondemand(self, region:str, event:str) -> object:

    filtered_data = {(region, event): self.counts_dict.get((region, event), 0)}

    x_labels = [f"{region} - {event}"] 
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['mediumslateblue']
    bars = ax.bar(x_labels, filtered_data.values(), color=colors)
    ax.set_xlabel('Event per Region', fontsize=12)
    ax.set_ylabel('Count', fontsize=12)
    ax.set_title('Counting Events per Region', fontsize=14)
    ax.tick_params(axis='x', rotation=0)
    plt.close()
    return fig
def plot_all_region_event_highlight(self, region:str, event: str) -> object:

    colors = []
    x_etiquette = []
    values = []


    for (key, value) in self.counts_dict.items():
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
