import os
from config.Columns import Columns
from models.FileSampleInfo import FileSampleInfo
from models.SampleOption import SampleOption


def get_files(sampling_methods: list[SampleOption]) -> list[FileSampleInfo]:
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

    for file in os.listdir("input"):
        split_filename = file.split('.')
        original_filename = split_filename[-2]
        split_filename[-1] = "xlsx"

        for method in sampling_methods:
            split_filename[-2] = original_filename + method.file_modifier
            files.append(
                FileSampleInfo(
                    input_filename=file,
                    output_filename='.'.join(split_filename),
                    column_index=method.column,
                    time_filter_in_seconds=method.time_filter_in_seconds,
                    count=method.count,
                    is_random=method.is_random))

    return files
