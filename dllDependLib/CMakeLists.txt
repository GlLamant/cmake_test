cmake_minimum_required(VERSION 3.5)
project(dllDependLibPro)

include_directories(${PROJECT_SOURCE_DIR})

add_library(sta STATIC static.cpp)
add_library(dym SHARED dynamic.cpp)
target_link_libraries(dym sta)

add_executable(main_test main.cpp)
target_link_libraries(main_test dym)
