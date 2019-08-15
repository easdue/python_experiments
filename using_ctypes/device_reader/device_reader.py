"""This module provides the DeviceReader class"""
from ctypes import cdll, c_char_p, c_int, c_void_p


class DeviceReader:
    """Wrapper that enables to call libdevice_reader.dll functions

    Attributes
    ----------
    lib: CDLL
        The loaded libdevice_reader.dll
    allocated_resources: List[c_void_p]
        Holds references to allocated resources
    """

    class ResourceNotAllocated(Exception):
        """Exception thrown when trying to free a resource that was not previously allocated"""

    def __init__(self):
        self.lib = cdll.LoadLibrary("../../device_reader_dll/build/libdevice_reader.dll")
        self.lib.get_cell.argtypes = [c_char_p, c_int, c_int]
        self.lib.get_cell.restype = c_void_p
        self.lib.free_resource.argtypes = [c_void_p]
        self.lib.free_resource.restype = None
        self.allocated_resources = []

    def get_cell(self, device: bytes, row: int, column: int) -> c_void_p:
        """Returns the requested cell value of the specified device

        Parameters
        ----------
        device: bytes
            The device you want to retrieve the cell value on
        row: int
            The table row of the value you want to retrieve
        column: int
            The table column of the value you want to retrieve

        Returns
        -------
        c_void_p
            The pointer to the byte array containing the value of the cell
        """
        self.allocated_resources.append(self.lib.get_cell(device, row, column))
        print(f"allocated: {hex(self.allocated_resources[-1])}")
        return self.allocated_resources[-1]

    def free_resource(self, resource: c_void_p) -> None:
        """Releases the resource previously allocated when calling get_cell

        Parameters
        ----------
        resource: c_void_p
            The pointer to the byte array previously allocated by get_cell()

        Returns
        -------
        None
            When the resource has been successfully released

        Raises
        ------
        ResourceNotAllocated
            If the resource was not previously allocated
        """
        if resource in self.allocated_resources:
            print(f"releasing: {hex(resource)}")
            self.allocated_resources.remove(resource)
            self.lib.free_resource(resource)
        else:
            raise self.ResourceNotAllocated

    def free_resources(self):
        """Release all previously allocated resources"""
        for resource in reversed(self.allocated_resources):
            self.free_resource(resource)

    def num_allocated_resources(self) -> int:
        """Return the number of allocated resources

        Returns
        int
            The number of allocated resources
        """
        return len(self.allocated_resources)
