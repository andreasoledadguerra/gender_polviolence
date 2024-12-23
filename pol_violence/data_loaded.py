import pandas as pd
from datetime import date
from pol_violence.const import PATH_DATA_DF, COL_REGION 

def map_region_to_normalized_region(df_gpv: pd.DataFrame) -> pd.DataFrame:
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


    #new_column = {'COL_REGION': ['america', 'middle east', 'asia', 'america and caribbean', 'europe', 'oceania']}
    df_gpv['COL_REGION'] = df_gpv['COL_REGION'].map(flattened_map)
    return df_gpv


def load_dataframe() -> pd.DataFrame :
    # Dataset is downloaded
    df_gpv = pd.read_csv(PATH_DATA_DF)
    df_gpv.drop([
        'event_id_cnty',
        #'event_date', 
        'year', 
        'time_precision',
        'disorder_type', 
        #'event_type', 
        #'sub_event_type', 
        'actor1',
        'assoc_actor_1', 
        #'inter1', 
        'actor2', 
        'assoc_actor_2', 
        'inter2',
        #'interaction', 
        'civilian_targeting', 
        #'iso',
        #'region', 
        #'country',
        'admin1', 
        'admin2', 
        'admin3', 
        #'location', 
        #'latitude', 
        #'longitude',
        'geo_precision', 
        'source', 
        'source_scale', 
        #'notes', 
        #'fatalities',
        'tags',
        'timestamp'                           
    ], axis=1, inplace=True)
    df_gpv["date"] = df_gpv["event_date"].apply(date.fromisoformat)

    df_gpv = map_region_to_normalized_region(df_gpv)

    return df_gpv