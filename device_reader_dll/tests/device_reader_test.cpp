#include "gtest/gtest.h"
#include "device_reader.h"

#define GTEST_COUT std::cerr << "[          ] [ INFO ]"

TEST(device_reader, get_cell_returns_correct_string1)
{
    char *result = get_cell("device1", 0, 0);
    EXPECT_STREQ("device1[0][0]", result);
    free_resource(result);
}

TEST(device_reader, get_cell_returns_correct_string2)
{
    char *result = get_cell("device2", 0, 1);
    EXPECT_STREQ("device2[0][1]", result);
    free_resource(result);
}

TEST(device_reader, get_cell_returns_correct_string3)
{
    char *result = get_cell("device3", 1, 0);
    EXPECT_STREQ("device3[1][0]", result);
    free_resource(result);
}
