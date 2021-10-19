from utils.interface import interface
import traceback


def main():
    '''
    Main program for randomly sampling 50 clips.
    Controls execution flow for processing files and attempts to handle execution errors.
    '''
    try:
        interface()
    except:
        print("\nSomething went wrong. Details:")
        print(traceback.format_exc())

    input("Press any key to exit...")


if __name__ == "__main__":
    main()
