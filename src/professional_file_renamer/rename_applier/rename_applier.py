
import os
from abc import ABC, abstractmethod

class RenameApplier(ABC):
    @abstractmethod
    def rename(
            self,
            path: str,
            source_filename: str,
            destination_filename: str) -> None:
        pass
