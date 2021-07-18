import pandas as pd
import os


def get_data(filename: str) -> pd.DataFrame:
    os.chdir("input")
    if filename[-4:] == ".csv":
        data = pd.read_csv(filename)
    elif filename[-4:] == ".xls" or filename[-5:] == ".xlsx":
        data = pd.read_excel(filename)
    else:
        raise ValueError("File extension not supported")

    for col in data.columns[4:]:
        del data[col]

    non_zero_awc_data = data[data[data.columns[3]] > 0]
    non_zero_awc_data.insert(3, "SegEnd", data[data.columns[2]] + 30)
    non_zero_awc_data.columns = ["Index", "Time", "SegStart", "SegEnd", "AWC"]

    os.chdir("..")
    return non_zero_awc_data


def write_output(data: pd.DataFrame, filename: str):
    os.chdir("output")
    data.to_excel(filename, index=False)
    os.chdir("..")
