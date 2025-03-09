import unittest
import os
from parameterized import parameterized
from typing import Any, List
import fnmatch

from professional_file_renamer.filenames_filterer.wildcard_filename_filterer import WildcardFilenameFilterer


class TestFilenamesFilterer(unittest.TestCase):

    def setUp(self) -> None:
        self.filterer = WildcardFilenameFilterer()

    @parameterized.expand([
        ("wildcard_txt_files", ["test.txt", "doc.txt", "image.png"], "*.txt", ["test.txt", "doc.txt"]),
        ("single_char_pattern", ["a.txt", "ab.txt", "abc.txt"], "?.txt", ["a.txt"]),
        ("Complex_pattern", ["a.txt", "ab.txt", "abc.txt"], "??.txt", ["ab.txt"]),
        ("empty_input", [], "*.txt", []),
        ("character_set", ["file1.txt", "fileA.txt", "file_.txt"],"file[0-9].txt",["file1.txt"])
    ])
    def test_filter_filenames(
            self,
            scenario: str,
            filenames: List[str],
            extension: str,
            expected: List[str]) -> None:
        result = self.filterer.filter_filenames(filenames, extension)
        self.assertEqual(result, expected)


