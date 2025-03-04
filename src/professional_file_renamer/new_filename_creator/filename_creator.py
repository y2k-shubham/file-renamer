# Imports:
import os
from abc import ABC, abstractmethod
# Class Definition:
class FilenameCreator(ABC):
# Abstract Method:
    @abstractmethod
    def get_new_filename(
            self,
            source_filename: str,
            suffix: str) -> str:
        pass
