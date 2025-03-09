from unittest import TestCase
from src.professional_file_renamer.filenames_retriever.simple_filenames_retriever import SimpleFilenamesRetriever
from parameterized import parameterized
from typing import Any, List

# Class Setup:
class TestSimpleFileNamesRetriever(TestCase):
    subject: SimpleFilenamesRetriever

    def setUp(self) -> None:
        self.subject: SimpleFilenamesRetriever = SimpleFilenamesRetriever()

# Bad Input Tests:
    @parameterized.expand([
        ("test_none", None),
        ("test_empty_string", ""),
        ("test_empty_list", []),
        ("test_non_empty_list", ["puchi"]),
        ("test_float", 56.75),
        ("test_float", -75)
    ])
    def test_get_files_bad_inputs(
            self,
            scenario_name: str,
            path: Any) -> None:
        """
        verify that when get_files(..) function is called with invalid
        input then ValueError is raised
        """
        with self.assertRaises(ValueError) as e:
            self.subject.get_filenames(path=path)
        self.assertEqual(str(e.exception), f"Invalid path='{path}'")

# Success Tests:
#     @parameterized.expand([
#         ("project_root_dir", "..", ["requirements.txt", ".python-version", ".gitignore", "README.md"]),
#         ("test_empty_string", "../src/childish_file_renamer", ["__init__.py", "childish_file_renamer.py"])
#     ])
#     def test_get_files_success_project_root(
#             self,
#             scenario_name: str,
#             path: str,
#             file_names_expected: List[str]) -> None:
#         file_names_computed: List[str] = self.subject.get_filenames(path=path)
#         self.assertEqual(first=set(file_names_expected), second=set(file_names_computed))
