from cffi import FFI


class DeviceReader:
    def __init__(self):
        self.ffi = FFI()
        self.ffi.cdef("""
            char* get_cell(char *device, int row, int column);
            void free_resource(char *resource);
        """)
        #self.lib = self.ffi.dlopen("../../device_reader_dll/build/libdevice_reader.dll")
        self.lib = self.ffi.dlopen("./device_reader.dll")
        self.allocated_resource = []

    def get_cell(self, device: str, row: int, col: int):
        self.allocated_resource.append(self.lib.get_cell(device, row, col))
        return self.allocated_resource[-1]

    def to_string(self, c_char_ptr):
        return self.ffi.string(c_char_ptr)


reader = DeviceReader()

cell = reader.get_cell(b"Device1", 0, 1)
print(type(cell))
print(reader.to_string(cell))
