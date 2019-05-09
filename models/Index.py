class Index:
    def __init__(self, index, title, url, links_to):
        """
        The Index is like a unique
        node in the www, each web
        page is a node in the www.
        The Index is same as the Page,
        except Page is more bound to the web page
        containing the text of the web page,
        while Index stores the location of the
        node in the www
        :param index: Index of the node in the www
        :param title: Title of the web page
        of this node
        :param url: URL of the web page or node
        :param links_to: other Index this
        node points to
        """
        self.index = index
        self.title = title
        self.url = url
        self.links_to = links_to

    def __str__(self):
        return "{0}\n{1}".format(self.title[:min(len(self.title), 50)], self.url[:min(len(self.url), 50)])

    def __repr__(self):
        return "{0} ({1} : {2})".format(self.index, self.title[:min(len(self.title), 30)], len(self.links_to))

    def __lt__(self, other):
        return self.index < other.index

    def __le__(self, other):
        return self.index <= other.index

    def __eq__(self, other):
        return self.index == other.index

    def __ne__(self, other):
        return self.index != other.index

    def __gt__(self, other):
        return self.index > other.index

    def __ge__(self, other):
        return self.index >= other.index
