"""This"""

from database.database_commands import (fetch_all, fetch_one,
                                        fetch_one_with_args)

COUNT = """select count(*) from {}"""
JOINED_ROWS = """SELECT * FROM {} INNER JOIN {} ON
{}.{}ID={}.id ORDER BY id DESC"""
SELECT_ROWS = """SELECT * FROM {}"""
SELECT_DESCRIPTIONS = """SELECT description FROM {}"""
SELECT_FROM_ID = """SELECT * FROM {} where id = ?"""


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

    def get_joined_rows(self):
        """This"""
        table1 = self.table1
        table2 = self.table2
        description = self.description
        join = JOINED_ROWS.format(table1, table2, table1, description, table2)
        return fetch_all(join)

    def get_row_from_id(self):
        """This"""
        select = SELECT_FROM_ID.format(self.table1)
        return fetch_one_with_args(select, (self.id_,))
