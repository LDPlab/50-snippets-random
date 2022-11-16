import pandas as pd
from numpy import random


def get_random_snippets(data: pd.DataFrame, is_tvn: bool, count: int) -> pd.DataFrame:
    '''
    Takes a data frame in and randomly selects 50 snippets from it,
    filtering out +/- 180 seconds from each selected segment.

    Parameters:
    data : Pandas DataFrame
        DataFrame with data pulled in from input file.

    Returns
    Pandas DataFrame
        DataFrame of the 50 random snippets in order by start time.
    '''
    output = pd.DataFrame(columns=data.columns)

    if is_tvn:
        TIME_FILTER_IN_SECONDS = 60
    else:
        TIME_FILTER_IN_SECONDS = 180

    print(f"Selecting {count} random snippets at least +/- {TIME_FILTER_IN_SECONDS} seconds apart...")
    while len(output) < count and len(data) > 0:
        random_index = random.randint(0, len(data))
        random_row = data[random_index:random_index+1]
        filter_start = random_row.values[0][2] - TIME_FILTER_IN_SECONDS
        filter_end = random_row.values[0][3] + TIME_FILTER_IN_SECONDS
        data = data[(data["SegStart"] > filter_end) | (data["SegEnd"] < filter_start)]
        output = output.append(random_row)

    return output.sort_values(by="SegStart")

def get_ordered_snippets(data: pd.DataFrame, is_tvn: bool, count: int) -> pd.DataFrame:
    '''
    Takes a data frame in and searches for the top 50 snippets from it with given time filter,
    filtering out +/- 180 seconds from each selected segment.

    Parameters:
    data : Pandas DataFrame
        DataFrame with data pulled in from input file.

    Returns
    Pandas DataFrame
        DataFrame of the 50 random snippets in order by start time.
    '''
    output = pd.DataFrame(columns=data.columns)

    if is_tvn:
        TIME_FILTER_IN_SECONDS = 60
    else:
        TIME_FILTER_IN_SECONDS = 180

    print(f"Selecting {count} ordered snippets at least +/- {TIME_FILTER_IN_SECONDS} seconds apart...")
    output = output.append(data[:1])

    while len(output) < count:
        filter_start = output.values[-1][2] - TIME_FILTER_IN_SECONDS
        filter_end = output.values[-1][3] + TIME_FILTER_IN_SECONDS
        data = data[(data["SegStart"] > filter_end) | (data["SegEnd"] < filter_start)]
        output = output.append(data[:1])

    return output.sort_values(by="SegStart")
