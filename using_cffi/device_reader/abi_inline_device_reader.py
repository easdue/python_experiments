import os

from cffi import FFI

from cffi_device_reader import CffiDeviceReader


class AbiInlineDeviceReader(CffiDeviceReader):
    def __init__(self, library: CffiDeviceReader.Library):
        super().__init__()

        self.ffi = FFI()
        self.ffi.cdef("""
            char* get_cell(char *device, int row, int column);
            void free_resource(char *resource);
        """)

        library_name = library.get_library_name()
        self.lib = self.ffi.dlopen(os.path.join(os.path.dirname(__file__), library_name))

    def get_cell(self, device: bytes, row: int, col: int):
        """
        Returns the requested cell value of the specified device

        Parameters
        ----------
        device bytes
            The device you want to retrieve the cell value on
        row int
            The table row of the value you want to retrieve
        col int
            The table column of the value you want to retrieve

        Returns
        -------
            The pointer to the byte array containing the value of the cell
            **NOTE:** call free_resource() or free_resources() to free the allocated memory
        """
        self.allocated_resources.append(self.lib.get_cell(device, row, col))
        return self.allocated_resources[-1]

    def to_string(self, c_char_ptr) -> str:
        return self.ffi.string(c_char_ptr)

    def free_resource(self, resource) -> None:
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


#reader2 = AbiInlineDeviceReader(AbiInlineDeviceReader.Library.mingw64)
#cell2 = reader2.get_cell(b"Device2", 1, 0)
#print(f"reader2.cell: {reader2.to_string(cell2)}")
