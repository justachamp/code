
class Row(object):
    """ Object representing campaign row in sidebar """

    def __init__(self, client, element, link_class=None):
        """
        Initialize Row object.

        :param client: a client we operate on
        :param element: element
        :param str link_class: class which indicates click-able row element. Default will be row
        """
        self.client = client
        self.element = element
        self.link = None
        if link_class:
            self.link = self.element.find_element_by_class_name(link_class)

    @property
    def text(self):
        return self.element.text

    def __repr__(self):
        return '<Row: %s>' % self.text

    def click(self):
        """Click on row's element."""
        to_click = self.link or self.element
        return self.client.click(to_click)
