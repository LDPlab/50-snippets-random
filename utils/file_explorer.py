import os


def get_files() -> dict:
    files_map = {}

    if not os.path.isdir("output"):
        os.mkdir("output")
    if not os.path.isdir("input"):
        print("Creating input folder, please place input files in and run again.")
        os.mkdir("input")
        input("Press any key to exit...")
        exit(0)

    os.chdir("input")
    for file in os.listdir():
        split_filename = file.split('.')
        split_filename[-2] += "_50_snippets"
        split_filename[-1] = "xlsx"
        files_map[file] = '.'.join(split_filename)

    os.chdir("..")
    return files_map
