cmake_minimum_required(VERSION 3.21)
project(goodshell C)

add_executable(goodshell
    handler.c
    logic.c
    main.c
)

target_include_directories(goodshell PRIVATE headerfiles)
