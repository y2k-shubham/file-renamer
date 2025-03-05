import os
from unittest import TestCase
from typing import override
from src.professional_file_renamer.rename_applier.simple_rename_applier import SimpleRenameApplier


class TestSimpleRenameApplier(TestCase):
    TEST_DIRECTORY: str = "test_dir"
    TEST_FILE: str = "test_file.txt"

    subject: SimpleRenameApplier

    @override
    def setUp(self):
        self.subject: SimpleRenameApplier = SimpleRenameApplier()
        # create sample test directory and file
        os.mkdir(self.TEST_DIRECTORY)
        open(os.path.join(self.TEST_DIRECTORY, self.TEST_FILE), "w").close()

    @override
    def tearDown(self):
        # delete sample test directory and file
        os.remove(os.path.join(self.TEST_DIRECTORY, self.TEST_FILE))
        os.rmdir(self.TEST_DIRECTORY)

    def test_rename(self):
        self.fail()


