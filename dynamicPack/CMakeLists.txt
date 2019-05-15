cmake_minimum_required(VERSION 3.5)
project(DynamicPack)

option (FUN1 "Use fun1 library" ON)
option (FUN2 "Use fun2 library" ON)
option (FUN3 "Use fun3 library" ON)
option (FUN4 "Use fun4 library" ON)
option (FUN5 "Use fun5 library" ON)

if(FUN1)
	aux_source_directory(./fun1 SRCS)
endif(FUN1)

if(FUN2)
	aux_source_directory(./fun2 SRCS)
endif(FUN2)

if(FUN3)
	aux_source_directory(./fun3 SRCS)
endif(FUN3)

if(FUN4)
	aux_source_directory(./fun4 SRCS)
endif(FUN4)

if(FUN5)
	aux_source_directory(./fun5 SRCS)
endif(FUN5)

add_library(dynamicPack SHARED ${SRCS})