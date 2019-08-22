import os

os.environ["PATH"] += os.pathsep + os.path.join(os.path.dirname(__file__), "../lib")

from _device_reader_mingw_cffi import ffi, lib


print(ffi.string(lib.get_cell(b"Device1", 1, 0)))
