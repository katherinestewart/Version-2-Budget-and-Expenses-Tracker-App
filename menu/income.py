"""This module contains the income menu. It gets user choice to add
income, view income, manage income sources; view sources of income,
edit income source, add new income source, or return to main menu. It
also contains all relevant functions to get the required returns for
each selection.
"""

from menu.sub_menu.source import source_menu
from user.input import get_menu_selection, request_complete, finish_viewing
from user.interface import clear, income_menu_heading, income_sub_heading

INCOME_MENU = f"""{income_menu_heading("INCOME")}
\nPlease choose from the following options:
\n1.  Add income
2.  View income
3.  View income by source
4.  Manage income sources
0.  Return to main menu\
"""


def add_income():
    """This function adds an income to the database."""
    print("Print income that has been added")


def view_income():
    """This function displays income in a specified date range.
    """
    print("Logic here to select date and print income.")


def view_income_by_source():
    """This function displays income from a specified source in a
    specified date range."""
    print("Logic here to select source and date and print expenses.")


def income_menu():
    """This function gets user input for the income menu and calls
    relevant functions according to this selection

    :return: None
    """
    while True:
        clear()
        print(INCOME_MENU)
        menu = get_menu_selection(4)

        if menu == 1:
            clear()
            print(income_sub_heading("Add Income"))
            add_income()
            request_complete("Income", "added")

        elif menu == 2:
            clear()
            print(income_sub_heading("View Income"))
            view_income()
            finish_viewing()

        elif menu == 3:
            clear()
            print(income_sub_heading("View Income by Source"))
            view_income_by_source()
            finish_viewing()

        elif menu == 4:
            clear()
            source_menu()

        # Return to main menu
        else:
            break
