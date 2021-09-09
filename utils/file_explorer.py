import os
from config.Columns import Columns
from models.FileSampleInfo import FileSampleInfo


def get_files(sampling_methods: str) -> list:
    '''
    Searches through input directory for all files to process and creates a dictonary
    where the keys are the input filename and the values are the output filename.
    Appends _50snippets to all filenames and all output file extensions are .xlsx.

    Example:
    input_filename.xls >> input_filename_50snippets.xlsx

    Parameters:
    sampling_methods : str
        The desired sampling methods

    Returns:
    List
        List of FileSampleInfo objects
    '''
    files = []

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
        original_filename = split_filename[-2]
        split_filename[-1] = "xlsx"

        if "1" in sampling_methods:
            split_filename[-2] = original_filename + "_50snippets"
            files.append(
                FileSampleInfo(
                    input_filename=file,
                    output_filename='.'.join(split_filename),
                    column_index=Columns.AWC,
                    is_random=False))
        if "2" in sampling_methods:
            split_filename[-2] = original_filename + "_50snippets_random"
            files.append(
                FileSampleInfo(
                    input_filename=file,
                    output_filename='.'.join(split_filename),
                    column_index=Columns.AWC,
                    is_random=True))
        if "3" in sampling_methods:
            split_filename[-2] = original_filename + "_50snippets_tvn"
            files.append(
                FileSampleInfo(
                    input_filename=file,
                    output_filename='.'.join(split_filename),
                    column_index=Columns.TVN,
                    is_random=False))

    os.chdir("..")
    return files
