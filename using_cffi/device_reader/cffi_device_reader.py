from abc import ABC
from enum import Enum


class CffiDeviceReader(ABC):
    class ResourceNotAllocated(Exception):
        """Exception thrown when trying to free a resource that was not previously allocated"""

    class Library(Enum):
        mingw = 1
        msvc = 2

        def get_library_name(self) -> str:
            return {1: "../lib/libdevice_reader_mingw.dll",
                    2: "../lib/device_reader_msvc.dll"}[self.value]

    def __init__(self):
        self.allocated_resources = []
