# import and class setup:
import unittest
from parameterized import parameterized
from typing import Any, List
from src.professional_file_renamer.filenames_filterer.regex_filename_filterer import RegexFilenameFilterer

class TestRegexFilenameFilterer(unittest.TestCase):

    # Setup Method:
    def setUp(self):
        self.filterer = RegexFilenameFilterer()

    # Test Cases Definition:
    @parameterized.expand([
        ("filter_empty_list", [], r".*\.txt$",[]),
        ("filter_single_file", ["file1.txt"], r".*\.txt$", ["file1.txt"]),
        ("filter_multiple_files", ["file1.txt", "file2.txt", "file3.doc"], r".*\.txt$", ["file1.txt", "file2.txt"]),
        ("filter_multiple_files", ["file1.txt", "goojy.java", "file2.txt", "file3.doc", "poncho.py"], r"file", ["file1.txt", "file2.txt", "file3.doc"]),
        # following test-case will only word with re.search(..) and NOT with re.match(..)
        # ("filter_multiple_files", ["file1.txt", "goojy.java", "file2.txt", "file3.doc", "poncho.py", "ile.poncho"], r"ile",
        #  ["file1.txt", "file2.txt", "file3.doc", "ile.poncho"]),
        # to make it work with re.match(..) we must add .* in the beginning of pattern
        ("filter_multiple_files", ["file1.txt", "goojy.java", "file2.txt", "file3.doc", "poncho.py", "ile.poncho"], r".*ile",
         ["file1.txt", "file2.txt", "file3.doc", "ile.poncho"])
    ])
    # Test method:
    def test_filter_filenames(
            self,
            scenario_name:  str,
            filenames: List[str],
            extension: str,
            expected: List[str]
            ) -> None:
        result = self.filterer.filter_filenames(filenames, extension)
        self.assertEqual(expected, result)
