"""TODO ver en python lo que es el scope de variable"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#asd = 'lo que quieras' -> es una variable global, puede ser llamada en cualquier scope
#def sarasa():
    #asd = 'lo que quieras' # es una variable local, sóo puede ser invocada si es llamada la función

class DataProcessor:
    def __init__(self, df_gpv: pd.DataFrame, grouped_counts: pd.Series,  fatalities_per_region: dict, counts_dict: dict, region: str, event: str, color:list):
        self.df_gpv = df_gpv
        self.region = region
        self.event = event
        self.grouped_counts = grouped_counts
        self.fatalities_per_region = fatalities_per_region
        self.counts_dict = counts_dict
        self.region = region
        self.event = event
        self.color = color

    def plot_stacked_bar(grouped_counts: pd.DataFrame) -> object:

        stacked_df = grouped_counts.unstack(fill_value=0)  
        plt.figure(figsize=(12, 6))
        fig = stacked_df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))

        return fig
    

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
    
