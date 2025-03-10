import os
import shutil
from parameterized import parameterized
from unittest import TestCase
from typing import override, List
from src.professional_file_renamer.rename_applier.simple_rename_applier import SimpleRenameApplier

# Class Constants:
class TestSimpleRenameApplier(TestCase):
    TEST_DIR_NAME: str = "test_dir"
    TEST_FILE_NAME_1: str = "test_file_1.txt"
    TEST_FILE_NAME_2: str = "test_file_2.json"
    TEST_FILE_NAMES: List[str] = [TEST_FILE_NAME_1, TEST_FILE_NAME_2]

    # Subject Declaration:
    subject: SimpleRenameApplier

    # Setup Method:
    @override
    def setUp(self):
        # create new instance of the class under test
        self.subject: SimpleRenameApplier = SimpleRenameApplier()
        # clean up any existing test files
        self.tearDown()
        # create sample test directory and file
        os.mkdir(self.TEST_DIR_NAME)
        #create empty test files
        for test_file_name in TestSimpleRenameApplier.TEST_FILE_NAMES:
            open(os.path.join(self.TEST_DIR_NAME, test_file_name), "w").close()
        # for test_file_name in TestSimpleRenameApplier.TEST_FILE_NAMES:
        #     # Builds full path: test_dir/test_file_1.txt
        #     full_path = os.path.join(self.TEST_DIR_NAME, test_file_name)
        #     # Creates empty file and closes it immediately
        #     open(full_path, "w").close()

    @override
    def tearDown(self):
        # delete sample test directory and file
        # os.remove(os.path.join(self.TEST_DIR_NAME, self.TEST_FILE_NAME))
        # os.rmdir(self.TEST_DIR_NAME)

        # check if directory exists first
        if os.path.exists(self.TEST_DIR_NAME):
            # use shutil.rmtree to recursively delete the directory and its contents
            shutil.rmtree(self.TEST_DIR_NAME)

    # Test Case Parameters:
    @parameterized.expand([
        ("test_case_1", "non_existent_directory", "file1.txt", "file1.txt"),
        ("test_case_2", "non_existent_directory", "file2.png", "file2.png"),
    ])
    # Test Method:
    def test_rename_file_source_and_destination_filenames_are_same(
            self,
            scenario_name: str,
            path: str,
            source_filename: str,
            dest_filename: str) -> None:
        # Attempt rename
        self.subject.rename(path, source_filename, dest_filename)
        # Validate no changes occurred
        self._validate_no_change_in_file()

    @parameterized.expand([
        ("test_case_1", "invalid_directory", TEST_FILE_NAME_1, "file1.txt"),
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

    @parameterized.expand([
        ("test_case_1", TEST_DIR_NAME, TEST_FILE_NAME_2, TEST_FILE_NAME_1),
        ("test_case_2", TEST_DIR_NAME, TEST_FILE_NAME_1, TEST_FILE_NAME_2),
    ])
    def test_rename_file_destination_file_already_exists(
            self,
            scenario_name: str,
            path: str,
            source_filename: str,
            dest_filename: str) -> None:

        with self.assertRaises(FileExistsError) as e:
            self.subject.rename(path=path, source_filename=source_filename, destination_filename=dest_filename)
        dest_filepath: str = os.path.join(path, dest_filename)
        self.assertEqual(str(e.exception), f"Destination file already exists: '{dest_filepath}'")

        self._validate_no_change_in_file()

    @parameterized.expand([
        ("test_case_1", TEST_DIR_NAME, TEST_FILE_NAME_1, "new_file_name_1.md", [TEST_FILE_NAME_2]),
        ("test_case_2", TEST_DIR_NAME, TEST_FILE_NAME_2, "new_file_name_2.xml", [TEST_FILE_NAME_1]),
    ])
    def test_rename_file_happy_case(
            self,
            scenario_name: str,
            path: str,
            source_filename: str,
            dest_filename: str,
            unchanged_filenames: List[str]) -> None:
        # perform rename operation
        self.subject.rename(path=path, source_filename=source_filename, destination_filename=dest_filename)
        # create list of expected files
        new_filenames: List[str] = [dest_filename] + unchanged_filenames
        # validate file exist
        self._validate_files_exist(filenames=new_filenames)

    def _validate_no_change_in_file(self) -> None:
        # verify all original test files still exist
        for test_file_name in TestSimpleRenameApplier.TEST_FILE_NAMES:
            self.assertTrue(os.path.exists(os.path.join(self.TEST_DIR_NAME, test_file_name)))

    def _validate_files_exist(self, filenames: List[str]) -> None:
        # verify specific files exists
        for filename in filenames:
            self.assertTrue(os.path.isfile(os.path.join(TestSimpleRenameApplier.TEST_DIR_NAME, filename)))
