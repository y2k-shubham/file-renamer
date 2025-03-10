from typing import List, override
import re
from src.professional_file_renamer.filenames_filterer.filenames_filterer import FilenamesFilterer

class RegexFilenameFilterer(FilenamesFilterer):

    @override
    def filter_filenames(self, filenames: List[str], extension: str) -> List[str]:

        if (not isinstance(extension, str)) or (not extension):
            raise ValueError(f"Invalid regex_pattern='{extension}'")
        if not isinstance(filenames, list):
            raise ValueError(f"Invalid filenames='{filenames}'")

        # filtered_filenames: List[str] = []
        # for filename in filenames:
        #     if re.match(extension, filename):
        #         filtered_filenames.append(filename)
        filtered_filenames: List[str] =  list(filter(lambda filename: re.match(extension, filename), filenames))
        # filtered_filenames:  List[str] = [filename for filename in filenames if re.match(extension, filename)]
        return filtered_filenames


    # re.match() looks for pattern at start of string
    # re.search() to find pattern anywhere in string









