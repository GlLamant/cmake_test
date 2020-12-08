set(SRCS main.cpp)

add_executable(baseExe
    ${SRCS}
)

target_link_libraries(baseExe
    base
)

install(
    TARGETS baseExe
)