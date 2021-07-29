import pandas as pd
import os


def get_data(filename: str) -> pd.DataFrame:
    '''
    Generates a Pandas DataFrame of the top 100 Adult Word Count [AWC] rows from input file.
    May return rows that have 0 AWC.

    Parameters:
    filename : str
        The filename to use to load DataFrame.

    Returns:
    Pandas DataFrame
        A DataFrame of the top 100 rows by AWC from file data.
    '''
    os.chdir("input")
    if filename[-4:] == ".csv":
        data = pd.read_csv(filename)
    elif filename[-4:] == ".xls" or filename[-5:] == ".xlsx":
        data = pd.read_excel(filename)
    else:
        raise ValueError("File extension not supported")

    for col in data.columns[4:]:
        del data[col]

    top_100_awc_data = data.sort_values(by=data.columns[3], ascending=False)[:100]
    top_100_awc_data.insert(3, "SegEnd", data[data.columns[2]] + 30)
    top_100_awc_data.columns = ["Index", "Time", "SegStart", "SegEnd", "AWC"]

    os.chdir("..")
    return top_100_awc_data


def write_output(data: pd.DataFrame, filename: str):
    '''
    Writes the 50 random snippets to an excel sheet.

    Parameters:
    data : Pandas DataFrame
        The 50 snippets to write out.
    filename : str
        The name of the output file.
    '''
    os.chdir("output")
    data.to_excel(filename, index=False)
    os.chdir("..")
