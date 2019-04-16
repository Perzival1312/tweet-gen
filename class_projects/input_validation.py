# TODO original.replace(' ','').isalpha()
def single_letter(input_string):
    valid_input = False
    while not valid_input:
        try:
            testing_input = input(input_string)
            if not testing_input.isalpha():
                print("Only letters, please try again!")
            elif len(testing_input) != 1:
                print("Must be a singular letter, please try again!")
            else:
                valid_input = True
                return testing_input
        except EOFError:
            print("Not a letter! Try again.")
            continue


def single_number(input_string):
    valid_input = False
    while not valid_input:
        try:
            testing_input = input(input_string)
            if not testing_input.isnumeric():
                print("Only numbers, please try again!")
            elif len(testing_input) != 1:
                print("Must be a singular number, please try again!")
            else:
                valid_input = True
                return testing_input
        except EOFError:
            print("Not a number! Try again.")
            continue


def multi_letter(input_string, length=32):
    valid_input = False
    while not valid_input:
        try:
            testing_input = input(input_string)
            if not testing_input.replace(" ", "").isalpha():
                print("That is not a letter, please try again!")
            elif len(testing_input) >= length:
                print(
                    "Must be less than "
                    + str(length)
                    + " characters long, please try again!"
                )
            else:
                valid_input = True
                return testing_input
        except EOFError:
            print("Not a letter! Try again.")
            continue


def multi_number(input_string, length=32):
    valid_input = False
    while not valid_input:
        try:
            testing_input = input(input_string)
            if not testing_input.isnumeric():
                print("That is not a number, please try again!")
            elif len(testing_input) >= length:
                print(
                    "Must be less than "
                    + str(length)
                    + " characters long, please try again!"
                )
            else:
                valid_input = True
                return testing_input
        except EOFError:
            print("Not a number! Try again.")
            continue


# TODO get this module working!!!
def continuation(input_string):
    valid_input = False
    while not valid_input:
        try:
            testing_input = input(input_string)
            if not testing_input.isalpha():
                print("That is not a letter, please try again!")
            elif len(testing_input) != 1:
                print("Must be a singular letter, please try again!")
            elif testing_input.lower() != "n" and testing_input.lower() != "y":
                print("Must be Y or N")
            else:
                valid_input = True
        except EOFError:
            print("Not a letter! Try again.")
            continue
    if testing_input.lower() == "y":
        return True
    else:
        return False
