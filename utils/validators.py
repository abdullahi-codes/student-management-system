def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))

            if min_val is not None and value < min_val:
                print(f"Must be >= {min_val}")
                continue

            if max_val is not None and value > max_val:
                print(f"Must be <= {max_val}")
                continue

            return value

        except ValueError:
            print("Please enter a valid number")


def get_float(prompt, min_val=0.0, max_val=4.0):
    while True:
        try:
            value = float(input(prompt))

            if value < min_val or value > max_val:
                print(f"Must be between {min_val} and {max_val}")
                continue

            return value

        except ValueError:
            print("Please enter a valid decimal number")