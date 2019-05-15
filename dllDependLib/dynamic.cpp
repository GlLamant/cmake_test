#include <stdio.h>
#include <static.h>
#include <dynamic.h>
void dynamicFun() {
	staticFun();
	printf("Dynamic >>> %s:%d [%s]\n", __FILE__, __LINE__, __FUNCTION__);
}