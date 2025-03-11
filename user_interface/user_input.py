"""This module contains logic to validate user input."""

from time import sleep

ENTER = "\nEnter your selection: "
INVALID_INPUT = "You entered an invalid input. Please try again."


def request_complete(thing, done):
    """This function"""
    sleep(0.6)
    print(f"\n{thing} has been {done} \U00002705")
    finish_viewing()


def finish_viewing():
    """This function gets user input once they have finished viewing
    printed information.

    :return: None
    """
    sleep(0.6)
    input("\nPress enter to return to previous menu: ")


def get_menu_selection(number_of_options):
    """This function checks validity of user input for expenses menu

    :return: True if valid or False if invalid
    :rtype: bool
    """
    while True:
        menu_choice = input(ENTER).strip().replace(".", "")
        try:
            menu_choice = int(menu_choice)
            if menu_choice in range(number_of_options + 1):
                return menu_choice
            print(INVALID_INPUT)
        except ValueError:
            print(INVALID_INPUT)
