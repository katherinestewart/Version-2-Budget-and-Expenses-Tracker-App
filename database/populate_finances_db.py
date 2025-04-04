"""This module adds dummy data to the tables in the database for
testing purposes."""

import sqlite3
from contextlib import contextmanager

INSERT_EXPENSE = """
INSERT INTO expense(date, expense, amount, categoryID)
VALUES(?,?,?,?)
"""
INSERT_CATEGORY = """INSERT INTO category(category) VALUES(?)"""
INSERT_INCOME = """INSERT INTO income(date, sourceID, amount) VALUES(?,?,?)"""
INSERT_BUDGET = """INSERT INTO budget(amount, term) VALUES(?,?)"""
INSERT_GOAL = """INSERT INTO goals(goal, amount, term) VALUES(?,?,?)"""
INSERT_SOURCE = """INSERT INTO source(source) VALUES(?)"""
MAX_BUDGET_ID = """SELECT MAX(id) FROM budget"""
INSERT_BUDGET = """INSERT INTO budget(amount, term) VALUES(?,?)"""
UPDATE_CATEGORY = """UPDATE category SET budgetID = ? WHERE id = ?"""
SELECT_FIRST_EXPENSE = """SELECT * FROM expense WHERE id = 1"""

expenses = [
    ("2024-01-01", "Home Insurance", 180.55, 3),
    ("2024-01-01", "Mortgage", 1000, 5),
    ("2024-01-01", "Internet", 60, 1),
    ("2024-01-01", "Phone bill", 45, 6),
    ("2024-01-01", "Gas & Electric", 68, 5),
    ("2024-01-01", "Council Tax", 160, 1),
    ("2024-01-01", "Gym membership", 100, 4),
    ("2024-01-02", "Boots", 63.98, 6),
    ("2024-01-03", "Dinner", 34.27, 4),
    ("2024-01-04", "Bowling", 24.50, 4),
    ("2024-01-09", "Fuel", 57.78, 7),
    ("2024-01-10", "Lidl", 83.20, 2),
    ("2024-01-11", "Train", 102.10, 7),
    ("2024-01-12", "Pizza Express", 61.20, 4),
    ("2024-01-15", "Lidl", 19.23, 2),
    ("2024-01-18", "Veg", 18.35, 2),
    ("2024-01-21", "Asda", 98.38, 2),
    ("2024-01-21", "Asda", 50.90, 2),
    ("2024-01-22", "Christmas presents", 125.80, 2),
    ("2024-01-23", "Tesco", 42.56, 2),
    ("2024-01-25", "stuff", 200, 6),
    ("2024-01-26", "Car service", 240, 6),
    ("2024-01-31", "Tax", 2000, 6),
    ("2024-02-02", "Home Insurance", 180.55, 3),
    ("2024-02-02", "Mortgage", 1000, 5),
    ("2024-02-02", "Internet", 60, 1),
    ("2024-02-02", "Phone bill", 45, 6),
    ("2024-02-02", "Gas & Electric", 68, 5),
    ("2024-02-02", "Council Tax", 160, 1),
    ("2024-02-02", "Gym membership", 100, 4),
    ("2024-02-02", "Tesco", 77.76, 2),
    ("2024-02-05", "Swimming", 10, 4),
    ("2024-02-07", "Sainsbury's", 62.17, 2),
    ("2024-02-09", "Presents", 85, 6),
    ("2024-02-10", "Fuel", 56.74, 7),
    ("2024-02-11", "Asda", 20.24, 2),
    ("2024-02-13", "Train", 85, 7),
    ("2024-02-15", "Car Insurance", 483.00, 2),
    ("2024-02-18", "Aldi", 20.01, 2),
    ("2024-02-20", "stuff", 345.98, 6),
    ("2024-02-25", "Sainsbury's", 85.40, 2),
    ("2024-02-26", "Asda", 59.30, 2),
    ("2024-03-01", "Home Insurance", 180.55, 3),
    ("2024-03-01", "Mortgage", 1000, 5),
    ("2024-03-01", "Internet", 60, 1),
    ("2024-03-01", "Phone bill", 45, 6),
    ("2024-03-01", "Gas & Electric", 68, 5),
    ("2024-03-01", "Council Tax", 160, 1),
    ("2024-03-01", "Gym membership", 100, 4),
    ("2024-03-05", "Tesco", 32.57, 2),
    ("2024-03-08", "Asda", 29.54, 2),
    ("2024-03-09", "Fuel", 58.06, 7),
    ("2024-03-13", "Asda", 82.13, 2),
    ("2024-03-20", "Tesco", 55.60, 2),
    ("2024-03-23", "GAP", 85.00, 6),
    ("2024-03-24", "Tesco", 62.40, 2),
    ("2024-03-25", "Tesco", 12.30, 2),
    ("2024-03-27", "Fuel", 18.10, 7),
    ("2024-03-28", "Clothes", 54.50, 6),
    ("2024-03-30", "Sainsbury's", 10.50, 2),
    ("2024-03-31", "Pub", 32.40, 4),
    ("2024-05-31", "stuff", 200, 6),
    ("2024-04-01", "Home Insurance", 180.55, 3),
    ("2024-04-01", "Mortgage", 1000, 5),
    ("2024-04-01", "Internet", 60, 1),
    ("2024-04-01", "Phone bill", 45, 6),
    ("2024-04-01", "Gas & Electric", 68, 5),
    ("2024-04-01", "Council Tax", 160, 1),
    ("2024-04-01", "Gym membership", 100, 4),
    ("2024-04-02", "Dinner out", 42.00, 4),
    ("2024-04-05", "Fuel", 56.10, 7),
    ("2024-04-09", "Tesco", 25.10, 2),
    ("2024-04-11", "Lululemon", 75.00, 6),
    ("2024-04-14", "Asda", 83.30, 2),
    ("2024-04-20", "Asda", 100.53, 2),
    ("2024-04-23", "Tesco", 23.05, 2),
    ("2024-04-25", "Asda", 45.46, 2),
    ("2024-04-28", "stuff", 122.12, 6),
    ("2024-04-30", "Asda", 48.50, 2),
    ("2024-05-01", "Home Insurance", 180.55, 3),
    ("2024-05-01", "Mortgage", 1000, 5),
    ("2024-05-01", "Internet", 60, 1),
    ("2024-05-01", "Phone bill", 45, 6),
    ("2024-05-01", "Gas & Electric", 68, 5),
    ("2024-05-01", "Council Tax", 160, 1),
    ("2024-05-01", "Gym membership", 100, 4),
    ("2024-05-03", "Aldi", 30, 2),
    ("2024-05-06", "Fuel", 62.15, 7),
    ("2024-05-08", "Asda", 51.70, 2),
    ("2024-05-15", "Asda", 104.32, 2),
    ("2024-05-18", "Zara", 83.95, 2),
    ("2024-05-23", "Asda", 70.90, 2),
    ("2024-05-25", "stuff", 200, 6),
    ("2024-05-22", "stuff", 833.90, 6),
    ("2024-05-30", "Sainsbury's", 81.42, 2),
    ("2024-06-01", "Home Insurance", 180.55, 3),
    ("2024-06-01", "Mortgage", 1000, 5),
    ("2024-06-01", "Internet", 60, 1),
    ("2024-06-01", "Phone bill", 45, 6),
    ("2024-06-01", "Gas & Electric", 68, 5),
    ("2024-06-01", "Council Tax", 160, 1),
    ("2024-06-01", "Gym membership", 100, 4),
    ("2024-06-09", "Fuel", 57.78, 7),
    ("2024-06-10", "Lidl", 83.20, 2),
    ("2024-06-12", "Pizza Express", 61.20, 4),
    ("2024-06-15", "Lidl", 19.23, 2),
    ("2024-06-21", "Asda", 98.38, 2),
    ("2024-06-21", "Asda", 50.90, 2),
    ("2024-06-22", "Christmas presents", 125.80, 2),
    ("2024-06-23", "Tesco", 42.56, 2),
    ("2024-06-25", "Stuff", 300, 6),
    ("2024-07-01", "Home Insurance", 180.55, 3),
    ("2024-07-01", "Mortgage", 1000, 5),
    ("2024-07-01", "Internet", 60, 1),
    ("2024-07-01", "Phone bill", 45, 6),
    ("2024-07-01", "Gas & Electric", 68, 5),
    ("2024-07-01", "Council Tax", 160, 1),
    ("2024-07-01", "Gym membership", 100, 4),
    ("2024-07-09", "Fuel", 57.78, 7),
    ("2024-07-10", "Lidl", 83.20, 2),
    ("2024-07-12", "Pizza Express", 61.20, 4),
    ("2024-07-15", "Lidl", 19.23, 2),
    ("2024-07-21", "Asda", 98.38, 2),
    ("2024-07-21", "Asda", 50.90, 2),
    ("2024-07-22", "Christmas presents", 125.80, 2),
    ("2024-07-23", "Tesco", 42.56, 2),
    ("2024-07-24", "stuff", 600, 6),
    ("2024-01-30", "Tax", 1600, 6),
    ("2024-08-01", "Home Insurance", 180.55, 3),
    ("2024-08-01", "Mortgage", 1000, 5),
    ("2024-08-01", "Internet", 60, 1),
    ("2024-08-01", "Phone bill", 45, 6),
    ("2024-08-01", "Gas & Electric", 68, 5),
    ("2024-08-01", "Council Tax", 160, 1),
    ("2024-08-01", "Gym membership", 100, 4),
    ("2024-08-09", "Fuel", 57.78, 7),
    ("2024-08-10", "Lidl", 83.20, 2),
    ("2024-08-12", "Pizza Express", 61.20, 4),
    ("2024-08-15", "Lidl", 19.23, 2),
    ("2024-08-21", "Asda", 98.38, 2),
    ("2024-08-21", "Asda", 50.90, 2),
    ("2024-08-22", "Christmas presents", 125.80, 2),
    ("2024-08-23", "Tesco", 42.56, 2),
    ("2024-08-27", "stuff", 467, 6),
    ("2024-07-01", "Home Insurance", 180.55, 3),
    ("2024-07-01", "Mortgage", 1000, 5),
    ("2024-07-01", "Internet", 60, 1),
    ("2024-07-01", "Phone bill", 45, 6),
    ("2024-07-01", "Gas & Electric", 68, 5),
    ("2024-07-01", "Council Tax", 160, 1),
    ("2024-07-01", "Gym membership", 100, 4),
    ("2024-07-09", "Fuel", 57.78, 7),
    ("2024-07-10", "Lidl", 83.20, 2),
    ("2024-07-12", "Pizza Express", 61.20, 4),
    ("2024-07-15", "Lidl", 19.23, 2),
    ("2024-07-21", "Asda", 98.38, 2),
    ("2024-07-21", "Asda", 50.90, 2),
    ("2024-07-22", "Christmas presents", 125.80, 2),
    ("2024-07-23", "Tesco", 42.56, 2),
    ("2024-07-29", "Stuff", 500, 2),
    ("2024-08-01", "Home Insurance", 180.55, 3),
    ("2024-08-01", "Mortgage", 1000, 5),
    ("2024-08-01", "Internet", 60, 1),
    ("2024-08-01", "Phone bill", 45, 6),
    ("2024-08-01", "Gas & Electric", 68, 5),
    ("2024-08-01", "Council Tax", 160, 1),
    ("2024-08-01", "Gym membership", 100, 4),
    ("2024-08-02", "Tesco", 77.76, 2),
    ("2024-08-07", "Sainsbury's", 62.17, 2),
    ("2024-08-10", "Fuel", 56.74, 7),
    ("2024-08-11", "Asda", 20.24, 2),
    ("2024-08-15", "Car Insurance", 483.00, 2),
    ("2024-08-18", "Aldi", 20.01, 2),
    ("2024-08-25", "Sainsbury's", 85.40, 2),
    ("2024-08-30", "Asda", 59.30, 2),
    ("2024-08-30", "Stuff", 710, 2),
    ("2024-09-01", "Home Insurance", 180.55, 3),
    ("2024-09-01", "Mortgage", 1000, 5),
    ("2024-09-01", "Internet", 60, 1),
    ("2024-09-01", "Phone bill", 45, 6),
    ("2024-09-01", "Gas & Electric", 68, 5),
    ("2024-09-01", "Council Tax", 160, 1),
    ("2024-09-01", "Gym membership", 100, 4),
    ("2024-09-05", "Tesco", 32.57, 2),
    ("2024-09-08", "Asda", 29.54, 2),
    ("2024-09-09", "Fuel", 58.06, 7),
    ("2024-09-13", "Asda", 82.13, 2),
    ("2024-09-20", "Tesco", 55.60, 2),
    ("2024-09-23", "GAP", 85.00, 6),
    ("2024-09-24", "Tesco", 62.40, 2),
    ("2024-09-25", "Tesco", 12.30, 2),
    ("2024-09-27", "Fuel", 18.10, 7),
    ("2024-09-28", "Clothes", 54.50, 6),
    ("2024-09-29", "Sainsbury's", 10.50, 2),
    ("2024-09-30", "Pub", 32.40, 4),
    ("2024-09-30", "Stuff", 300, 6),
    ("2024-10-01", "Home Insurance", 180.55, 3),
    ("2024-10-01", "Mortgage", 1000, 5),
    ("2024-10-01", "Internet", 60, 1),
    ("2024-10-01", "Phone bill", 45, 6),
    ("2024-10-01", "Gas & Electric", 68, 5),
    ("2024-10-01", "Council Tax", 160, 1),
    ("2024-10-01", "Gym membership", 100, 4),
    ("2024-10-02", "Pub", 32.40, 4),
    ("2024-10-03", "Tesco", 15.20, 2),
    ("2024-10-02", "Dinner out", 42.00, 4),
    ("2024-10-05", "Fuel", 56.10, 7),
    ("2024-10-09", "Tesco", 25.10, 2),
    ("2024-10-11", "Lululemon", 75.00, 6),
    ("2024-10-14", "Asda", 83.30, 2),
    ("2024-10-20", "Asda", 100.53, 2),
    ("2024-10-23", "Tesco", 23.05, 2),
    ("2024-10-25", "Asda", 45.46, 2),
    ("2024-10-30", "Stuff", 310, 6),
    ("2024-10-30", "Asda", 48.50, 2),
    ("2024-11-01", "Mortgage", 1000, 5),
    ("2024-11-01", "Internet", 60, 1),
    ("2024-11-01", "Phone bill", 45, 6),
    ("2024-11-01", "Gas & Electric", 68, 5),
    ("2024-11-01", "Council Tax", 160, 1),
    ("2024-11-01", "Gym membership", 100, 4),
    ("2024-11-02", "Pub", 24, 4),
    ("2024-11-03", "Sainsbury's", 43.10, 2),
    ("2024-11-03", "Aldi", 21.18, 2),
    ("2024-11-06", "Fuel", 62.15, 7),
    ("2024-11-08", "Asda", 51.70, 2),
    ("2024-11-15", "Asda", 61.72, 2),
    ("2024-11-18", "Zara", 83.95, 2),
    ("2024-11-23", "Asda", 70.90, 2),
    ("2024-1-25", "Stuff", 600, 6),
    ("2024-11-30", "Sainsbury's", 81.42, 2),
    ("2024-12-01", "Mortgage", 1000, 5),
    ("2024-12-01", "Internet", 60, 1),
    ("2024-12-01", "Phone bill", 45, 6),
    ("2024-12-01", "Gas & Electric", 68, 5),
    ("2024-12-01", "Council Tax", 160, 1),
    ("2024-12-01", "Gym membership", 100, 4),
    ("2024-12-02", "Christmas presents", 113.23, 4),
    ("2024-12-03", "Tesco", 20.80, 2),
    ("2024-12-06", "Tesco", 71.40, 2),
    ("2024-12-09", "Fuel", 57.78, 7),
    ("2024-12-10", "Lidl", 83.20, 2),
    ("2024-12-12", "Pizza Express", 61.20, 4),
    ("2024-12-15", "Lidl", 19.23, 2),
    ("2024-12-21", "Asda", 98.38, 2),
    ("2024-12-21", "Asda", 50.90, 2),
    ("2024-12-22", "Christmas presents", 125.80, 2),
    ("2024-12-23", "Tesco", 42.56, 2),
    ("2024-12-30", "Stuff", 810, 2),
    ("2025-01-01", "Mortgage", 1000, 5),
    ("2025-01-01", "Internet", 60, 1),
    ("2025-01-01", "Phone bill", 45, 6),
    ("2025-01-01", "Gas & Electric", 68, 5),
    ("2025-01-01", "Council Tax", 160, 1),
    ("2025-01-01", "Gym membership", 100, 4),
    ("2025-01-02", "Fuel", 24.50, 4),
    ("2025-01-03", "Weekend Away", 550.60, 3),
    ("2025-01-02", "Tesco", 77.76, 2),
    ("2025-01-07", "Sainsbury's", 62.17, 2),
    ("2025-01-10", "Fuel", 56.74, 7),
    ("2025-01-11", "Asda", 20.24, 2),
    ("2025-01-15", "Car Insurance", 483.00, 3),
    ("2025-01-18", "Aldi", 20.01, 2),
    ("2025-01-25", "Sainsbury's", 85.40, 2),
    ("2025-01-30", "Asda", 59.30, 2),
    ("2024-08-30", "Stuff", 610, 2),
    ("2025-02-01", "Mortgage", 1000, 5),
    ("2025-02-01", "Internet", 60, 1),
    ("2025-02-01", "Phone bill", 45, 6),
    ("2025-02-01", "Gas & Electric", 68, 5),
    ("2025-02-01", "Council Tax", 160, 1),
    ("2025-02-01", "Gym membership", 100, 4),
    ("2025-02-02", "Pub", 12, 4),
    ("2025-02-03", "Tesco", 32.12, 2),
    ("2025-02-05", "Tesco", 32.57, 2),
    ("2025-02-08", "Asda", 29.54, 2),
    ("2025-02-09", "Fuel", 58.06, 7),
    ("2025-02-13", "Asda", 82.13, 2),
    ("2025-02-20", "Tesco", 55.60, 2),
    ("2024-02-23", "GAP", 85.00, 6),
    ("2025-02-24", "Tesco", 62.40, 2),
    ("2025-02-25", "Tesco", 12.30, 2),
    ("2025-02-27", "Fuel", 18.10, 7),
    ("2025-02-28", "Clothes", 54.50, 6),
    ("2024-02-29", "Stuff", 710, 2),
    ("2025-03-01", "Sainsbury's", 10.50, 2),
    ("2025-03-01", "Mortgage", 1000, 5),
    ("2025-03-01", "Internet", 60, 1),
    ("2025-03-01", "Phone bill", 45, 6),
    ("2025-03-01", "Gas & Electric", 68, 5),
    ("2025-03-01", "Council Tax", 160, 1),
    ("2025-03-01", "Gym membership", 100, 4),
    ("2025-03-02", "Pub", 32.40, 4),
    ("2025-03-02", "Weekend break", 200, 2),
    ("2025-03-03", "Tesco", 15.20, 2),
]
incomes = [
    ("2024-01-03", 3, 30),
    ("2024-01-12", 3, 60),
    ("2024-01-21", 3, 120),
    ("2024-01-26", 3, 30),
    ("2024-01-28", 2, 196),
    ("2024-01-28", 1, 3000),
    ("2024-02-03", 3, 30),
    ("2024-02-12", 3, 60),
    ("2024-02-21", 3, 60),
    ("2024-02-26", 3, 30),
    ("2024-02-28", 1, 3000),
    ("2024-03-03", 3, 30),
    ("2024-03-12", 3, 60),
    ("2024-03-18", 2, 196),
    ("2024-03-21", 3, 90),
    ("2024-03-26", 3, 30),
    ("2024-03-28", 1, 3000),
    ("2024-04-03", 3, 120),
    ("2024-04-12", 3, 60),
    ("2024-04-21", 3, 120),
    ("2024-04-26", 3, 30),
    ("2024-04-28", 2, 196),
    ("2024-04-28", 1, 3000),
    ("2024-05-03", 3, 30),
    ("2024-05-12", 3, 150),
    ("2024-05-21", 3, 120),
    ("2024-05-26", 3, 30),
    ("2024-05-28", 1, 3000),
    ("2024-06-03", 3, 60),
    ("2024-06-12", 3, 60),
    ("2024-06-21", 3, 120),
    ("2024-06-24", 2, 198),
    ("2024-06-26", 3, 30),
    ("2024-06-28", 1, 3000),
    ("2024-07-03", 3, 30),
    ("2024-07-12", 3, 60),
    ("2024-07-21", 3, 90),
    ("2024-07-26", 3, 180),
    ("2024-07-28", 1, 3000),
    ("2024-08-03", 3, 30),
    ("2024-08-12", 3, 30),
    ("2024-08-21", 3, 30),
    ("2024-01-22", 2, 293),
    ("2024-01-24", 2, 196),
    ("2024-08-26", 3, 30),
    ("2024-08-28", 1, 3000),
    ("2024-09-03", 3, 30),
    ("2024-09-12", 3, 60),
    ("2024-09-21", 3, 120),
    ("2024-09-26", 3, 30),
    ("2024-09-28", 1, 3000),
    ("2024-10-03", 3, 30),
    ("2024-10-12", 3, 90),
    ("2024-10-21", 3, 120),
    ("2024-10-26", 3, 30),
    ("2024-10-28", 1, 3000),
    ("2024-11-03", 3, 90),
    ("2024-11-12", 3, 60),
    ("2024-11-21", 3, 120),
    ("2024-11-26", 3, 30),
    ("2024-11-28", 1, 3000),
    ("2024-12-03", 3, 30),
    ("2024-12-12", 3, 90),
    ("2024-12-21", 3, 120),
    ("2024-12-26", 3, 90),
    ("2024-12-28", 1, 3000),
    ("2025-01-03", 3, 30),
    ("2025-01-12", 3, 60),
    ("2025-01-21", 3, 180),
    ("2025-01-28", 2, 196),
    ("2025-01-26", 3, 90),
    ("2025-01-28", 1, 3000),
    ("2025-02-03", 3, 30),
    ("2025-02-12", 3, 60),
    ("2025-02-15", 2, 420),
    ("2025-02-28", 2, 196),
    ("2025-02-28", 2, 255),
    ("2025-02-21", 3, 120),
    ("2025-02-26", 3, 30),
    ("2025-02-28", 1, 3000),
    ("2025-03-24", 3, 60),
    ("2025-03-05", 2, 550),
]
categories = [
    ("Bills",),
    ("Groceries",),
    ("Insurance",),
    ("Leisure",),
    ("Mortgage",),
    ("Other",),
    ("Travel",),
]
goals = [
    ("budget", 780, "weekly"),
    ("budget", 3380, "monthly"),
    ("budget", 32448, "annual"),
    ("net income", 40560, "annual"),
    ("gross income", 50000, "annual"),
]
budgets = [(500, "monthly"), (200, "monthly"), (1000, "monthly"), (200, "weekly")]
budget_category_ids = [2, 4, 5, 7]
sources = [("Salary",), ("Freelance",), ("Teaching",), ("Refund",)]


def populate_tables():
    """This function populates tables in database with dummy data.

    :return: None
    """
    commands = [
        (INSERT_EXPENSE, expenses),
        (INSERT_CATEGORY, categories),
        (INSERT_INCOME, incomes),
        (INSERT_SOURCE, sources),
        (INSERT_GOAL, goals),
    ]

    for _, command in enumerate(commands):
        insert_many(command)

    for index, budget in enumerate(budgets):
        insert_budget(budget_category_ids[index], budget)


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


def insert_many(command):
    """This function inserts a list of data into the database.

    :param command: tuple containing (str, list)
    :return: None
    """
    with get_cursor(True) as cursor:
        cursor.executemany(*command)


def insert_data(string, args):
    """This function inserts data into the database.

    :param string: SQLite command
    :param args: tuple with arguments for command
    :return: None
    """
    with get_cursor(True) as cursor:
        cursor.execute(string, args)


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


def insert_budget(category_id, budget):
    """This function enters a new budget assigned to a category.

    :param category_id: primary key in categories table
    :param budget: tuple containing (amount, term)
    :return: None
    """
    insert_data(INSERT_BUDGET, budget)
    budget_id = fetch_one(MAX_BUDGET_ID)
    insert_data(UPDATE_CATEGORY, (*budget_id, category_id))
