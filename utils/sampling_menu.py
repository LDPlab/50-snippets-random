def get_user_sampling() -> int:
    """
    Display the sampling menu to terminal, and get user choice.

    Returns
    str
        The sampling selection from user.
    """
    print("\nSelect desired sampling method:")
    print("1 Top 100 clips by AWC")
    print("2 All non zero AWC clips")
    print("3 Top 100 clips by TVN")
    sampling_method = input("Please enter desired sampling: ")

    while "1" not in sampling_method and "2" not in sampling_method and "3" not in sampling_method:
        print("Invalid selection.")
        print("\nSelect desired sampling method:")
        print("1 Top 100 clips by AWC")
        print("2 All non zero AWC clips")
        print("3 Top 100 clips by TVN")
        sampling_method = input("Please enter desired sampling: ")

    return sampling_method