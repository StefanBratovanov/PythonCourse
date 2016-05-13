import csv


class CatalogEntry:
    def __init__(self, item_id, category_name):
        self.item_id = str(item_id)
        self.category_name = str(category_name)

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, str(self.__dict__))


def load_catalog_by_item_id(filename_catalog):
    with open(filename_catalog) as f:
        catalog = {
            row[0]: CatalogEntry(item_id=row[0], category_name=row[5])
            for row in csv.reader(f)
            }

    return catalog


if __name__ == "__main__":
    pass
