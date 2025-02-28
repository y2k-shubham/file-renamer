from typing import List
from abc import ABC, abstractmethod
import os
from typing import List, override

from src.professional_file_renamer.filenames_filterer.filenames_filterer import FilenamesFilterer

class MultiExtensionFilenamesFilterer(FilenamesFilterer):
    @override
    def filter_filenames(self, filenames: List[str], extension: str) -> List[str]:
        """
        :param filenames: list of file names to be filtered via extensions
        :param extension: list of comma-separated extensions, eg. txt,json,xml
        :return:
        """
        if (not isinstance(extension, str)) or (not extension):
            raise ValueError(f"Invalid extension='{extension}'")
        if not isinstance(filenames, list):
            raise ValueError(f"Invalid filenames='{filenames}'")

        extensions: List[str] = extension.split(",")
        filtered_filenames: List[List[str]] = []
        for single_extension in extensions:
            filtered_filenames.append(list(filter(lambda filename: filename.endswith(single_extension), filenames)))

        return [filename for sublist in filtered_filenames for filename in sublist]
