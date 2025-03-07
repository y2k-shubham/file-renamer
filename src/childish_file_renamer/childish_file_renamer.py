import os
from typing import List


class FileRenamer:
    def get_files(self, path: str) -> List[str]:
        # Get a list of all entries in the directory
        entries: List[str] = os.listdir(path)
        # Filter out directories and keep only files
        filenames: List[str] = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
        # os.path.join() creates file paths
        # os.path.isfile() return only directory files not directories
        return filenames

    def filter_files(self, filenames: List[str], extension: str) -> List[str]:
        filtered_files: List[str] = list(filter(lambda filename: filename.endswith(extension), filenames))
        return filtered_files
        # return [filename for filename in filenames if filename.endswith(extension)]

    # def filter_files(self, filenames: List[str], extension: str) -> List[str]:
    #       filtered_files: List[str] = []
    #         for filename in filenames:
    #             if filename.endswith(extension):
    #                 filtered_files.append(filename)
    #         return filtered_files

    def _replace_extension(
            self,
            filename: str,
            old_extension: str,
            new_extension: str) -> str:
        filename_without_extension: str = filename.removesuffix(old_extension)
        filename_with_new_extension: str = f"{filename_without_extension}{new_extension}"
        return filename_with_new_extension

    def rename_files(
            self,
            path: str,
            old_filenames: List[str],
            old_extension: str,
            new_extension: str) -> None:
        for old_filename in old_filenames:
            # prepare path of new file (with updated extension)
            new_filename: str = self._replace_extension(
                filename=old_filename,
                old_extension=old_extension,
                new_extension=new_extension)
            old_file_path: str = os.path.join(path, old_filename)
            new_file_path: str = os.path.join(path, new_filename)
            # Rename the file
            os.rename(src=old_file_path, dst=new_file_path)

    def rename_files_in_directory(
            self,
            path: str,
            old_extension: str,
            new_extension: str) -> None:
        filenames: List[str] = self.get_files(path)
        filtered_filenames: List[str] = self.filter_files(filenames, old_extension)
        self.rename_files(
            path=path,
            old_filenames=filtered_filenames,
            old_extension=old_extension,
            new_extension=new_extension)


if __name__ == '__main__':
    renamer: FileRenamer = FileRenamer()
    renamer.rename_files_in_directory(
        # path="/Users/ykshubhm/Downloads/playground/attempt_1",
        path = "../../playground",
        # old_extension='txt',
        # new_extension='md')
        old_extension='json',
        new_extension='jpeg')

