import unittest

from parameterized import parameterized

from src.professional_file_renamer.new_filename_creator.extension_filename_creator import ExtensionFilenameCreator


class MyTestCase(unittest.TestCase):
    subject: ExtensionFilenameCreator

    def setUp(self):
        self.subject: ExtensionFilenameCreator = ExtensionFilenameCreator()

    @parameterized.expand([
        ("test_case_1", "file1.txt", "pdf", "file1.pdf"),
        ("test_case_2", "file.1.txt", "json", "file.1.json"),
        ("test_case_3", "file..1..txt", "json", "file..1..json"),
        ("test_case_3", ".file..1..txt", "yaml", ".file..1..yaml"),
    ])
    def test_get_new_filename(
            self,
            scenario_name: str,
            source_filename_with_extension: str,
            new_extension: str,
            expected_new_filename_with_extension: str) -> None:
        actual_new_filename_with_extension: str = self.subject.get_new_filename(
            source_filename_with_extension,
            new_extension)
        self.assertEqual(expected_new_filename_with_extension, actual_new_filename_with_extension)
