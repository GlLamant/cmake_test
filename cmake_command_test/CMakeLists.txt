cmake_minimum_required(VERSION 3.17)
project(base C CXX)

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    message(guol_warning " --- CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT")
endif()

add_subdirectory(src)

message( STATUS "C compiler: " ${CMAKE_C_COMPILER})
message( STATUS "C compiler flags: " ${CMAKE_C_FLAGS})
message( STATUS "CXX compiler: " ${CMAKE_CXX_COMPILER})
message( STATUS "CXX compiler flags: " ${CMAKE_CXX_FLAGS})
if(CMAKE_BUILD_TYPE)
  message( STATUS "Build type: " ${CMAKE_BUILD_TYPE})
endif(CMAKE_BUILD_TYPE)
message( STATUS "Install prefix: " ${CMAKE_INSTALL_PREFIX})
