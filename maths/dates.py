"""This module"""

from datetime import date
from dateutil.relativedelta import relativedelta


def get_first_of_month():
    """This function"""
    today = date.today()
    first_of_month = today.replace(day=1)

    return first_of_month


def get_three_months_ago():
    """This function"""
    today = date.today()
    day = today - relativedelta(months=3)
    day = day.replace(day=1)

    return day


def get_six_months_ago():
    """This function"""
    today = date.today()
    day = today - relativedelta(months=6)
    day = day.replace(day=1)

    return day


def get_one_year_ago():
    """This function"""
    today = date.today()
    day = today - relativedelta(months=12)
    day = day.replace(day=1)

    return day
