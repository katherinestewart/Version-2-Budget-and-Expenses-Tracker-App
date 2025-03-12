"""This module"""


from managers.table_manager import TableManager as tm
from user.input import get_menu_selection


class Category:
    """This class
    """

    def __init__(self, id_, description, budget_id):
        """Constructs attributes for a category."""
        self.id_ = id_
        self.description = description
        self.budget = budget_id


def get_categories():
    """This"""
    return tm(table1="categories", description="category").get_descriptions()


def select_category():
    """This"""
    print_categories()
    id_ = get_menu_selection(*tm(table1 = "categories").count_rows())
    return Category(*tm(table1="categories", id_=id_).get_row_from_id())


def print_categories():
    """This function prints a list of categories.

    :return: None
    """
    category_list = get_categories()
    print("\n\U0001f9fe \033[1mCategories: \033[0m\n")

    for i, category in enumerate(category_list):
        if i + 1 < 10:
            print(f"{i+1}.  {category[0]}")
        else:
            print(f"{i+1}. {category[0]}")
