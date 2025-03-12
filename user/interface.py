"""This module contains functions which format strings for printing or
effect the user interface."""

import os

START = "\033[1m -------- \033[0m\033[1m"
END = "\033[1m --------\033[0m"
SUB_EMOJI = "\U00002714"
SUB_START = "\033[1m --- \033[0m\033[1m"
SUB_END  = "\033[1m ---\033[0m"


def clear():
    """Clears terminal

    :return: None
    """
    os.system("cls||clear")


def expenses_menu_heading(title):
    """This function constructs the heading for options selected from
    the main menu: Expenses, Income, Budget and Financial Goals.

    :return: menu heading
    :rtype: str
    """
    return f"\U0001f4b8\033[31m{START}{title}\033[31m{END}"


def income_menu_heading(title):
    """This function constructs the heading for options selected from
    the main menu: Expenses, Income, Budget and Financial Goals.

    :return: menu heading
    :rtype: str
    """
    return f"\U0001f4b7\033[32m{START}{title}\033[32m{END}"


def budget_menu_heading(title):
    """This function constructs the heading for options selected from
    a sub menu: Manage Categories.

    :return: menu heading
    :rtype: str
    """
    return f"\U0001fa99\033[33m{START}{title}\033[33m{END}"


def goals_menu_heading(title):
    """This function constructs the heading for options selected from
    a sub menu: Manage Categories.

    :return: menu heading
    :rtype: str
    """
    return f"\U0001f90c\033[34m{START}{title}\033[34m{END}"


def expenses_sub_heading(title):
    """This function constructs the heading for options selected from
    a sub menu: Manage Categories.

    :return: menu heading
    :rtype: str
    """
    return f"{SUB_EMOJI}\033[31m{SUB_START}{title}\033[31m{SUB_END}"


def income_sub_heading(title):
    """This function constructs the heading for options selected from
    a sub menu: Manage Categories.

    :return: menu heading
    :rtype: str
    """
    return f"{SUB_EMOJI}\033[32m{SUB_START}{title}\033[32m{SUB_END}"


def budget_sub_heading(title):
    """This function constructs the heading for options selected from
    a sub menu: Manage Categories.

    :return: menu heading
    :rtype: str
    """
    return f"{SUB_EMOJI}\033[33m{SUB_START}{title}\033[33m{SUB_END}"


def goals_sub_heading(title):
    """This function constructs the heading for options selected from
    a sub menu: Manage Categories.

    :return: menu heading
    :rtype: str
    """
    return f"{SUB_EMOJI}\033[34m{SUB_START}{title}\033[34m{SUB_END}"


def money_format(some_amount):
    """This function convert an amount of money into a string with £
    sign and 2 decimal places.

    :return: amount with £ and 2 dp
    :rtype: str
    """
    if len(str(some_amount)) == 1:
        some_amount = str(some_amount) + ".00"
    if str(some_amount)[-1] == ".":
        some_amount = str(some_amount) + "00"
    if len(str(some_amount)) > 1:
        if str(some_amount)[-2] == ".":
            some_amount = str(some_amount) + "0"

    some_amount = "£" + str(some_amount)
    return some_amount
