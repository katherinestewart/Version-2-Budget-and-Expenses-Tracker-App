"""This module contains the goals menu. It gets user choice to set
financial goals; by net or gross income, weekly, monthly or annually,
view progress towards financial goals; for gross income, net income or
budget and cancel; return to main menu. It also contains all relevant
functions to get the required returns for each selection.
"""

from user.input import finish_viewing, request_complete, get_menu_selection
from user.interface import clear, goals_menu_heading, goals_sub_heading

GOALS_MENU = f"""{goals_menu_heading("FINANCIAL GOALS")}
\nPlease choose from the following options:
\n1.  Set financial goals
2.  View progress towards financial goals
0.  Return to main menu\
"""


def set_financial_goals():
    """This function"""
    print("Set financial goal here")


def view_goals_progress():
    """This function"""
    print("make some graphs")


def goals_menu():
    """This function gets user selection for the financial goals menu
    and calls relevant functions according to user choice

    :return: None
    """
    while True:
        clear()
        print(GOALS_MENU)
        menu = get_menu_selection(2)

        if menu == 1:
            clear()
            print(goals_sub_heading("Set Financial Goals"))
            set_financial_goals()
            request_complete("Financial goal", "updated")

        elif menu == 2:
            clear()
            print(goals_sub_heading("View Financial Goals Progress"))
            view_goals_progress()
            finish_viewing()

        # Return to main menu
        else:
            break
