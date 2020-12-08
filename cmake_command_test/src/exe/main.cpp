#include <base.h>

int main()
{
#if 1
    print(1);
#else
    const char *msg = "Hello world!";
    print(msg);
#endif
    return 0;
}