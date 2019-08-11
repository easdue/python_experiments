cmake_minimum_required(VERSION 3.0.0)
project(device_reader VERSION 0.1.0)

include(CTest)
enable_testing()

# Automatically download and compile googletest 
# https://github.com/Crascit/DownloadProject/blob/master/CMakeLists.txt

if (CMAKE_VERSION VERSION_LESS 3.2)
    set(UPDATE_DISCONNECTED_IF_AVAILABLE "")
else()
    set(UPDATE_DISCONNECTED_IF_AVAILABLE "UPDATE_DISCONNECTED 1")
endif()

include(DownloadProject.cmake)
download_project(PROJ               googletest
                 GIT_REPOSITORY     https://github.com/google/googletest.git
                 GIT_TAG            master
                 ${UPDATE_DISCONNECTED_IF_AVAILABLE})

# Prevent GoogleTest from overriding our compiler/linker options
# when building with Visual Studio
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

add_subdirectory(${googletest_SOURCE_DIR} ${googletest_BINARY_DIR})

add_library(device_reader SHARED device_reader.c)
add_definitions(-DBUILD_DLL)

add_subdirectory(tests ${device_reader_BINARY_DIR})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
