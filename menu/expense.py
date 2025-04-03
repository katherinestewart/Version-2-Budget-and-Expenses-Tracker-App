"""This module contains the expenses menu. It gets user choice to add
expense, view expenses by category; over a selected term, manage
categories or return to main menu. It also contains all relevant
functions to get the required returns for each selection.
"""

from datetime import date
from user.input import (get_menu_selection, request_complete, finish_viewing,
                        select_date_range, get_start_date)
from user.interface import (expenses_menu_heading, expenses_sub_heading,
                            clear)
from menu.sub_menu.category import category_menu
from managers.expense_manager import (ExpenseManager as EM, print_expenses,
                                      get_objects_from_rows, fetch_all_rows,
                                      fetch_rows_by_date, fetch_rows_by_date_cat,
                                      fetch_rows_by_cat)
from managers.category_manager import CategoryManager as CM

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
    expense = EM(da=date.today().strftime("%Y-%m-%d")).get_new_expense()
    expense.insert_expense()
    clear()
    print_expenses([expense])


def view_expenses():
    """This function displays expenses in a specified date range.
    """
    start = None
    expenses_list = []
    date_range = select_date_range()

    if date_range == 0:
        pass

    else:
        if date_range == 5:
            rows = fetch_all_rows()
        else:
            start = get_start_date(date_range)
            rows = fetch_rows_by_date(start)

        expenses_list = get_objects_from_rows(rows)

        clear()
        print_expenses(expenses_list)
        finish_viewing()


def view_expenses_by_category():
    """This function displays expenses from a specified category in a
    specified date range."""
    category = CM().select_category()
    date_range = select_date_range()

    if date_range == 0:
        pass
    else:
        if date_range == 5:
            rows = fetch_rows_by_cat(category.id_)
        else:
            start = get_start_date(date_range)
            rows = fetch_rows_by_date_cat(start, category.id_)
        expenses_list = get_objects_from_rows(rows)

        clear()
        print_expenses(expenses_list)
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

        elif menu == 4:
            category_menu()

        # Return to main menu
        else:
            break
