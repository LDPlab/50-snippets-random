import pandas as pd
import os
from models.FileSampleInfo import FileSampleInfo
from config.Columns import Columns


def read_file(filename: str):
    '''
    Reads csv or excel files, throws error if not correct file type.

    Parameters:
    filename : str
        The filename to use to load DataFrame.

    Returns:
    Pandas DataFrame
        Loaded dataframe from file.
    '''
    os.chdir("input")
    if filename.endswith(".csv"):
        data = pd.read_csv(filename)
    elif filename.endswith(".xls") or filename.endswith(".xlsx"):
        data = pd.read_excel(filename)
    else:
        os.chdir("..")
        raise ValueError("File extension not supported")
    os.chdir("..")
    return data


def get_data(file_info: FileSampleInfo) -> pd.DataFrame:
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
    data = read_file(file_info.input_filename)

    if file_info.column_index == Columns.AWC:
        if file_info.is_random:
            print("Filtering out snippets with 0 AWC...")
            data = data[data[data.columns[Columns.AWC.value]] > 0]
        else:
            print("Getting top 100 snippets by AWC...")
            data = data.sort_values(by=data.columns[Columns.AWC.value], ascending=False)[:100]

        for col in data.columns[4:]:
            del data[col]
    elif file_info.column_index == Columns.TVN:
        print("Getting top 100 snippets by TVN...")
        data = data.sort_values(by=data.columns[Columns.TVN.value], ascending=False)[:100]

        for col in data.columns[3:-1]:
            del data[col]

    data.insert(3, "SegEnd", data[data.columns[Columns.SEGMENT_START.value]] + 30)
    data.columns = ["Index", "Time", "SegStart", "SegEnd", file_info.column_index.name]
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
