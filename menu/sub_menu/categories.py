"""This module contains the categories menu."""

from user_interface.display import expenses_sub_heading, clear
from user_interface.user_input import (get_menu_selection, finish_viewing,
                                       request_complete)

CATEGORIES_MENU = f"""{expenses_sub_heading("Manage Categories")}
\nPlease choose from the following options:
\n1.  View categories
2.  Edit category
3.  Add category
0.  Return to expenses menu\
"""

def view_categories():
    """This function prints categories to user.
    """
    print("Logic here to print categories.")


def edit_category():
    """This function"""
    print("Logic here to edit categories.")


def add_category():
    """This function adds a category to the database."""
    print("Print category that has been added")


def categories_menu():
    """This function presents the user with options to manage expense
    categories and calls relevant functions according to user selection

    :return: None
    """
    while True:
        clear()
        print(CATEGORIES_MENU)
        menu = get_menu_selection(3)

        # ****** View categories ******
        if menu == 1:
            clear()
            print(expenses_sub_heading("View Categories"))
            view_categories()
            finish_viewing()

        # ****** Edit category ******
        elif menu == 2:
            clear()
            print(expenses_sub_heading("Edit Categories"))
            edit_category()
            request_complete("Category", "updated")

        # ****** Add category ******
        elif menu == 3:
            clear()
            print(expenses_sub_heading("Add Category"))
            add_category()
            request_complete("Category", "added")

        # ****** Return to Expenses Menu ******
        else:
            break
