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
        ("filter_txt_files",["test.txt", "sample.doc", "data.txt"],r".*\.txt$",["test.txt", "data.txt"]),
        ("filter_empty_list", [], r".*\.txt$",[]),
        ("filter_single_file", ["file1.txt"], r".*\.txt$", ["file1.txt"]),
        ("filter_multiple_files", ["file1.txt", "file2.txt", "file3.doc"], r".*\.txt$", ["file1.txt", "file2.txt"])
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
        self.assertEqual(result, expected)


