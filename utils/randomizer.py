import pandas as pd
from numpy import random


def get_50_random_snippets(data: pd.DataFrame, is_tvn: bool) -> pd.DataFrame:
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

    print(f"Selecting 50 random snippets at least +/- {TIME_FILTER_IN_SECONDS} seconds apart...")
    while len(output) < 50 and len(data) > 0:
        random_index = random.randint(0, len(data))
        random_row = data[random_index:random_index+1]
        filter_start = random_row.values[0][2] - TIME_FILTER_IN_SECONDS
        filter_end = random_row.values[0][2] + TIME_FILTER_IN_SECONDS
        data = data[(data["SegStart"] > filter_end) | (data["SegStart"] < filter_start)]
        output = output.append(random_row)

    return output.sort_values(by="SegStart")
