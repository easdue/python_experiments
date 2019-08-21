from abc import ABC
from enum import Enum


class CffiDeviceReader(ABC):
    class ResourceNotAllocated(Exception):
        """Exception thrown when trying to free a resource that was not previously allocated"""

    class Library(Enum):
        mingw64 = 1
        vscode = 2

        def get_library_name(self) -> str:
            return {1: "libdevice_reader_mingw64.dll",
                    2: "device_reader_vscode.dll"}[self.value]

    def __init__(self):
        self.allocated_resources = []
