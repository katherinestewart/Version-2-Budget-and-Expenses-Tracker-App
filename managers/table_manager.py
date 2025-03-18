"""This"""

from database.database_commands import (fetch_all, fetch_one,
                                        fetch_one_with_args)

COUNT = """select count(*) from {}"""
GET_JOIN_EXPENSE = """
SELECT * FROM {}
    INNER JOIN {} ON {}.{}={}.id
    ORDER BY id DESC
"""
SELECT_MONTH = """
SELECT * FROM {}
    INNER JOIN {} ON {}.{}={}.id
    WHERE strftime('%Y-%m-%d', {}) <= date
    ORDER BY id DESC
"""
SELECT_ROWS = """SELECT * FROM {}"""
SELECT_DESCRIPTIONS = """SELECT description FROM {}"""
SELECT_FROM_ID = """SELECT * FROM {} WHERE id = ?"""


class TableManager:
    """This class manages expenses in the expenses table."""
    def __init__(self, **kwargs):
        self.table = kwargs.setdefault("table", None)
        self.rows = kwargs.setdefault("table", None)

    def count_rows(self):
        """Does stuff"""
        return fetch_one(COUNT.format(self.table))

    def get_all_rows(self):
        """Does stuff"""
        return fetch_all(SELECT_ROWS.format(self.table))

    def get_descriptions(self):
        """This"""
        table = self.table
        return fetch_all(SELECT_DESCRIPTIONS.format(table))

    def get_row_from_id(self):
        """This"""
        select = SELECT_FROM_ID.format(self.table)
        return fetch_one_with_args(select, (self.id_,))

