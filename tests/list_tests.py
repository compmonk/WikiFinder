import unittest
from models.OccurrenceList import OccurrenceList
from models.Index import Index


class OccurrenceListTests(unittest.TestCase):
    def setUp(self):
        self.__class__.occurrence_list = OccurrenceList()
        self.__class__.occurrence_list1 = OccurrenceList()
        self.__class__.occurrence_list2 = OccurrenceList()

    def test_01_check_non_empty(self):
        # Arrange
        occurrence_list = self.__class__.occurrence_list

        # Act
        occurrence_list.append(Index("20019", "Test 1", "www.test.com", list()))

        # Assert
        self.assertEqual(occurrence_list[0].index, "20019", "index not set correctly")
        self.assertEqual(occurrence_list[0].url, "www.test.com", "url not set correctly")
        self.assertListEqual(occurrence_list[0].links_to, list(), "links_to not set correctly")

    def test_02_union_two_elements(self):
        # Arrange
        occurrence_list1 = self.__class__.occurrence_list1
        occurrence_list1.append(Index("20019", "Test 1", "www.test1.com", ["www.test2.com"]))

        occurrence_list2 = self.__class__.occurrence_list2
        occurrence_list2.append(Index("20020", "Test 2", "www.test2.com", ["www.test1.com"]))

        # Act
        occurrence_list = occurrence_list1.union(occurrence_list2)

        # Assert
        self.assertEqual(occurrence_list[0].index, "20019", "index not merged correctly")
        self.assertEqual(occurrence_list[0].url, "www.test1.com", "url not merged correctly")
        self.assertListEqual(occurrence_list[0].links_to, ["www.test2.com"], "links_to not merged correctly")

        self.assertEqual(occurrence_list[1].index, "20020", "index not merged correctly")
        self.assertEqual(occurrence_list[1].url, "www.test2.com", "url not merged correctly")
        self.assertListEqual(occurrence_list[1].links_to, ["www.test1.com"], "links_to not merged correctly")

        self.assertEqual(2, len(occurrence_list), "Multiple elements added")

    def test_03_union_four_elements(self):
        # Arrange
        occurrence_list1 = self.__class__.occurrence_list1
        occurrence_list1.append(Index("20019", "Test 1", "www.test1.com", ["www.test2.com"]))
        occurrence_list1.append(Index("20020", "Test 1", "www.test1.com", ["www.test4.com"]))
        occurrence_list1.append(Index("20021", "Test 1", "www.test1.com", ["www.test4.com"]))

        occurrence_list2 = self.__class__.occurrence_list2
        occurrence_list2.append(Index("20020", "Test 2", "www.test2.com", ["www.test3.com"]))
        occurrence_list2.append(Index("20020", "Test 2", "www.test2.com", ["www.test3.com"]))
        occurrence_list2.append(Index("20021", "Test 2", "www.test2.com", ["www.test3.com"]))
        occurrence_list2.append(Index("20022", "Test 2", "www.test2.com", ["www.test1.com"]))

        # Act
        occurrence_list = occurrence_list1.union(occurrence_list2)

        # Assert
        self.assertEqual("20019", occurrence_list[0].index, "index not merged correctly")
        self.assertEqual("www.test1.com", occurrence_list[0].url, "url not merged correctly")
        self.assertListEqual(["www.test2.com"], occurrence_list[0].links_to, "links_to not merged correctly")

        self.assertEqual("20020", occurrence_list[1].index, "index not merged correctly")
        self.assertEqual("www.test1.com", occurrence_list[1].url, "url not merged correctly")
        self.assertListEqual(["www.test4.com"], occurrence_list[1].links_to, "links_to not merged correctly")

        self.assertEqual("20021", occurrence_list[2].index, "index not merged correctly")
        self.assertEqual("www.test1.com", occurrence_list[2].url, "url not merged correctly")
        self.assertListEqual(["www.test4.com"], occurrence_list[2].links_to, "links_to not merged correctly")

        self.assertEqual("20022", occurrence_list[3].index, "index not merged correctly")
        self.assertEqual("www.test2.com", occurrence_list[3].url, "url not merged correctly")
        self.assertListEqual(["www.test1.com"], occurrence_list[3].links_to, "links_to not merged correctly")

        self.assertEqual(4, len(occurrence_list), "Multiple elements added")

    def test_04_intersect_two_common_elements(self):
        # Arrange
        occurrence_list1 = self.__class__.occurrence_list1
        occurrence_list1.append(Index("20019", "Test 1", "www.test1.com", ["www.test2.com"]))

        occurrence_list2 = self.__class__.occurrence_list2
        occurrence_list2.append(Index("20019", "Test 1", "www.test2.com", ["www.test3.com"]))

        # Act
        occurrence_list = occurrence_list1.intersect(occurrence_list2)

        # Assert
        self.assertEqual("20019", occurrence_list[0].index, "index not merged correctly")
        self.assertEqual(1, len(occurrence_list), "Improperly intersected")

    def test_05_intersect_two_uncommon_elements(self):
        # Arrange
        occurrence_list1 = self.__class__.occurrence_list1
        occurrence_list1.append(Index("20019", "Test 1", "www.test1.com", ["www.test2.com"]))

        occurrence_list2 = self.__class__.occurrence_list2
        occurrence_list2.append(Index("20020", "Test 2", "www.test2.com", ["www.test3.com"]))

        # Act
        occurrence_list = occurrence_list1.intersect(occurrence_list2)

        # Assert
        self.assertEqual(0, len(occurrence_list), 0, "Improperly intersected")
        self.assertListEqual(OccurrenceList(), occurrence_list, "non emtpy list returned")

    def test_06_intersect_different_object(self):
        # Arrange
        occurrence_list1 = self.__class__.occurrence_list1
        occurrence_list1.append(Index("20019", "Test 1", "www.test1.com", ["www.test2.com"]))
        occurrence_list1.append(Index("20020", "Test 1", "www.test1.com", ["www.test3.com"]))
        occurrence_list1.append(Index("20021", "Test 1", "www.test1.com", ["www.test3.com"]))

        occurrence_list2 = self.__class__.occurrence_list2
        occurrence_list2.append(Index("20019", "Test 2", "www.test2.com", ["www.test2.com"]))
        occurrence_list2.append(Index("20019", "Test 2", "www.test2.com", ["www.test2.com"]))
        occurrence_list2.append(Index("20022", "Test 2", "www.test2.com", ["www.test1.com"]))

        # Act
        occurrence_list = occurrence_list1.intersect(occurrence_list2)

        # Assert
        self.assertEqual("20019", occurrence_list[0].index, "index not merged correctly")
        self.assertEqual("www.test1.com", occurrence_list[0].url, "index not merged correctly")
        self.assertEqual(1, len(occurrence_list), "Improperly intersected")

    def test_07_intersect_different_element(self):
        # Arrange
        occurrence_list1 = self.__class__.occurrence_list1
        occurrence_list1.append(0)
        occurrence_list1.append(1)
        occurrence_list1.append(2)

        occurrence_list2 = self.__class__.occurrence_list2
        occurrence_list2.append(0)
        occurrence_list2.append(0)
        occurrence_list2.append(3)

        # Act
        occurrence_list = occurrence_list1.intersect(occurrence_list2)

        # Assert
        self.assertEqual(0, occurrence_list[0], "index not merged correctly")
        self.assertEqual(1, len(occurrence_list), "Improperly intersected")

    def test_08_index_of_object_present(self):
        # Arrange
        occurrence_list = self.__class__.occurrence_list
        occurrence_list.append(1234)
        occurrence_list.append(1235)
        occurrence_list.append(1236)

        # Act
        index1 = occurrence_list.index_of(1234)
        index2 = occurrence_list.index_of(1235)
        index3 = occurrence_list.index_of(1236)

        # Assert
        self.assertEqual(0, index1, "index_of produces incorrect result when value is present")
        self.assertEqual(1, index2, "index_of produces incorrect result when value is present")
        self.assertEqual(2, index3, "index_of produces incorrect result when value is present")

    def test_09_index_of_object_present(self):
        # Arrange
        occurrence_list = self.__class__.occurrence_list
        occurrence_list.append(1234)
        occurrence_list.append(1235)
        occurrence_list.append(1236)

        # Act
        index1 = occurrence_list.index_of(1231)
        index2 = occurrence_list.index_of(1232)
        index3 = occurrence_list.index_of(1233)

        # Assert
        self.assertEqual(-1, index1, "index_of produces incorrect result when value is absent")
        self.assertEqual(-1, index2, "index_of produces incorrect result when value is absent")
        self.assertEqual(-1, index3, "index_of produces incorrect result when value is absent")

    def test_10_index_of_object_present(self):
        # Arrange
        occurrence_list = self.__class__.occurrence_list
        occurrence_list.append(Index(20019, "Test 1", "www.test1.com", ["www.test2.com"]))
        occurrence_list.append(Index(20020, "Test 2", "www.test2.com", ["www.test3.com"]))
        occurrence_list.append(Index(20021, "Test 2", "www.test2.com", ["www.test3.com"]))

        # Act
        index1 = occurrence_list.index_of(20019, attr="index")
        index2 = occurrence_list.index_of(20020, attr="index")
        index3 = occurrence_list.index_of(20021, attr="index")

        # Assert
        self.assertEqual(0, index1, "index_of produces incorrect result when object is present")
        self.assertEqual(1, index2, "index_of produces incorrect result when object is present")
        self.assertEqual(2, index3, "index_of produces incorrect result when object is present")

    def test_11_index_of_object_absent(self):
        # Arrange
        occurrence_list = self.__class__.occurrence_list
        occurrence_list.append(Index(20019, "Test 1", "www.test1.com", ["www.test2.com"]))
        occurrence_list.append(Index(20020, "Test 2", "www.test2.com", ["www.test3.com"]))
        occurrence_list.append(Index(20021, "Test 2", "www.test2.com", ["www.test3.com"]))

        # Act
        index1 = occurrence_list.index_of(20022, attr="index")
        index2 = occurrence_list.index_of(20023, attr="index")
        index3 = occurrence_list.index_of(20024, attr="index")

        # Assert
        self.assertEqual(-1, index1, "index_of produces incorrect result when object is absent")
        self.assertEqual(-1, index2, "index_of produces incorrect result when object is absent")
        self.assertEqual(-1, index3, "index_of produces incorrect result when object is absent")


if __name__ == '__main__':
    unittest.main()
