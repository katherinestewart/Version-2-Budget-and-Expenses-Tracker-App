"""This module contains the expenses menu. It gets user choice to add
expense, view expenses by category; over a selected term, manage
categories or return to main menu. It also contains all relevant
functions to get the required returns for each selection.
"""

from menu.sub_menu.categories import categories_menu, view_categories
from managers.expenses_manager import get_new_expense, print_expenses, get_expenses_this_month
from user.input import (get_menu_selection, request_complete, finish_viewing,
                        select_date_range)
from user.interface import (expenses_menu_heading, expenses_sub_heading,
                            clear)

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
    expense = get_new_expense()
    expense.insert_expense()
    clear()
    print_expenses([expense])


def view_expenses():
    """This function displays expenses in a specified date range.
    """
    date_range = select_date_range()
    if date_range == 0:
        pass
    else:
        if date_range == 1:
            expenses_list = get_expenses_this_month()
            clear()
            print_expenses(expenses_list)
            finish_viewing()


def view_expenses_by_category():
    """This function displays expenses from a specified category in a
    specified date range."""
    print("Please choose a category.")
    view_categories()
    #number_of_categories =
    get_menu_selection(5)
    date_range = select_date_range()
    if date_range == 0:
        pass
    else:
        #get_expenses_in_date_range()
        finish_viewing()


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
