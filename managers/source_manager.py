"""This module"""

from database.database_commands import fetch_all, insert_data
from user.input import INVALID_INPUT, get_menu_selection

GET_SOURCES = """SELECT id, source FROM source"""
COUNT = """SELECT count(*) FROM source"""
INSERT_SOURCE = """
    INSERT INTO source(source)
    VALUES(?)
"""
UPDATE_SOURCE = """
    UPDATE source
    SET source = ?
    WHERE id = ?
"""


class SourceManager:
    """This class
    """
    table = "category"
    def __init__(self, **kwargs):
        """Constructs attributes for a category."""
        self.id_ = kwargs.setdefault("id", None)
        self.source = kwargs.setdefault("so", None)

    def get_all_atts(self):
        """This"""
        return (self.id_, self.source)

    def get_sources(self):
        """This"""
        source_dict = {}
        rows_list = fetch_all(GET_SOURCES)
        for row in rows_list:
            source_dict[row[0]] = SourceManager(id=row[0], so=row[1])
        return source_dict

    def select_source(self):
        """This"""
        source_dict = self.get_sources()
        self.print_sources()
        while True:
            self.id_ = get_menu_selection(len(source_dict))
            if self.id_ != 0:
                return source_dict[self.id_]
            print(INVALID_INPUT)

    def update_source(self, update):
        """This"""
        insert_data(UPDATE_SOURCE, (update, self.id_))

    def insert_source(self):
        """This"""
        insert_data(INSERT_SOURCE, (self.source,))

    def print_sources(self):
        """This function prints a list of categories.

        :return: None
        """
        source_dict = self.get_sources()
        print("\n\U0001f9fe \033[1mSources: \033[0m\n")

        for (i, source_obj) in source_dict.items():
            if i < 10:
                print(f"{i}.  {source_obj.source}")
            else:
                print(f"{i}. {source_obj.source}")
