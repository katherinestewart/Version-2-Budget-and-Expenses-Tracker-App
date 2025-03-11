"""This module contains the expenses menu. It gets user choice to add
expense, view expenses by category; over a selected term, manage
categories or return to main menu. It also contains all relevant
functions to get the required returns for each selection.
"""

from menu.sub_menu.categories import categories_menu
from user_interface.user_input import (get_menu_selection, request_complete,
                                       finish_viewing)
from user_interface.display import (expenses_menu_heading,
                                    expenses_sub_heading, clear)

EXPENSES_MENU = f"""{expenses_menu_heading("EXPENSES")}
\nPlease choose from the following options:
\n1.  Add expense
2.  View expenses
3.  View expenses by category
4.  Manage categories
0.  Return to main menu\
"""

def add_expense():
    """This function adds an expense to the database."""
    print("Print expense that has been added")


def view_expenses():
    """This function displays expenses in a specified date range.
    """
    print("Logic here to select date and print expenses.")


def view_expenses_by_category():
    """This function displays expenses from a specified category in a
    specified date range."""
    print("Logic here to select category and date and print expenses.")


def expenses_menu():
    """This function manages the user selection from the expense menu
    calls the relevant functions according to the menu selection

    :return: None
    """

    while True:
        clear()
        print(EXPENSES_MENU)
        menu = get_menu_selection(4)

        if menu == 1:
            clear()
            print(expenses_sub_heading("Add Expense"))
            add_expense()
            request_complete("Expense", "added")

        elif menu == 2:
            clear()
            print(expenses_sub_heading("View Expenses"))
            view_expenses()
            finish_viewing()

        elif menu == 3:
            clear()
            print(expenses_sub_heading("View Expenses by Category"))
            view_expenses_by_category()
            finish_viewing()

        elif menu == 4:
            categories_menu()

        # Return to main menu
        else:
            break
