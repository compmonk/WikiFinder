class Site:
    def __init__(self, url, html_doc=None):
        """
        A website specifying the url or the
        location of the html doc of the website
        :param url: url of the website
        :param html_doc: location of the
        html_doc of the website
        """
        self.url = url
        self.html_doc = html_doc

    def __str__(self):
        return self.url[:min(len(self.url), 30)]

    def __repr__(self):
        return self.url[:min(len(self.url), 30)]
