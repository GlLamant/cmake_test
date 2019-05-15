cmake_minimum_required(VERSION 3.5)
project(subdirectory_pass_param_pro)

set(MAIN_DEFINE "Variable defined by main")
message(WARNING "MAIN >> MAIN_DEFINE: " ${MAIN_DEFINE})

add_subdirectory(sub)

message(WARNING "MAIN >> SUB_DEFINE: " ${SUB_DEFINE})

add_executable(main_test main.cpp)	