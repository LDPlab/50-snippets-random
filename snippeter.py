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

    sampling_method = get_user_sampling()
    files = get_files(sampling_method)


    for [output_file, input_file] in files.items():
        print(f"\nProcessing {input_file}...")
        try:
            is_random_sampling = "_50snippets_random" in output_file
            processed_data = get_data(input_file, is_random_sampling)
        except ValueError:
            print(f"File extension for {input_file} is not supported")
            print("Please rerun the program and provide a valid extension (.xls, .xlsx, .csv)")
            continue

        randomized_data = get_50_random_snippets(processed_data)

        print(f"Writing {output_file} file...")
        write_output(randomized_data, output_file)
        print(f"Output file {output_file} has been generated")

    print("\nAll files processed.")
    input("Press any key to exit...")


if __name__ == "__main__":
    main()
