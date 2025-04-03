"""This module contains logic to validate user input."""

from time import sleep
from maths.dates import (get_first_of_month, get_one_year_ago,
                         get_six_months_ago, get_three_months_ago)

ENTER = "\nEnter your selection: "
INVALID_INPUT = "You entered an invalid input. Please try again."
SELECT_DATE_RANGE = """\n\U0001f5d3  \
Please choose from the following time periods:\n
1.  This month
2.  Past 3 months
3.  Past 6 months
4.  Past year
5.  All history
0.  Cancel\
"""


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


def get_term(number_selection):
    """This function returns a term from a user choice

    :param string: 1, 2 or 3
    :return: 'weekly', 'monthly', 'annual' or None
    :rtype: str or None
    """
    term_dict = {
        1: "weekly",
        2: "monthly",
        3: "annual"
    }

    return term_dict[number_selection]


def get_amount():
    """This function gets an amount from the user

    :return: new amount
    :rtype: str
    """
    while True:
        new_amount = input("\nEnter amount: ").strip()

        if amount_check(new_amount):
            return new_amount

        print(INVALID_INPUT)


def amount_check(new_amount):
    """This function checks that a user input is valid for a monetary
    amount.

    :param new_amount: amount entered by user
    :return: True if valid or False if invalid
    :rtype: bool
    """
    try:
        amount = float(new_amount)
        pounds, pence = str(amount).split(".")
        if len(pence) <= 2 and pounds[0] != "-":
            return True
        return False
    except ValueError:
        return False


def get_description(thing):
    """This function gets a description
    """
    while True:
        description = input(f"\nEnter {thing} description: ").strip()

        if description_check(description):
            return description


def description_check(description):
    """Checks validity of user input
    """
    if description == "":
        print("You didn't enter anything.")
        return False
    if len(description) > 20:
        print("You entered too many characters.")
        return False

    return True


def select_date_range():
    """This function 
    """
    print(SELECT_DATE_RANGE)
    date_range = get_menu_selection(5)
    return date_range


def get_start_date(date_range):
    """This function.
    """
    start = None

    if date_range == 1:
        start = get_first_of_month()
    if date_range == 2:
        start = get_three_months_ago()
    if date_range == 3:
        start = get_six_months_ago()
    if date_range == 4:
        start = get_one_year_ago()

    return start
