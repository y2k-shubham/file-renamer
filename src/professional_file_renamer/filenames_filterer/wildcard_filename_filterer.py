from typing import List, override
import fnmatch
from src.professional_file_renamer.filenames_filterer.filenames_filterer import FilenamesFilterer

class WildcardFilenameFilterer(FilenamesFilterer):

    @override
    def filter_filenames(self, filenames: List[str], Extension: str) -> List[str]:
        if (not isinstance(Extension, str)) or (not Extension):
            raise ValueError(f"Invalid wildcard_pattern='{Extension}'")
        if not isinstance(filenames, list):
            raise ValueError(f"Invalid filenames='{filenames}'")

        filtered_filenames: List[str] = fnmatch.filter(filenames, Extension)
        return filtered_filenames


