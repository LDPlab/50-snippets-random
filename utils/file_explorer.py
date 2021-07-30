import os


def get_files(sampling_method: int) -> dict:
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
        split_filename[-1] = "xlsx"

        if sampling_method == 1 or sampling_method == 3:
            split_filename[-2] += "_50snippets"
            files_map['.'.join(split_filename)] = file
        elif sampling_method == 2:
            split_filename[-2] += "_50snippets_random"
            files_map['.'.join(split_filename)] = file
        if sampling_method == 3:
            split_filename[-2] += "_random"
            files_map['.'.join(split_filename)] = file


    os.chdir("..")
    return files_map
