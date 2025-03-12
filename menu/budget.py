"""This module contains the budget menu. It gets user selection to set
overall budget; for week, month or year, set budget by category; for
week month or year, view budgets, view budget progress; for week month
or year or return to main menu.
"""

from user.interface import clear, budget_menu_heading, budget_sub_heading
from user.input import get_menu_selection, request_complete, finish_viewing

BUDGET_MENU = f"""{budget_menu_heading("BUDGET")}
\nPlease select from the following options:
\n1.  Set overall budget
2.  Set budget by category
3.  View budgets
4.  View budget progress
0.  Return to main menu\
"""


def set_overall_budget():
    """This function"""
    print("Set overall budget")


def set_budget_by_category():
    """This function"""
    print("Set budget by category")


def view_budgets():
    """This function"""
    print("display budgets here")


def view_budget_progress():
    """This function"""
    print("view budget progress")


def budget_menu():
    """This function"""
    while True:
        clear()
        print(BUDGET_MENU)
        menu = get_menu_selection(4)

        if menu == 1:
            clear()
            print(budget_sub_heading("Set Overall Budget"))
            set_overall_budget()
            request_complete("Overall budget", "updated")

        elif menu == 2:
            clear()
            print(budget_sub_heading("Set budget by Category"))
            set_budget_by_category()
            request_complete("Budget", "updated")

        elif menu == 3:
            clear()
            print(budget_sub_heading("View Budgets"))
            view_budgets()
            finish_viewing()

        elif menu == 4:
            clear()
            print(budget_sub_heading("View Budget Progress"))
            view_budget_progress()
            finish_viewing()

        # Return to main menu
        else:
            break
