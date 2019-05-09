import unittest

from tests.trie_tests import PatriciaTrieTests
from tests.list_tests import OccurrenceListTests
from tests.util_tests import UtilTests
from tests.index_tests import IndexTests

trie_test_suite = unittest.TestLoader().loadTestsFromModule(trie_tests)
list_test_suite = unittest.TestLoader().loadTestsFromModule(list_tests)
utils_test_suite = unittest.TestLoader().loadTestsFromModule(util_tests)
# index_test_suite = unittest.TestLoader().loadTestsFromModule(index_tests)

all_tests = unittest.TestSuite([trie_test_suite, list_test_suite, utils_test_suite])
unittest.TextTestRunner(verbosity=2).run(all_tests)
