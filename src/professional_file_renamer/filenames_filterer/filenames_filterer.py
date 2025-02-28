
from typing import List
from abc import ABC, abstractmethod

class FilenamesFilterer(ABC):
    @abstractmethod
    def filter_filenames(self, filenames: List[str], extension: str) -> List[str]:
        pass
