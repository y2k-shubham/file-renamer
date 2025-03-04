# Imports:
from typing import List # For type hints
from abc import ABC, abstractmethod # For creating abstract class

# Abstract Class Definition:
class FilenamesFilterer(ABC):
# Abstract Method:
    @abstractmethod
    def filter_filenames(self, filenames: List[str], extension: str) -> List[str]:
        pass
