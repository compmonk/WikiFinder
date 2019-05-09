import unittest

from models.Page import Page
from models.OccurrenceList import OccurrenceList


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.__class__.page1 = Page("Page 1",
                                    "www.index1.com",
                                    "This is page number 1",
                                    OccurrenceList(["www.index2.com",
                                                    "www.index3.com"]))
        self.__class__.page2 = Page("Page 2",
                                    "www.index2.com",
                                    "This is page number 2",
                                    OccurrenceList(["www.index1.com",
                                                    "www.index3.com"]))
        self.__class__.page3 = Page("Page 3",
                                    "www.index3.com",
                                    "This is page number 3",
                                    OccurrenceList(["www.index1.com",
                                                    "www.index2.com"]))

    def test_1_page_init(self):
        # Arrange and Act
        page1 = self.__class__.page1
        links_to = OccurrenceList(["www.index2.com",
                                   "www.index3.com"])

        # Assert
        self.assertEqual(page1.title, "Page 1", "Title not assigned correctly")
        self.assertEqual(page1.url, "www.index1.com", "URL not assigned correctly")
        self.assertEqual(page1.text, "This is page number 1", "Text not assigned correctly")
        self.assertListEqual(page1.links_to, links_to, "links_to not assigned correctly")
