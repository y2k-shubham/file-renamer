from src.professional_file_renamer.new_filename_creator.filename_creator import FilenameCreator
from typing import override
from typing import List

class ExtensionFilenameCreator(FilenameCreator):
    @override
    def get_new_filename(
            self,
            source_filename: str,
            suffix: str) -> str:
        if (not isinstance(source_filename, str)) or (not source_filename):
            raise ValueError(f"Invalid source_filename='{source_filename}'")
        if (not isinstance(suffix, str)) or (not suffix):
            raise ValueError(f"Invalid suffix='{suffix}'")

        # Splits filename at each dot(.)
        filename_tokens: List[str] = source_filename.split('.')
        filename_tokens_without_extension: List[str] = filename_tokens[:-1]
        filename_without_extension: str = ".".join(filename_tokens_without_extension)
        new_filename: str = f"{filename_without_extension}.{suffix}"
        return new_filename

