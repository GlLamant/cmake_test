aux_source_directory(. DIR_LIB_SRCS)
add_library(MathFunctions ${DIR_LIB_SRCS})

if(USE_MYMATH)
	message(math)
else(USE_MYMATH) 
	message(Not math)
endif(USE_MYMATH)