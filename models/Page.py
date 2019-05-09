class Page:
    def __init__(self, title, url, text, links_to):
        """
        The web page object containing results
        after scraping a Site
        :param title: The title of the web page
        :param url: The url of the web page
        :param text: The cleaned text body of the web page
        :param links_to: other Page this
        Page points to
        """
        self.title = title
        self.url = url
        self.text = text
        self.links_to = links_to

    def __str__(self):
        return "{0}: {1}".format(self.title[min(len(self.title), 20):],
                                 self.url[min(len(self.url), 20):])
