cmake_minimum_required(VERSION 3.16)

project(HelloQt6 VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)

qt_standard_project_setup()

qt_add_executable(HelloQt6 src/main.cpp)

target_link_libraries(HelloQt6 PRIVATE Qt6::Widgets)

add_custom_command(TARGET HelloQt6 POST_BUILD
    COMMAND "${WINDEPLOYQT_EXECUTABLE}"
            --verbose 1
            --pdb
            \"$<TARGET_FILE:HelloQt6>\"
    COMMENT "Deploying Qt libraries using windeployqt for HelloQt6 ..."
)
