"""This module"""

from user.interface import clear, income_sub_heading
from user.input import (get_menu_selection, finish_viewing, request_complete,
                        get_description)
from managers.source_manager import SourceManager as SM

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
    SM().print_sources()


def edit_source():
    """This function"""
    source = SM().select_source()
    update = get_description("source")
    source.update_source(update)


def add_source():
    """This function adds a income source to the database."""
    source = get_description("source")
    SM(so=source).insert_source()


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
            print(income_sub_heading("View Income Sources"))
            view_sources()
            finish_viewing()

        # Edit income source
        elif menu == 2:
            clear()
            print(income_sub_heading("Edit Income Sources"))
            edit_source()
            clear()
            view_sources()
            request_complete("Income source", "updated")

        # Add new income source
        elif menu == 3:
            clear()
            print(income_sub_heading("Add Source"))
            add_source()
            clear()
            view_sources()
            request_complete("Source", "added")

        # Return to income menu
        else:
            break
