"""This"""

from database.database_commands import (fetch_all, fetch_one,
                                        fetch_one_with_args)

COUNT = """select count(*) from {}"""
SELECT_MONTH = """
SELECT * FROM {}
    INNER JOIN {} ON {}.{}ID={}.id
    WHERE strftime('%Y-%m-%d', {}) <= date <= strftime('%Y-%m-%d', {})
    ORDER BY id DESC
"""
SELECT_ROWS = """SELECT * FROM {}"""
SELECT_DESCRIPTIONS = """SELECT description FROM {}"""
SELECT_FROM_ID = """SELECT * FROM {} WHERE id = ?"""


class TableManager:
    """This class manages expenses in the expenses table."""
    def __init__(self, **kwargs):
        self.table1 = kwargs.setdefault("table1", None)
        self.table2 = kwargs.setdefault("table2", None)
        self.dates = kwargs.setdefault("dates", None)
        self.description = kwargs.setdefault("description", None)
        self.id_ = kwargs.setdefault("id_", None)

    def __str__(self):
        """Constructs a string in a readable format."""

    def count_rows(self):
        """Does stuff"""
        return fetch_one(COUNT.format(self.table1))

    def get_all_rows(self):
        """Does stuff"""
        return fetch_all(SELECT_ROWS.format(self.table1))

    def get_descriptions(self):
        """This"""
        table1 = self.table1
        return fetch_all(SELECT_DESCRIPTIONS.format(table1))

    def get_row_from_id(self):
        """This"""
        select = SELECT_FROM_ID.format(self.table1)
        return fetch_one_with_args(select, (self.id_,))

    def get_by_date(self):
        """This"""
        t1 = self.table1
        t2 = self.table2
        des = self.description
        (start, end) = self.dates
        join = SELECT_MONTH.format(t1, t2, t1, des, t2, start, end)
        return fetch_all(join)
