cmake_minimum_required(VERSION 3.10)

project(MyProject VERSION 1.0)

add_executable(MyProject src/main.cpp)

target_include_directories(MyProject
    PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>  # Use this during build
        $<INSTALL_INTERFACE:include>                      # Use this during install
)

install(TARGETS MyProject
    RUNTIME DESTINATION bin
)

install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/ DESTINATION include)
