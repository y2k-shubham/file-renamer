from src.professional_file_renamer.rename_applier.rename_applier import RenameApplier
import os
import logging


class SimpleRenameApplier(RenameApplier):
    def rename(
            self,
            path: str,
            source_filename: str,
            destination_filename: str) -> None:
        if (not isinstance(path, str)) or (not path):
            raise ValueError(f"Invalid path='{path}'")
        if (not isinstance(source_filename, str)) or (not source_filename):
            raise ValueError(f"Invalid source_filename='{source_filename}'")
        if (not isinstance(destination_filename, str)) or (not destination_filename):
            raise ValueError(f"Invalid destination_filename='{destination_filename}'")

        source_path: str = os.path.join(path, source_filename)
        destination_path: str = os.path.join(path, destination_filename)

        # Check if filenames are identical
        if source_filename == destination_filename:
            logging.warning(
                f"Source and destination filenames are identical: '{source_filename}'. "
                "No action needed."
            )
            return

        # Check if source file does not exist
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file does not exist: '{source_path}'")

        # Check if destination file already exists
        if os.path.exists(destination_path):
            raise FileExistsError(f"Destination file already exists: '{destination_path}'")

        os.rename(source_path, destination_path)