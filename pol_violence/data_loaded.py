import pandas as pd
from datetime import date
def load_dataframe() -> pd.DataFrame :
    
    # Dataset is downloaded
    df_gpv = pd.read_csv("gender_Sep27-1.csv")
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

    return df_gpv