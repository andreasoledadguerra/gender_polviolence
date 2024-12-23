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
