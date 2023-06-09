from config.sample_options import sample_options
from models.SampleOption import SampleOption

def get_user_sampling() -> list[SampleOption]:
    """
    Display the sampling menu to terminal, and get user choice.

    Returns
    str
        The sampling selection from user.
    """
    print_menu()
    sampling_methods = input("Please enter desired sampling: ")

    while not check_contains_valid_selection(sampling_methods):
        print("Invalid selection.")
        print_menu()
        sampling_methods = input("Please enter desired sampling: ")

    return process_options(sampling_methods)

def print_menu():
    """Helper for printing the option menu"""
    print("\nSelect desired sampling methods:")
    for key, value in sample_options.items():
        print(f"{key} - {value.name}")

def check_contains_valid_selection(sampling_methods: str) -> bool:
    """Helper for determining if a valid selction has been added"""
    for option in sample_options.keys():
        if option in sampling_methods:
            return True
    return False

def process_options(sampling_methods: str) -> list[SampleOption]:
    """Get the options that a user has entered"""
    options = []

    for option in sample_options.values():
        if option.key in sampling_methods:
            options.append(option)

    return options
