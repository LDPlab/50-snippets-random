def get_input_file_name() -> str:
    supported_extentions = ["xls", "xlsx", "csv"]
    filename = get_filename("Input")

    if filename.split('.')[-1] not in supported_extentions:
        filename += ".xls"

    return filename


def get_output_file_name() -> str:
    supported_extentions = ["xlsx", "csv"]
    filename = get_filename("Output")

    if filename.split('.')[-1] not in supported_extentions:
        filename += ".csv"

    return filename

def get_filename(direction: str) -> str:
    filename = input(f"{direction} filename: ")

    while len(filename) == 0:
        filename = input(f"{direction} filename: ")

    return filename
