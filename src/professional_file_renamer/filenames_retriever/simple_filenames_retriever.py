import os
from typing import List, override
from src.professional_file_renamer.filenames_retriever.filenames_retriever import FilenamesRetriever

class SimpleFilenamesRetriever(FilenamesRetriever):
    @override
    def get_filenames(self, path: str) -> List[str]:
        if (not isinstance(path, str)) or (not path):
            raise ValueError(f"Invalid path='{path}'")

        try:
            # Get a list of all entries in the directory
            entries: List[str] = os.listdir(path)
            # Filter out directories and keep only files
            # filenames: List[str] = list(filter(lambda entry: os.path.isfile(os.path.join(path, entry)), entries))
            filenames: List[str] = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
            return filenames
        except FileNotFoundError as e:
            print(f"Directory '{path}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
