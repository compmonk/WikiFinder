import unittest

from models.Index import Index
from models.OccurrenceList import OccurrenceList


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.__class__.index1 = Index(10010,
                                      "Index 1",
                                      "www.index1.com",
                                      OccurrenceList(["www.index2.com",
                                                      "www.index3.com"]))
        self.__class__.index2 = Index(10011,
                                      "Index 2",
                                      "www.index2.com",
                                      OccurrenceList(["www.index1.com",
                                                      "www.index3.com"]))
        self.__class__.index3 = Index(10010,
                                      "Index 3",
                                      "www.index3.com",
                                      OccurrenceList(["www.index1.com",
                                                      "www.index2.com"]))

    def test_1_index_init(self):
        # Arrange and Act
        index1 = self.__class__.index1
        links_to = OccurrenceList(["www.index2.com",
                                   "www.index3.com"])

        # Assert
        self.assertEqual(index1.index, 10010, "Index not assigned correctly")
        self.assertEqual(index1.title, "Index 1", "Title not assigned correctly")
        self.assertEqual(index1.url, "www.index1.com", "URL not assigned correctly")
        self.assertListEqual(index1.links_to, links_to, "links_to not assigned correctly")

    def test_2_less_than_when_smaller(self):
        # Arrange
        index1 = self.__class__.index1
        index2 = self.__class__.index2

        # Act
        result = index1 < index2

        # Assert
        self.assertTrue(result, "__lt__ returns incorrect result")

    def test_3_less_than_when_greater(self):
        # Arrange
        index1 = self.__class__.index1
        index2 = self.__class__.index2

        # Act
        result = index2 < index1

        # Assert
        self.assertFalse(result, "__lt__ returns incorrect result")

    def test_4_great_than_when_greater(self):
        # Arrange
        index1 = self.__class__.index1
        index2 = self.__class__.index2

        # Act
        result = index2 > index1

        # Assert
        self.assertTrue(result, "__gt__ returns incorrect result")

    def test_5_great_than_when_smaller(self):
        # Arrange
        index1 = self.__class__.index1
        index2 = self.__class__.index2

        # Act
        result = index1 > index2

        # Assert
        self.assertFalse(result, "__gt__ returns incorrect result")

    def test_6_equal_to_when_equal(self):
        # Arrange
        index1 = self.__class__.index1
        index3 = self.__class__.index3

        # Act
        result = index1 == index3

        # Assert
        self.assertTrue(result, "__eq__ returns incorrect result")

    def test_7_equal_to_when_not_equal(self):
        # Arrange
        index1 = self.__class__.index1
        index2 = self.__class__.index2

        # Act
        result = index1 == index2

        # Assert
        self.assertFalse(result, "__eq__ returns incorrect result")

    def test_8_not_equal_to_when_not_equal(self):
        # Arrange
        index1 = self.__class__.index1
        index2 = self.__class__.index2

        # Act
        result = index1 != index2

        # Assert
        self.assertTrue(result, "__ne__ returns incorrect result")

    def test_9_not_equal_to_when_equal(self):
        # Arrange
        index1 = self.__class__.index1
        index3 = self.__class__.index3

        # Act
        result = index1 != index3

        # Assert
        self.assertFalse(result, "__eq__ returns incorrect result")


if __name__ == '__main__':
    unittest.main()
