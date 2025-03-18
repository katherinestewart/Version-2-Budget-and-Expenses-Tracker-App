"""This module"""

from database.database_commands import fetch_all, insert_data
from user.input import get_menu_selection

GET_CATEGORIES = """SELECT id, category FROM category"""
COUNT = """SELECT count(*) FROM category"""
INSERT_CATEGORY = """
    INSERT INTO category(category)
    VALUES(?)
"""
UPDATE_CATEGORY = """
    UPDATE category
    SET category = ?
    WHERE id = ?
"""


class CategoryManager:
    """This class
    """
    table = "category"
    def __init__(self, **kwargs):
        """Constructs attributes for a category."""
        self.id_ = kwargs.setdefault("id", None)
        self.category = kwargs.setdefault("ca", None)
        self.budget = kwargs.setdefault("bu", None)

    def get_all_atts(self):
        """This"""
        return (self.id_, self.category, self.budget)

    def get_categories(self):
        """This"""
        category_dict = {}
        rows_list = fetch_all(GET_CATEGORIES)
        for row in rows_list:
            category_dict[row[0]] = CategoryManager(id=row[0], ca=row[1])
        return category_dict

    def select_category(self):
        """This"""
        category_dict = self.get_categories()
        self.print_categories()
        self.id_ = get_menu_selection(len(category_dict))
        return category_dict[self.id_]

    def update_category(self, update):
        """This"""
        insert_data(UPDATE_CATEGORY, (update, self.id_))

    def insert_category(self):
        """This"""
        insert_data(INSERT_CATEGORY, (self.category,))

    def print_categories(self):
        """This function prints a list of categories.

        :return: None
        """
        category_dict = self.get_categories()
        print("\n\U0001f9fe \033[1mCategories: \033[0m\n")

        for (i, category_obj) in category_dict.items():
            if i+1 < 10:
                print(f"{i}.  {category_obj.category}")
            else:
                print(f"{i}. {category_obj.category}")
