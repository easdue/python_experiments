from cffi import FFI


ffibuilder = FFI()\

"""
 Can currently not parse preprocessor directives
   with open(os.path.join(os.path.dirname(__file__), "device_reader.h")) as f:
       ffibuilder.cdef(f.read())
"""
ffibuilder.cdef("""
    char* __cdecl get_cell(const char* device, int row, int column);
    void __cdecl free_resource(char* resource);
""")

ffibuilder.set_source("_device_reader_mingw_cffi",
"""
    #include "device_reader.h"
""", libraries=['../lib/libdevice_reader_mingw.dll'])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)

