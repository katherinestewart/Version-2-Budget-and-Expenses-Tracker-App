"""This module contains the categories menu."""

from user.interface import expenses_sub_heading, clear
from user.input import (get_menu_selection, finish_viewing, request_complete,
                        get_description)
from managers.category_manager import CategoryManager as CM

CATEGORIES_MENU = f"""{expenses_sub_heading("Manage Categories")}
\nPlease choose from the following options:
\n1.  View categories
2.  Edit category
3.  Add category
0.  Return to expenses menu\
"""


def view_categories():
    """This"""
    CM().print_categories()


def edit_category():
    """This function"""
    category = CM().select_category()
    update = get_description("category")
    category.update_category(update)


def add_category():
    """This function adds a category to the database."""
    category = get_description("category")
    CM(ca=category).insert_category()


def category_menu():
    """This function presents the user with options to manage expense
    categories and calls relevant functions according to user selection

    :return: None
    """
    while True:
        clear()
        print(CATEGORIES_MENU)
        menu = get_menu_selection(3)

        if menu == 1:
            clear()
            print(expenses_sub_heading("View Categories"))
            view_categories()
            finish_viewing()

        elif menu == 2:
            clear()
            print(expenses_sub_heading("Edit Categories"))
            edit_category()
            clear()
            view_categories()
            request_complete("Category", "updated")

        elif menu == 3:
            clear()
            print(expenses_sub_heading("Add Category"))
            add_category()
            view_categories()
            request_complete("Category", "added")

        # ****** Return to Expenses Menu ******
        else:
            break
