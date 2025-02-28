
import os
from abc import ABC, abstractmethod

class FilenameCreator(ABC):
    @abstractmethod
    def get_new_filename(
            self,
            source_filename: str,
            suffix: str) -> str:
        pass
