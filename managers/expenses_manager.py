"""This module"""

from datetime import date
from managers.categories_manager import select_category
from database.database_commands import insert_data
from user.input import get_amount, get_description

INSERT_EXPENSE = """INSERT INTO expenses
(date, description, amount, categoryID) VALUES(?,?,?,?)
"""

'''
class ExpensesManager:
    """This class manages expenses in the expenses table."""
    def __init__(self, **kwargs):
        self.rows = kwargs["rows"]
        self.dates = kwargs["date"]
        self.category = kwargs["category"]

    def __str__(self):
        """Constructs a string in a readable format."""

    def rows_by_date(self):
        """Does stuff"""'''


class Expense:
    """This class manages expenses in the expenses table."""
    def __init__(self, date_, description, amount, category_id):
        self.date_ = date_
        self.description = description
        self.amount = amount
        self.category_id = category_id

    def get_all_att(self):
        """This method returns the attributes of an Expense object.

        :param self: Expense object
        :return: Tuple containing Expense attributes
        """
        return (self.date_, self.description, self.amount, self.category_id)

    def insert_expense(self):
        """This"""
        insert_data(INSERT_EXPENSE, self.get_all_att())


def get_expense():
    """This function gets a new expense from the user.

    :return: today's date, expense, amount and category ID number
    :rtype: tuple
    """
    today = date.today().strftime("%Y-%m-%d")
    description = get_description("expense")
    amount = get_amount()
    category_id = select_category().id_

    return Expense(today, description, amount, category_id)
