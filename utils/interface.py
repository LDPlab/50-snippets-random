from config.Columns import Columns
from utils.data_tool import get_data, write_output
from utils.randomizer import get_50_random_snippets
from utils.file_explorer import get_files
from utils.sampling_menu import get_user_sampling


def interface():
    '''
    Main program for randomly sampling 50  clips.
    Controls execution flow for processing files and attempts to handle execution errors.
    '''
    print("Please ensure that the input files are in a folder labeled \"input\"")
    print("Supported input extensions: .xls, .xlsx, .csv | Default to .xls")
    print("Output extensions: .xlsx")

    sampling_methods = get_user_sampling()
    files = get_files(sampling_methods)

    for file_info in files:
        print(f"\nProcessing {file_info.input_filename}...")
        try:
            data = get_data(file_info)
        except ValueError:
            print(f"File extension for {file_info.input_filename} is not supported")
            continue

        sampled_data = get_50_random_snippets(data, file_info.column_index == Columns.TVN)

        print(f"Was able to select {len(sampled_data)} snippets")
        if len(sampled_data) < 50 and not file_info.is_random:
            print("Expanding sample size to top 200 clips")
            expanded_data = get_data(file_info, 200)
            sampled_data = get_50_random_snippets(expanded_data, file_info.column_index == Columns.TVN)
            print(f"Was able to select {len(sampled_data)} snippets")

        print(f"Writing {file_info.output_filename} file...")
        write_output(sampled_data, file_info.output_filename)
        print(f"Output file {file_info.output_filename} has been generated")

    print("\nAll files processed.")
