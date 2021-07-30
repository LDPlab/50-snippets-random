def get_user_sampling() -> int:
    """
    Display the sampling menu to terminal, and get user choice.

    Returns
    int
        The sampling selection from user. (1, 2, or 3)
    """
    print("\nSelect desired sampling method:")
    print("1 Top 100 clips by AWC")
    print("2 All non zero AWC clips")
    print("3 Both")
    sampling_method = input("Please enter 1, 2, or 3: ")

    while sampling_method not in ["1", "2", "3"]:
        print("Invalid selection.")
        print("\nSelect desired sampling method:")
        print("1 Top 100 clips by AWC")
        print("2 All non zero AWC clips")
        print("3 Both")
        sampling_method = input("Please enter 1, 2, or 3: ")

    return int(sampling_method)
