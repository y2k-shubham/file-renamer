from typing import List
from abc import ABC, abstractmethod
import os
from typing import List, override

from src.professional_file_renamer.filenames_filterer.filenames_filterer import FilenamesFilterer

class SingleExtensionFilenamesFilterer(FilenamesFilterer):
    @override
    def filter_filenames(self, filenames: List[str], extension: str) -> List[str]:
        if (not isinstance(extension, str)) or (not extension):
            raise ValueError(f"Invalid extension='{extension}'")
        if not isinstance(filenames, list):
            raise ValueError(f"Invalid filenames='{filenames}'")

        filtered_filenames: List[str] = list(filter(lambda filename: filename.endswith(extension), filenames))
        return filtered_filenames
