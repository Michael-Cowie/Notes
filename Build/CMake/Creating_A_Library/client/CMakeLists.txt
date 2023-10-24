cmake_minimum_required(VERSION 3.27)

project(client VERSION 1.0.0)

# --- Allows us to use the targets inside of `youtube_searcher`.
find_package(youtube_searcher REQUIRED)

# --- Creates `client.exe` from the source file.
add_executable(client src/client.cpp)

# --- Link our library to the `youtube_searcher.lib` and allows us the use the function definitions that we previously `#include youtube_searcher.hpp`.
target_link_libraries(client
    youtube_searcher
)