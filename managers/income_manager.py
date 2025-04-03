"""This"""

from managers.source_manager import SourceManager as SM
from database.database_commands import insert_data, fetch_all_with_args, fetch_all
from user.input import get_amount
from user.interface import money_format

GET_JOINED = """
SELECT date, source, amount, sourceID
    FROM income
    INNER JOIN source ON income.sourceID=source.id
"""
SELECT_BY_SRC = """
SELECT date, source, amount, sourceID
    FROM income
    INNER JOIN source ON income.sourceID=source.id
    WHERE sourceID = ?
    ORDER BY income.id DESC
"""
INSERT_INCOME= """
INSERT INTO income(date, sourceID, amount)
VALUES((strftime('%Y-%m-%d', 'now')),?,?)
"""
SELECT_BY_DATE = """
SELECT date, source, amount, sourceID
    FROM income
    INNER JOIN source ON income.sourceID=source.id
    WHERE date >= ?
    ORDER BY income.id DESC
"""
SELECT_BY_DATE_SRC = """
SELECT date, source, amount, sourceID
    FROM income
    INNER JOIN source ON income.sourceID=source.id
    WHERE date >= ? AND sourceID = ?
    ORDER BY income.id DESC
"""


class IncomeManager:
    """This class manages expenses in the expense table."""
    table = "income"
    def __init__(self, **kwargs):
        self.date_ = kwargs.setdefault("da", None)
        self.amount = kwargs.setdefault("am", None)
        self.source = kwargs.setdefault("so", None)
        self.start = kwargs.setdefault("st", None)

    def get_atts_to_insert(self):
        """This"""
        return (self.source.id_, self.amount)

    def get_atts_to_print(self):
        """This"""
        date_ = self.date_
        amount = self.amount
        source = self.source.source
        return date_, amount, source

    def get_new_income(self):
        """This """
        self.amount = get_amount()
        self.source = SM().select_source()
        return self

    def insert_income(self):
        """This"""
        insert_data(INSERT_INCOME, self.get_atts_to_insert())


def fetch_rows_by_date(start):
    """This"""
    rows = fetch_all_with_args(SELECT_BY_DATE, (start,))
    return rows


def fetch_rows_by_date_src(start, source_id):
    """This"""
    rows = fetch_all_with_args(SELECT_BY_DATE_SRC, (start, source_id))
    return rows


def fetch_rows_by_src(source_id):
    "This function"
    rows = fetch_all_with_args(SELECT_BY_SRC, (source_id,))
    return rows


def fetch_all_rows():
    """This"""
    rows = fetch_all(GET_JOINED)
    return rows


def get_objects_from_rows(rows):
    """This"""
    income_list = []

    for row in rows:
        income = IncomeManager(da=row[0], am=row[2])
        income.source = SM(so=row[1])
        income_list.append(income)

    return income_list


def print_incomes(income_list):
    """This function"""
    max_src = max(max(len(i.source.source) for i in income_list), 13)
    max_amt = max(max(len(money_format(i.amount)) for i in income_list), 6)

    length_line = max_src + max_amt + 18
    header_line = "\033[1m_\033[0m" * length_line
    date_ = "\033[1mDate" + " " * 10

    print(header_line + "\n")
    print(f"{date_}{"Income Source":<{max_src + 4}}{"Amount":<{max_amt + 4}}")
    print(header_line)

    for income in income_list:
        date_ = income.date_ + " " * 4
        amount = money_format(income.amount)
        src = income.source.source

        print(f"\n{date_}{src:<{max_src + 4}}{amount:<{max_amt + 4}}")
        print("\033[90m_\033[0m" * length_line)
