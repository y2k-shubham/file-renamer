import os
from parameterized import parameterized
from unittest import TestCase
from typing import override
from src.professional_file_renamer.rename_applier.simple_rename_applier import SimpleRenameApplier


class TestSimpleRenameApplier(TestCase):
    TEST_DIR_NAME: str = "test_dir"
    TEST_FILE_NAME: str = "test_file.txt"

    subject: SimpleRenameApplier

    @override
    def setUp(self):
        self.subject: SimpleRenameApplier = SimpleRenameApplier()
        # create sample test directory and file
        os.mkdir(self.TEST_DIR_NAME)
        open(os.path.join(self.TEST_DIR_NAME, self.TEST_FILE_NAME), "w").close()

    @override
    def tearDown(self):
        # delete sample test directory and file
        os.remove(os.path.join(self.TEST_DIR_NAME, self.TEST_FILE_NAME))
        os.rmdir(self.TEST_DIR_NAME)

    @parameterized.expand([
        ("test_case_1", "non_existent_directory", "file1.txt", "file1.txt"),
        ("test_case_2", "non_existent_directory", "file2.png", "file2.png"),
    ])
    def test_rename_file_source_and_destination_filenames_are_same(
            self,
            scenario_name: str,
            path: str,
            source_filename: str,
            dest_filename: str) -> None:
        self.subject.rename(path, source_filename, dest_filename)
        self._validate_no_change_in_file()

    def _validate_no_change_in_file(self) -> None:
        self.assertTrue(os.path.exists(os.path.join(self.TEST_DIR_NAME, self.TEST_FILE_NAME)))

    @parameterized.expand([
        ("test_case_1", "invalid_directory", TEST_FILE_NAME, "file1.txt"),
        ("test_case_2", TEST_DIR_NAME, "file1.puchi", "file2.png"),
    ])
    def test_rename_file_source_file_does_not_exist(
            self,
            scenario_name: str,
            path: str,
            source_filename: str,
            dest_filename: str) -> None:

        with self.assertRaises(FileNotFoundError) as e:
            self.subject.rename(path=path, source_filename=source_filename,destination_filename=dest_filename)
        source_filepath: str = os.path.join(path, source_filename)
        self.assertEqual(str(e.exception), f"Source file does not exist: '{source_filepath}'")

        self._validate_no_change_in_file()
