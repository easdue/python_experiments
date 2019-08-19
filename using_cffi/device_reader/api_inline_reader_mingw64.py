from _device_reader_cffi_mingw64 import ffi, lib

print(ffi.string(lib.get_cell(b"Device1", 1, 0)))