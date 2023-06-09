import pandas as pd
from numpy import random

from config.Columns import Columns


def get_random_snippets(data: pd.DataFrame, column: Columns, count: int, time_filter: int) -> pd.DataFrame:
    '''
    Takes a data frame in and randomly selects 50 snippets from it,
    filtering out +/- 180 seconds from each selected segment.

    Parameters:
    data : Pandas DataFrame
        DataFrame with data pulled in from input file.

    Returns
    Pandas DataFrame
        DataFrame of the requested number of random snippets in order by start time.
    '''
    output = pd.DataFrame(columns=data.columns)

    print(f"Selecting {count} random snippets with nonzero {column} at least +/- {time_filter} seconds apart...")
    while len(output) < count and len(data) > 0:
        random_index = random.randint(0, len(data))
        random_row = data[random_index:random_index+1]
        filter_start = random_row.values[0][1] - time_filter
        filter_end = random_row.values[0][2] + time_filter
        data = data[(data["SegStart"] > filter_end) | (data["SegEnd"] < filter_start)]
        output = output.append(random_row)

    return output.sort_values(by="SegStart")

def get_ordered_snippets(data: pd.DataFrame, column: Columns, count: int, time_filter: int) -> pd.DataFrame:
    '''
    Takes a data frame in and searches for the top 50 snippets from it with given time filter,
    filtering out +/- 180 seconds from each selected segment.

    Parameters:
    data : Pandas DataFrame
        DataFrame with data pulled in from input file.

    Returns
    Pandas DataFrame
        DataFrame of the requested number of ordered snippets.
    '''
    output = pd.DataFrame(columns=data.columns)

    print(f"Selecting {count} top snippets by {column} at least +/- {time_filter} seconds apart...")
    output = output.append(data[:1])

    while len(output) < count and len(data) > 0:
        filter_start = output.values[-1][1] - time_filter
        filter_end = output.values[-1][2] + time_filter
        data = data[(data["SegStart"] > filter_end) | (data["SegEnd"] < filter_start)]
        output = output.append(data[:1])

    return output.sort_values(by="SegStart")
