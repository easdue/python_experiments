#include "device_reader.h"
#include <stdio.h>
#include <stdlib.h>

DLLEXPORT char* get_cell(const char* device, int row, int column)
{
    char *result;
    int size = snprintf(NULL, 0, "device[%d][%d]", row, column);

    result = (char *) malloc((size + 1) * sizeof(char));

    if (sprintf(result, "%s[%d][%d]", device, row, column) < 0) {
        result[0] = '\0';
    }

    return result;
}

DLLEXPORT void free_resource(char* resource) {
    free(resource);
}