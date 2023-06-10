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
    filepath = f"input/{filename}"
    if filename.endswith(".csv"):
        data = pd.read_csv(filepath)
    elif filename.endswith(".xls") or filename.endswith(".xlsx"):
        data = pd.read_excel(filepath)
    else:
        raise ValueError("File extension not supported")

    return data


def get_data(file_info: FileSampleInfo) -> pd.DataFrame:
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

    if file_info.is_random and file_info.column_index is not None:
        data = data[data[data.columns[file_info.column_index.value]] > 0]
    elif file_info.column_index is not None:
        data = data.sort_values(by=data.columns[file_info.column_index.value], ascending=False)

    data.insert(2, "SegEnd", data[data.columns[Columns.SEGMENT_START.value]] + 30)
    data.columns = ["Index", "SegStart", "SegEnd", "AWC", "CTC", "CVC", "FAN", "MAN", "TVN"]
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
    data.to_excel(f"output/{filename}", index=False)
