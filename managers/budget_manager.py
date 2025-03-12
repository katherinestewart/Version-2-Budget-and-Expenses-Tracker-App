"""This module"""


class BudgetManager:
    """This class manages expenses in the expenses table."""
    def __init__(self, **kwargs):
        self.id_ = kwargs["id"]
        self.term = kwargs["term"]
