from ui.tests.browser.page.row import Row


class ElementList(object):
    """Represent list of elements."""

    def __init__(self, client, list_class, row_class, row_link_class):
        """
        Initialize list representation.

        :param client:
        :param str list_class:
        :param str row_class:
        :param str row_link_class:
        """
        self.client = client
        self.container = self.client.find_element_by_class_name(list_class)
        self.row_class = row_class
        self.row_link_class = row_link_class

    @property
    def items(self):
        """Read all items on a list."""
        rows = []
        for row in self.container.find_elements_by_class_name(self.row_class):
            rows.append(Row(self.client, row, self.row_link_class))
        return rows
