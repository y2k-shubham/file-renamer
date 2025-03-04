
from typing import List
from abc import ABC, abstractmethod

class FilenamesRetriever(ABC):
    @abstractmethod
    def get_filenames(self, path: str) -> List[str]:
        pass

# Abstract Base Class (ABC)
# Class Definition:
# class FilenamesRetriever(ABC):
# Method Definition:
#     @abstractmethod
#     def get_filenames(self, path: str) -> List[str]:
#         pass
