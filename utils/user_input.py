def get_file_name(direction: str) -> str:
    filename = input(f"{direction.capitalize()} filename: ")

    while len(filename) == 0:
        filename = input(f"{direction.capitalize()} filename: ")

    return validate_filename(filename)


def validate_filename(filename: str) -> str:
    supported_extentions = ["xls", "xlsx", "csv"]

    if filename.split('.')[-1] not in supported_extentions:
        filename += ".xls"

    return filename
