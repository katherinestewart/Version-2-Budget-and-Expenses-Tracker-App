"""This module"""

from managers.category_manager import CategoryManager as CM
from database.database_commands import insert_data, fetch_all_with_args, fetch_all
from user.input import get_amount, get_description
from user.interface import money_format

GET_JOINED = """
SELECT date, expense, amount, categoryID, category
    FROM expense
    INNER JOIN category ON expense.categoryID=category.id
"""
SELECT_BY_CAT = """
SELECT date, expense, amount, categoryID, category
    FROM expense
    INNER JOIN category ON expense.categoryID=category.id
    WHERE categoryID = ?
    ORDER BY expense.id DESC
"""
INSERT_EXPENSE = """
INSERT INTO expense(date, expense, amount, categoryID)
VALUES((strftime('%Y-%m-%d', 'now')),?,?,?)
"""
SELECT_BY_DATE = """
SELECT date, expense, amount, categoryID, category
    FROM expense
    INNER JOIN category ON expense.categoryID=category.id
    WHERE date >= ?
    ORDER BY expense.id DESC
"""
SELECT_BY_DATE_CAT = """
SELECT date, expense, amount, categoryID, category
    FROM expense
    INNER JOIN category ON expense.categoryID=category.id
    WHERE date >= ? AND categoryID = ?
    ORDER BY expense.id DESC
"""


class ExpenseManager:
    """This class manages expenses in the expense table."""
    table = "expense"
    def __init__(self, **kwargs):
        self.date_ = kwargs.setdefault("da", None)
        self.expense = kwargs.setdefault("ex", None)
        self.amount = kwargs.setdefault("am", None)
        self.category = kwargs.setdefault("ca", None)
        self.start = kwargs.setdefault("st", None)

    def get_atts_to_insert(self):
        """This"""
        return (self.expense, self.amount, self.category.id_)

    def get_atts_to_print(self):
        """This"""
        date_ = self.date_
        expense = self.expense
        amount = self.amount
        category = self.category.category
        return date_, expense, amount, category

    def get_new_expense(self):
        """This """
        self.expense = get_description(self.table)
        self.amount = get_amount()
        self.category = CM().select_category()
        return self

    def insert_expense(self):
        """This"""
        insert_data(INSERT_EXPENSE, self.get_atts_to_insert())


def fetch_rows_by_date(start):
    """This"""
    rows = fetch_all_with_args(SELECT_BY_DATE, (start,))
    return rows


def fetch_rows_by_date_cat(start, category_id):
    """This"""
    rows = fetch_all_with_args(SELECT_BY_DATE_CAT, (start, category_id))
    return rows


def fetch_rows_by_cat(category_id):
    "This function"
    rows = fetch_all_with_args(SELECT_BY_CAT, (category_id,))
    return rows


def fetch_all_rows():
    """This"""
    rows = fetch_all(GET_JOINED)
    return rows


def get_objects_from_rows(rows):
    """This"""
    expense_list = []

    for row in rows:
        expense = ExpenseManager(da=row[0], ex=row[1], am=row[2])
        expense.category = CM(id=row[3], ca=row[4])
        expense_list.append(expense)

    return expense_list


def print_expenses(expense_list):
    """This function"""
    max_des = max(max(len(i.expense) for i in expense_list), 7)
    max_amt = max(max(len(money_format(i.amount)) for i in expense_list), 5)
    max_cat = max(max(len(i.category.category) for i in expense_list), 8)

    length_line = max_des + max_amt + max_cat + 22
    header_line = "\033[1m_\033[0m" * length_line
    date_ = "\033[1mDate" + " " * 10
    cat = "Category\033[0m"

    print(header_line + "\n")
    print(f"{date_}{"Expense":<{max_des + 4}}{"Amount":<{max_amt + 4}}{cat}")
    print(header_line)

    for expense in expense_list:
        date_ = expense.date_ + " " * 4
        des = expense.expense
        amount = money_format(expense.amount)
        cat = expense.category.category

        print(f"\n{date_}{des:<{max_des + 4}}{amount:<{max_amt + 4}}{cat}")
        print("\033[90m_\033[0m" * length_line)
