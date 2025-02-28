import unittest
from parameterized import parameterized
from typing import Any, List

from src.professional_file_renamer.filenames_filterer.single_extension_filenames_filterer import SingleExtensionFilenamesFilterer


class TestSingleExtensionFileNamesFilterer(unittest.TestCase):
    subject: SingleExtensionFilenamesFilterer

    # setUp
    def setUp(self) -> None:
        self.subject: SingleExtensionFileNamesFilterer = SingleExtensionFileNamesFilterer()

    @parameterized.expand([
        ("test_list_1_extension_1", list(), "pdf"),
        ("test_list_2_extension_1", [], "pdf"),
        ("test_list_1_extension_2", list(), "xml"),
        ("test_list_2_extension_2", [], "xml"),
    ])
    def test_filter_filenames_empty_filenames(
            self,
            scenario_name: str,
            filenames: List[str],
            extension: str) -> None:
        result: List[str] = self.subject.filter_filenames(filenames=filenames, extension=extension)
        self.assertEqual(result, list())


    @parameterized.expand([
        ("test_filenames_empty", [], "json"),
        ("test_filenames_has_one_item", ["test.pdf"], "json"),
        ("test_filenames_has_multiple_items", ["test.md", "test2.txt"], "yaml"),
    ])
    def test_filter_filenames_no_filenames_with_given_extension(
            self,
            scenario_name: str,
            filenames: List[str],
            extension: str) -> None:
        result: List[str] = self.subject.filter_filenames(filenames=filenames, extension=extension)
        self.assertEqual(result, [])


    @parameterized.expand([
        ("test_filenames_has_one_item", ["test.pdf"], "pdf", ["test.pdf"]),
        ("test_filenames_has_multiple_items", ["test.md", "test2.pdf"], "pdf", ["test2.pdf"]),
        ("test_filenames_has_multiple_items", ["test1.pdf", "test.md", "test2.pdf", "my_file.json"], "pdf", ["test1.pdf", "test2.pdf"]),
    ])
    def test_filter_filenames_filenames_with_given_extension(
            self,
            scenario_name: str,
            input_filenames: List[str],
            extension: str,
            expected_filtered_filenames: List[str]) -> None:
        actual_filtered_filenames: List[str] = self.subject.filter_filenames(filenames=input_filenames, extension=extension)
        self.assertEqual(set(expected_filtered_filenames), set(actual_filtered_filenames))
