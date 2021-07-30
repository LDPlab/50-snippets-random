import pandas as pd
import os


def get_data(filename: str, is_random: bool) -> pd.DataFrame:
    '''
    Generates a Pandas DataFrame from input file.

    Parameters:
    filename : str
        The filename to use to load DataFrame.
    is_random : int
        True: Sample from all nonzero AWC clips.
        False: Sample from top 100 clips by AWC.

    Returns:
    Pandas DataFrame
        A DataFrame of clips by desired sampling method from file data.
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

    if is_random:
        print("Filtering out clips with 0 AWC...")
        data = data[data[data.columns[3]] > 0]
    else:
        print("Getting top 100 clips by AWC...")
        data = data.sort_values(by=data.columns[3], ascending=False)[:100]

    data.insert(3, "SegEnd", data[data.columns[2]] + 30)
    data.columns = ["Index", "Time", "SegStart", "SegEnd", "AWC"]

    os.chdir("..")
    return data


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
