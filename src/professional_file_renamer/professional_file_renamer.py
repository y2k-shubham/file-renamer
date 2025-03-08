import os

from src.professional_file_renamer.filenames_retriever.filenames_retriever import FilenamesRetriever
from src.professional_file_renamer.filenames_retriever.simple_filenames_retriever import SimpleFilenamesRetriever
from src.professional_file_renamer.filenames_filterer.filenames_filterer import FilenamesFilterer
# from src.professional_file_renamer.filenames_filterer.single_extension_filenames_filterer import SingleExtensionFilenamesFilterer
from src.professional_file_renamer.filenames_filterer.wildcard_filename_filterer import WildcardFilenameFilterer
from src.professional_file_renamer.new_filename_creator.filename_creator import FilenameCreator
from src.professional_file_renamer.new_filename_creator.extension_filename_creator import ExtensionFilenameCreator
from src.professional_file_renamer.rename_applier.rename_applier import RenameApplier
from src.professional_file_renamer.rename_applier.simple_rename_applier import SimpleRenameApplier
from typing import List

class ProfessionalFileRenamer:

    _filenames_retriever: FilenamesRetriever
    _filenames_filterer: FilenamesFilterer
    _filename_creator: FilenameCreator
    _rename_applier: RenameApplier

    # constructor that accepts all members and assigns them
    def __init__(
            self,
            filenames_retriever: FilenamesRetriever,
            filenames_filterer: FilenamesFilterer,
            filename_creator: FilenameCreator,
            rename_applier: RenameApplier):
        self._filenames_retriever = filenames_retriever
        self._filenames_filterer = filenames_filterer
        self._filename_creator = filename_creator
        self._rename_applier = rename_applier


    # renames all files in the given path
    def rename_files(
            self,
            path: str,
            from_extension: str,
            to_extension: str) -> None:
        filenames: List[str] = self._filenames_retriever.get_filenames(path=path)
        filtered_filenames: List[str] = self._filenames_filterer.filter_filenames(filenames=filenames, extension=from_extension)
        for filename in filtered_filenames:
            new_filename: str = self._filename_creator.get_new_filename(source_filename=filename, suffix=to_extension) # Create new filename
            self._rename_applier.rename(path=path, source_filename=filename, destination_filename=new_filename)  # Perform rename

if __name__ == '__main__':
    print(f"Current directory is {os.path.abspath(os.curdir)}")
    filenames_retriever: FilenamesRetriever = SimpleFilenamesRetriever()
    filenames_filterer: FilenamesFilterer = WildcardFilenameFilterer()
    filename_creator: FilenameCreator = ExtensionFilenameCreator()
    rename_applier: RenameApplier = SimpleRenameApplier()

    renamer: ProfessionalFileRenamer = ProfessionalFileRenamer(
        filenames_retriever=filenames_retriever,
        filenames_filterer=filenames_filterer,
        filename_creator=filename_creator,
        rename_applier=rename_applier)

    path: str = input("Enter the path of the directory: ")
    from_extension: str = input("Enter the extension of the files to be renamed: ")
    to_extension: str = input("Enter the extension of the files after renaming: ")

    renamer.rename_files(path=path, from_extension=from_extension, to_extension=to_extension)
