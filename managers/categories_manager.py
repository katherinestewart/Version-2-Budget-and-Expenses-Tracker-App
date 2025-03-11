"""This module"""

class CategoriesManager:
    """This class manages expenses in the expenses table."""
    def __init__(self, **kwargs):
        self.id_ = kwargs["id"]
        self.description = kwargs["description"]
        self.budget = kwargs["budget"]

    def __str__(self):
        """Constructs a string in a readable format."""
        return self.description

    def get_all_atts(self):
        """Returns all attributes for viewing an expense."""
        id_ = self.id_
        description = self.description
        budget = self.budget.description
        return (id_, description, budget)
