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


def get_data(file_info: FileSampleInfo, top_limit = 100) -> pd.DataFrame:
    '''
    Generates a Pandas DataFrame from input file.

    Parameters:
    filename : str
        The filename to use to load DataFrame.
    top_limit : int
        The top number of clips to select for given column.

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
            print(f"Getting top {top_limit} snippets by AWC...")
            data = data.sort_values(by=data.columns[Columns.AWC.value], ascending=False)[:top_limit]

        for col in data.columns[4:]:
            del data[col]
    elif file_info.column_index == Columns.TVN:
        print(f"Getting top {top_limit} snippets by TVN...")
        data = data.sort_values(by=data.columns[Columns.TVN.value], ascending=False)[:top_limit]

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
