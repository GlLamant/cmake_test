#include <stdio.h>
void staticFun() {
	printf("Static >>> %s:%d [%s]\n", __FILE__, __LINE__, __FUNCTION__);
}