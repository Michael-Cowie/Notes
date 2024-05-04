add_library(simplelib simplelib.cpp)

target_include_directories(simplelib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
