include_directories(..)

add_executable(device_reader_test device_reader_test.cpp)
target_link_libraries(device_reader_test device_reader${LIB_POSTFIX} gtest_main)

add_test(NAME DeviceReaderTest COMMAND device_reader_test)