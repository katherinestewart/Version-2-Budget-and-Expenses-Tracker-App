"""This module is the main menu. It gets the user choice for expenses,
income, budget, financial goals or to exit the programme.
"""

from time import sleep
from database import database_commands as dc
from user.interface import clear
from user.input import get_menu_selection
from menu.expense import expenses_menu
from menu.income import income_menu
from menu.budget import budget_menu
from menu.goals import goals_menu

INVALID_INPUT = "\nYou entered an invalid input.  Please try again."
MAIN_MENU = """\U0001f3e0 \033[1m\033[96m============ \033[0m\033[1m\
MAIN MENU\033[36m ============\033[0m
\nPlease choose from the following options:
\n1.  Expenses
2.  Income
3.  Budget
4.  Financial Goals
0.  Quit\
"""
WELCOME = "Welcome to the Expenses and Budget Tracker App! \U0001f4b0"


def display_message(message):
    """This function displays welcome and goodbye messages with a time
    delay

    :param message: welcome or goodbye message for user
    :return: None
    """
    x = ""
    for char in message:
        x += char
        print(x)
        sleep(0.04)
        clear()


def main_menu():
    """Gets the user selection from the main menu and calls relevant
    module from selection

    :return: None
    """
    dc.create_tables()

    display_message(WELCOME)

    # ********* Menu Selection *********
    while True:
        clear()
        print(MAIN_MENU)
        menu = get_menu_selection(4)

        # ****** Expenses ******
        if menu == 1:
            expenses_menu()

        # ****** Income ******
        elif menu == 2:
            clear()
            income_menu()

        # ****** Budget ******
        elif menu == 3:
            clear()
            budget_menu()

        # ****** Financial Goals ******
        elif menu == 4:
            clear()
            goals_menu()

        # ****** Exit ******
        elif menu == 0:
            clear()
            display_message("\nSee you next time! \U0001f44b\n")

            # Final break point to close the programme naturally
            break

        else:
            print(INVALID_INPUT)
