cmake_minimum_required(VERSION 3.5)
project(Demo)

option(OPTION1 "option 1" ON)
option(OPTION2 "option 2" ON)
option(OPTION3 "option 3" ON)

if(OPTION1)
	MESSAGE(STATUS "OPTION1 is ${OPTION1}")
else ()
	MESSAGE(STATUS "OPTION1 is ${OPTION1}")
endif ()

if(OPTION2)
	MESSAGE(STATUS "OPTION2 is ${OPTION2}")
else ()
	MESSAGE(STATUS "OPTION2 is ${OPTION2}")
endif ()

if(OPTION3)
	MESSAGE(STATUS "OPTION3 is ${OPTION3}")
else ()
	MESSAGE(STATUS "OPTION3 is ${OPTION3}")
endif ()

# configure_file(
	# "${PROJECT_SOURCE_DIR}/config.h.in"
	# "${PROJECT_SOURCE_DIR}/config.h"
	# )

aux_source_directory(. DIR_SRCS)

add_executable(Demo main.cc)

if(USE_MYMATH)
	target_link_libraries(Demo MathFunctions)
endif(USE_MYMATH)
