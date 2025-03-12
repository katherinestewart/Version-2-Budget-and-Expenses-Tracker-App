"""This module contains all functions with logic to interact with the
database finances.db. This is the only module which accesses the
database. There are six tables; expenses, income, categories, sources,
budget and goals.
"""

from contextlib import contextmanager
import sqlite3
from database import populate_finances_db as pf


CREATE_EXPENSES_TABLE = """CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, description TEXT,
amount FLOAT, categoryID INTEGER, FOREIGN KEY(categoryID)
REFERENCES categories(id))"""
CREATE_INCOME_TABLE = """CREATE TABLE IF NOT EXISTS income
(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, sourceID INT,
amount FLOAT, FOREIGN KEY(sourceID) REFERENCES income_sources(id))"""
CREATE_CATEGORY_TABLE = """CREATE TABLE IF NOT EXISTS categories
(id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, budgetID TEXT,
FOREIGN KEY(budgetID) REFERENCES budget(id))"""
CREATE_BUDGET_TABLE = """CREATE TABLE IF NOT EXISTS budget
(id INTEGER PRIMARY KEY AUTOINCREMENT, amount FLOAT, term TEXT)"""
CREATE_GOALS_TABLE = """CREATE TABLE IF NOT EXISTS goals
(id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, amount FLOAT, term TEXT)"""
CREATE_SOURCES_TABLE = """CREATE TABLE IF NOT EXISTS sources
(id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT)"""
MAX_BUDGET_ID = """SELECT MAX(id) FROM budget"""
INSERT_EXPENSE = """INSERT INTO expenses(date, description, amount, categoryID)
VALUES(?,?,?,?)"""
INSERT_INCOME = """INSERT INTO income(date, sourceID, amount) VALUES(?,?,?)"""
INSERT_CATEGORY = """INSERT INTO categories(description) VALUES(?)"""
INSERT_BUDGET = """INSERT INTO budget(amount, term) VALUES(?,?)"""
INSERT_GOAL = """INSERT INTO goals(description, amount, term) VALUES(?,?,?)"""
INSERT_SOURCE = """INSERT INTO sources(description) VALUES(?)"""
UPDATE_CATEGORY = """UPDATE categories SET budgetID = ? WHERE id = ?"""
SELECT_FIRST_EXPENSE = """SELECT * FROM expenses WHERE id = 1"""




@contextmanager
def get_cursor(commit_changes=False):
    """This function catches any errors when connecting to the database
    and creates a cursor.

    :param commit_changes: If changes should be committed (default = False)
    :return: cursor
    :rtype: cursor
    """
    try:
        db = sqlite3.connect("finances.db")
        cursor = db.cursor()
        yield cursor
    except sqlite3.Error as e:
        db.rollback()
        raise e
    else:
        if commit_changes:
            db.commit()
    finally:
        db.close()


def insert_data(string, args):
    """This function inserts data into the database.

    :param string: SQLite command
    :param args: tuple with arguments for command
    :return: None
    """
    with get_cursor(True) as cursor:
        cursor.execute(string, args)


def insert_many(command):
    """This function inserts a list of data into the database.

    :param command: tuple containing (str, list)
    :return: None
    """
    with get_cursor(True) as cursor:
        cursor.executemany(*command)


def fetch_one(command):
    """This function fetches data from one row in the database.

    :param input: SQLite command
    :param args: arguments for SQLite command
    :return: data from one row
    :rtype: tuple
    """
    with get_cursor() as cursor:
        cursor.execute(command)
        data = cursor.fetchone()

    return data


def fetch_one_with_args(string, args):
    """This function fetches data from one row in the database by
    selected arguments.

    :param input: SQLite command
    :param args: arguments for SQLite command
    :return: data from one row
    :rtype: tuple
    """
    with get_cursor() as cursor:
        cursor.execute(string, args)
        data = cursor.fetchone()

    return data


def fetch_all(command):
    """This function fetches data from one or more rows in the
    database.

    :param input: SQLite command
    :param args: arguments for SQLite command
    :return: data from one or more rows
    :rtype: List of tuples
    """
    with get_cursor() as cursor:
        cursor.execute(command)
        data = cursor.fetchall()

    return data


def fetch_all_with_args(string, args):
    """This function fetches data from one or more rows in the
    database which match selected arguments.

    :param input: SQLite command
    :param args: arguments for SQLite command
    :return: data from one or more rows
    :rtype: List of tuples
    """
    with get_cursor() as cursor:
        cursor.execute(string, args)
        data = cursor.fetchall()

    return data


def create_tables():
    """This function creates all tables in the database if they don't
    exist and calls function to populate tables.

    :return: None
    """
    commands = [
        CREATE_EXPENSES_TABLE,
        CREATE_CATEGORY_TABLE,
        CREATE_INCOME_TABLE,
        CREATE_SOURCES_TABLE,
        CREATE_BUDGET_TABLE,
        CREATE_GOALS_TABLE,
    ]

    for command in commands:
        with get_cursor() as cursor:
            cursor.execute(command)

    populate_tables()


def populate_tables():
    """This function checks if there is any data in the expenses table
    and if not it populates all tables with dummy data for testing.

    :return: None
    """
    if not fetch_one(SELECT_FIRST_EXPENSE):
        pf.populate_tables()


def insert_budget(category_id, budget):
    """This function enters a new budget assigned to a category.

    :param category_id: primary key in categories table
    :param budget: tuple containing (amount, term)
    :return: None
    """
    insert_data(INSERT_BUDGET, budget)
    budget_id = fetch_one(MAX_BUDGET_ID)
    insert_data(UPDATE_CATEGORY, (*budget_id, category_id))
