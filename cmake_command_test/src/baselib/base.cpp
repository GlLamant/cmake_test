#include "base.h"

#include <iostream>

int print(const char* msg)
{
    std::cout << msg << std::endl;
    return 0;
}

void print(int i)
{
    std::cout << i << std::endl;
}