import os


def get_files() -> dict:
    '''
    Searches through input directory for all files to process and creates a dictonary
    where the keys are the input filename and the values are the output filename.
    Appends _50snippets to all filenames and all output file extensions are .xlsx.

    Example:
    input_filename.xls >> input_filename_50snippets.xlsx

    Returns
    Dictionary
        Dictionary of input filenames to process to output filenames to write.
    '''
    files_map = {}

    if not os.path.isdir("output"):
        os.mkdir("output")
    if not os.path.isdir("input"):
        print("\nCreating input folder, please place input files in and run again.")
        os.mkdir("input")
        input("Press any key to exit...")
        exit(0)

    os.chdir("input")
    for file in os.listdir():
        split_filename = file.split('.')
        split_filename[-2] += "_50snippets"
        split_filename[-1] = "xlsx"
        files_map[file] = '.'.join(split_filename)

    os.chdir("..")
    return files_map
