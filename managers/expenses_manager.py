"""This module"""

from datetime import date
from managers.table_manager import TableManager as tm
from managers.categories_manager import Category, select_category
from database.database_commands import insert_data
from user.input import get_amount, get_description
from user.interface import money_format

INSERT_EXPENSE = """
INSERT INTO expenses(date, description, amount, categoryID)
VALUES(?,?,?,?)
"""


class Expense:
    """This class manages expenses in the expenses table."""
    def __init__(self, date_, description, amount, category):
        self.date_ = date_
        self.description = description
        self.amount = amount
        self.category = category

    def get_atts_to_insert(self):
        """This"""
        return (self.date_, self.description, self.amount, self.category.id_)

    def insert_expense(self):
        """This"""
        insert_data(INSERT_EXPENSE, self.get_atts_to_insert())


def get_new_expense():
    """This function gets a new expense from the user.

    :return: today's date, expense, amount and category ID number
    :rtype: tuple
    """
    date_ = date.today()
    description = get_description("expense")
    amount = get_amount()
    category = select_category()

    return Expense(date_, description, amount, category)


def print_expenses(expense_list):
    """This function"""
    max_des = max(max(len(i.description) for i in expense_list), 7)
    max_amt = max(max(len(money_format(i.amount)) for i in expense_list), 5)
    max_cat = max(max(len(i.category.description) for i in expense_list), 8)

    length_line = max_des + max_amt + max_cat + 22
    header_line = "\033[1m_\033[0m" * length_line
    date_ = "\033[1mDate" + " " * 10
    cat = "Category\033[0m"

    print(header_line + "\n")
    print(f"{date_}{"Expense":<{max_des + 4}}{"Amount":<{max_amt + 4}}{cat}")
    print(header_line)

    for expense in expense_list:
        date_ = expense.date_.strftime("%Y-%m-%d") + " " * 4
        des = expense.description
        amount = money_format(expense.amount)
        cat = expense.category.description

        print(f"\n{date_}{des:<{max_des + 4}}{amount:<{max_amt + 4}}{cat}")
        print("\033[90m_\033[0m" * length_line)


def get_expenses_from_rows(rows_list):
    """This"""
    expenses_list = []
    for row in rows_list:
        cat = Category(row[-3], row[-2], row[-1])
        expenses_list.append(Expense(row[1], row[2], row[3], cat))
    return expenses_list


def get_expenses_this_month():
    """This"""
    x = tm(table1="expenses", table2="categories", description="category")
    rows_list = x.get_this_month()
    expenses_list = get_expenses_from_rows(rows_list)
    return expenses_list
