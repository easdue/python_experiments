#ifndef DEVICE_READER_H
    #define DEVICE_READER_H

    #ifdef _WIN32
        #ifdef BUILD_DLL
            #define DLLEXPORT __declspec(dllexport)
        #else
            #define DLLEXPORT __declspec(dllimport)
        #endif

        #define ADDCALL __cdecl
    #else
        #define DLLEXPORT
        #define ADDCALL
    #endif

    #ifdef __cplusplus
        extern "C" {
    #endif

    DLLEXPORT char* ADDCALL get_cell(const char* device, int row, int column);
    DLLEXPORT void ADDCALL free_resource(char* resource);

    #ifdef __cplusplus
    }
    #endif
#endif