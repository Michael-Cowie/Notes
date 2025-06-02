add_library(lib1 lib1.cpp lib1.h)

target_include_directories(lib1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
