import unittest

from models.Index import Index
from models.OccurrenceList import OccurrenceList
from models.PatriciaTrie import Trie


class PatriciaTrieTests(unittest.TestCase):
    def setUp(self):
        self.__class__.trie = Trie

    def test_1_trie_init(self):
        # Arrange and Act
        trie = self.__class__.trie

        # Assert
        self.assertEqual(trie.key, "#", "Key not set correctly")
        self.assertListEqual(trie.children, list(), "Non empty children assigned")
        self.assertFalse(trie.is_leaf, "Incorrect assignment of leaf node")
        self.assertIsNone(trie.value, "Non none value assigned")

    def test_2_add_single(self):
        # Arrange
        trie = self.__class__.trie

        # Act
        value = OccurrenceList()
        value.append(Index("10011", "Test 1", "www.test1.com", []))
        result = trie.add("bear", value)

        # Assert
        self.assertTrue(result, "Word is not added")
        print(trie)

    def test_3_add_again(self):
        # Arrange
        trie = self.__class__.trie

        # Act
        value = OccurrenceList()
        value.append(Index("10023", "Test 2", "www.test2.com", []))
        result = trie.add("bear", value)

        # Assert
        self.assertTrue(result, "Word is not added")
        print(trie)

    def test_4_add_with_existing_prefix(self):
        # Arrange
        trie = self.__class__.trie

        # Act
        value = OccurrenceList()
        value.append(Index("10041", "Test 3", "www.test3.com", []))
        result = trie.add("bell", value)

        # Assert
        self.assertTrue(result, "Word is not added")
        print(trie)

    def test_5_add_multiple_words(self):
        # Arrange
        trie = self.__class__.trie
        words = ["bear",
                 "bell",
                 "bid",
                 "bull",
                 "buy",
                 "sell",
                 "stock",
                 "stop",
                 "beat",
                 "sea",
                 "stoop"
                 ]

        # Act and Assert
        for i in range(len(words)):
            value = OccurrenceList()
            value.append(Index("1000{0}".format(i), "Test {0}".format(i), "www.test{0}.com".format(i), []))
            result = trie.add(words[i], value)
            self.assertTrue(result, "Word {0} is not added".format(words[i]))

        print(trie)

    def test_6_add_and_search_multiple_words(self):
        # Arrange
        trie = self.__class__.trie
        words = ["bear",
                 "bell",
                 "bid",
                 "bull",
                 "buy",
                 "sell",
                 "stock",
                 "stop",
                 "beat",
                 "belly",
                 "bully",
                 "sea",
                 "stoop",
                 "gamma",
                 "game"
                 ]

        for i in range(len(words)):
            value = OccurrenceList()
            value.append(Index("1000{0}".format(i), "Test {0}".format(i), "www.test{0}.com".format(i), []))
            result = trie.add(words[i], value)
            self.assertTrue(result, "Word {0} is not added".format(words[i]))
        print(trie)

        # Act and Assert
        for i in range(len(words)):
            result = trie.search(words[i])
            self.assertIsNotNone(result, "Word {0} is not found".format(words[i]))
            self.assertTrue(words[i].endswith(result.key), "Suffix not matching with {0}".format(words[i]))
            self.assertTrue(result.value[0].index.endswith(str(i)), "Value suffix not matching with {0}".format(i))

    def test_8_validate_to_dict(self):
        # Arrange
        trie = self.__class__.trie
        words = ["bear",
                 "bell",
                 "bid",
                 "bull",
                 "buy",
                 "sell",
                 "stock",
                 "stop",
                 "beat",
                 "belly",
                 "bully",
                 "sea",
                 "stoop",
                 "gamma",
                 "game"
                 ]

        for i in range(len(words)):
            value = OccurrenceList()
            value.append(Index("1000{0}".format(i), "Test {0}".format(i), "www.test{0}.com".format(i), []))
            result = trie.add(words[i], value)
            self.assertTrue(result, "Word {0} is not added".format(words[i]))

        # Act
        trie_dict = trie.to_dict()

        # Assert
        self.assertIsNotNone(trie_dict, "to_dict returns None")
        self.assertIs(type(trie_dict), type(dict()), "to_dict doesn't return dict")

    def test_9_validate_to_json(self):
        # Arrange
        trie = self.__class__.trie
        words = ["bear",
                 "bell",
                 "bid",
                 "bull",
                 "buy",
                 "sell",
                 "stock",
                 "stop",
                 "beat",
                 "belly",
                 "bully",
                 "sea",
                 "stoop",
                 "gamma",
                 "game"
                 ]

        for i in range(len(words)):
            value = OccurrenceList()
            value.append(Index("1000{0}".format(i), "Test {0}".format(i), "www.test{0}.com".format(i), []))
            result = trie.add(words[i], value)
            self.assertTrue(result, "Word {0} is not added".format(words[i]))

        # Act
        json_string = trie.to_json()

        # Assert
        self.assertIsNotNone(json_string, "to_json returns None")
        self.assertIs(type(json_string), type(str()), "to_json doesn't return string")


if __name__ == '__main__':
    unittest.main()
