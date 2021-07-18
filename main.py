from utils.user_input import get_file_name

def main():
    print("Please ensure that the input file is in the folder with this executable.")
    print("When entering filenames .xls file type is assumed,")
    print("if a different filetype is preferred include the file extension in file name")
    print("ex SAMPLE_INPUT_FILE.csv")
    print("Supported extensions: .xls, .xlsx, .csv")

    input_filename = get_file_name("input")
    output_filename = get_file_name("output")

    print(input_filename, output_filename)

if __name__ == "__main__":
    main()
