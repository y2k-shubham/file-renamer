import os
import shutil
import unittest
from typing import List, override

from parameterized import parameterized

from src.professional_file_renamer.filenames_filterer.filenames_filterer import FilenamesFilterer
from src.professional_file_renamer.filenames_filterer.wildcard_filename_filterer import WildcardFilenameFilterer
from src.professional_file_renamer.filenames_retriever.filenames_retriever import FilenamesRetriever
from src.professional_file_renamer.filenames_retriever.simple_filenames_retriever import SimpleFilenamesRetriever
from src.professional_file_renamer.new_filename_creator.extension_filename_creator import ExtensionFilenameCreator
from src.professional_file_renamer.new_filename_creator.filename_creator import FilenameCreator
from src.professional_file_renamer.professional_file_renamer import ProfessionalFileRenamer
from src.professional_file_renamer.rename_applier.rename_applier import RenameApplier
from src.professional_file_renamer.rename_applier.simple_rename_applier import SimpleRenameApplier


class TestProfessionalRenameApplier(unittest.TestCase):
    TEST_DIR_NAME: str = "test_dir"
    TEST_FILE_NAME_1: str = "test_file_1.txt"
    TEST_FILE_NAME_2: str = "test_file_1.json"
    TEST_FILE_NAMES: List[str] = [TEST_FILE_NAME_1, TEST_FILE_NAME_2]

    subject: ProfessionalFileRenamer

    @override
    def setUp(self) -> None:
        self._create_subject()
        self._create_test_files()

    def _create_subject(self) -> None:
        filenames_retriever: FilenamesRetriever = SimpleFilenamesRetriever()
        filenames_filterer: FilenamesFilterer = WildcardFilenameFilterer()
        filename_creator: FilenameCreator = ExtensionFilenameCreator()
        rename_applier: RenameApplier = SimpleRenameApplier()
        self.subject: ProfessionalFileRenamer = ProfessionalFileRenamer(
            filenames_retriever=filenames_retriever,
            filenames_filterer=filenames_filterer,
            filename_creator=filename_creator,
            rename_applier=rename_applier)

    def _create_test_files(self) -> None:
        # clean up any existing test files
        self.tearDown()
        # create sample test directory and file
        os.mkdir(self.TEST_DIR_NAME)
        #create empty test files
        for test_file_name in TestProfessionalRenameApplier.TEST_FILE_NAMES:
            open(os.path.join(self.TEST_DIR_NAME, test_file_name), "w").close()

    @override
    def tearDown(self) -> None:
        # check if directory exists first
        if os.path.exists(self.TEST_DIR_NAME):
            # use shutil.rmtree to recursively delete the directory and its contents
            shutil.rmtree(self.TEST_DIR_NAME)

    # Test Case Parameters:
    @parameterized.expand([
        ("test_case_1", TEST_DIR_NAME, "*.txt", "json"),
        ("test_case_2", TEST_DIR_NAME, "*.json", "txt"),
    ])
    def test_rename_files_destination_file_already_exists(
            self,
            scenario_name: str,
            path: str,
            from_extension: str,
            to_extension: str) -> None:
        self.subject.rename_files(
            path=path,
            from_extension=from_extension,
            to_extension=to_extension)

        # verify all original test files still exist
        self._validate_no_change_in_file()

    def _validate_no_change_in_file(self) -> None:
        # verify all original test files still exist
        for test_file_name in TestProfessionalRenameApplier.TEST_FILE_NAMES:
            self.assertTrue(os.path.exists(os.path.join(self.TEST_DIR_NAME, test_file_name)))


if __name__ == '__main__':
    unittest.main()
