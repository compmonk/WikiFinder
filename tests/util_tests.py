import unittest

from models.Util import Util


class UtilTests(unittest.TestCase):
    def test_1_get_non_empty_prefix(self):
        # Arrange
        string1 = "hack"
        string2 = "hackathon"
        expected = "hack"

        # Act
        actual = Util.get_prefix(string1, string2)

        # Assert
        self.assertEqual(actual, expected, "Correct non empty prefix not found")

    def test_2_get_empty_prefix(self):
        # Arrange
        string1 = "ack"
        string2 = "hackathon"
        expected = ""

        # Act
        actual = Util.get_prefix(string1, string2)

        # Assert
        self.assertEqual(actual, expected, "Correct empty prefix not found")

    def test_3_has_prefix_if_present(self):
        # Arrange
        string1 = "hack"
        string2 = "hackathon"

        # Act
        result = Util.has_prefix(string1, string2)

        # Assert
        self.assertTrue(result, "Correct prefix not found")

    def test_4_has_prefix_if_absent(self):
        # Arrange
        string1 = "ack"
        string2 = "hackathon"

        # Act
        result = Util.has_prefix(string1, string2)

        # Assert
        self.assertFalse(result, "Correct prefix not found")


if __name__ == '__main__':
    unittest.main()
