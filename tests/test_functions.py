import unittest
from io import StringIO
import src.functions as functions


class TestFunctions(unittest.TestCase):
    def test_write_to_file(self):
        # complete test 
        out = StringIO()
        functions.write_to_file(["one", "two", "three", "four"], out)
        self.assertEqual(out.getvalue(), "1 one\n2 two\n3 three\n4 four\n")

    def test_merge_files(self):
        # complete test
        f1 = StringIO("cat\ndog\npig\n")
        f2 = StringIO("rabbit\nhorse\nmouse\n")
        out = StringIO()
        functions.merge_files(f1, f2, out)
        self.assertEqual(out.getvalue(), "cat,rabbit\ndog,horse\npig,mouse\n")

    def test_key_in_value(self):
        # incomplete test
        d = {"a": ["b", "c", "a"],
             "b": ["a", "c"],
             "c": ["c"],
             "d": ["c", "d"],
             "e": []}
        answer = set(("a", "c", "d"))
        result = functions.key_in_value(d)
        # two checks are required:
        # 1) does the results contain the right number of values?
        # 2) is the result the same as the answer?
        self.fail("No checks in test") # get rid of this after you've written your tests

    def test_most_common_letters(self):
        # incomplete test
        str_to_test = "abb bbdddc cdcdc"
        self.fail("No checks in test")        

    def test_merge_dictionaries(self):
        # incomplete test
        d1 = {"a": 3, "b": 9, "c": 4}
        d1_copy = d1.copy()
        d2 = {"b": 12, "c": 11, "d": 2, "e": 5}
        d2_copy = d2.copy()
        # three checks are required:
        # 1) was d1 changed?
        # 2) was d2 changes?
        # 3) is the result you get after the merger correct?
        self.fail("No checks in test")  # get rid of this after you've written your tests

if __name__ == '__main__':
    unittest.main()
