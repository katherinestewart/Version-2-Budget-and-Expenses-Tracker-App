"""This module"""

from user.interface import clear, income_sub_heading
from user.input import get_menu_selection, finish_viewing, request_complete

SOURCES_MENU = f"""{income_sub_heading("Sources")}
\nPlease choose from the following options:
\n1.  View sources of income
2.  Edit income source
3.  Add new income source
0.  Return to income menu\
"""


def view_sources():
    """This function prints income sources to user.
    """
    print(income_sub_heading("View Income Sources"))
    print("Logic here to print sources.")
    finish_viewing()


def edit_source():
    """This function"""
    print(income_sub_heading("Edit Income Sources"))
    print("Logic here to edit income sources.")
    request_complete("Income source", "updated")


def add_source():
    """This function adds a income source to the database."""
    print(income_sub_heading("Add Source"))
    print("Print source that has been added")
    request_complete("Source", "added")


def source_menu():
    """This function manages user selection for income sources and
    calls relevant functions according to this selection

    :return: None
    """
    while True:
        clear()
        print(SOURCES_MENU)
        menu = get_menu_selection(3)

        # View sources of income
        if menu == 1:
            clear()
            view_sources()

        # Edit income source
        elif menu == 2:
            clear()
            edit_source()

        # Add new income source
        elif menu == 3:
            clear()
            add_source()

        # Return to income menu
        else:
            break
