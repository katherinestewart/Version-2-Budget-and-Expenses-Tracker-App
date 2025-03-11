"""This module"""


class ExpensesManager:
    """This class manages expenses in the expenses table."""
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.date = kwargs["date"]
        self.description = kwargs["description"]
        self.amount = kwargs["amount"]
        self.category = kwargs["category"]

    def __str__(self):
        """Constructs a string in a readable format."""

    def get_all_atts(self):
        """Returns all attributes for viewing an expense."""
        date = self.date
        description = self.description
        amount = self.amount
        category_description = self.category.description
        return (date, description, amount, category_description)
