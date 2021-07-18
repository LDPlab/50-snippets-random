from utils.data_tool import get_data, write_output
from utils.randomizer import get_50_random_snippets
from utils.user_input import get_input_file_name, get_output_file_name

def main():
    print("Please ensure that the input file is in the folder with this executable.")
    print("When entering filenames .xls file type is assumed,")
    print("if a different filetype is preferred include the file extension in file name")
    print("ex SAMPLE_INPUT_FILE.csv")
    print("Supported input extensions: .xls, .xlsx, .csv")
    print("Supported output extensions: .xlsx, .csv")
    print()

    input_filename = get_input_file_name()
    output_filename = get_output_file_name()
    print()

    try:
        processed_data = get_data(input_filename)
    except ValueError:
        print(f"File extension for {input_filename} is not supported.")
        print("Please rerun the program and provide a valid extension (.xls, .xlsx, .csv).")
        input("Press enter to close window.")
        exit(1)
    except FileNotFoundError:
        print(f"File {input_filename} could not be found in directory.")
        print("Please ensure filename is correct and in the same folder as the executable, then rerun program.")
        input("Press enter to close window.")
        exit(1)

    randomized_data = get_50_random_snippets(processed_data)
    write_output(randomized_data, output_filename)

if __name__ == "__main__":
    main()
