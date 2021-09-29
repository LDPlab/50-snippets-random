from config.Columns import Columns
from utils.data_tool import get_data, write_output
from utils.randomizer import get_50_random_snippets
from utils.file_explorer import get_files
from utils.sampling_menu import get_user_sampling


def main():
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
            processed_data = get_data(file_info)
        except ValueError:
            print(f"File extension for {file_info.input_filename} is not supported")
            continue

        randomized_data = get_50_random_snippets(processed_data, file_info.column_index == Columns.TVN)

        print(f"Writing {file_info.output_filename} file...")
        write_output(randomized_data, file_info.output_filename)
        print(f"Output file {file_info.output_filename} has been generated")

    print("\nAll files processed.")
    input("Press any key to exit...")


if __name__ == "__main__":
    main()
