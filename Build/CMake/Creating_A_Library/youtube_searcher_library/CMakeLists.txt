cmake_minimum_required(VERSION 3.27)

project(youtube_searcher VERSION 1.0.0)

find_package(Boost REQUIRED)

# --- STATIC = `.lib`, SHARED = `.dll`
add_library(youtube_searcher STATIC src/youtube_searcher.cpp)

target_link_libraries(youtube_searcher
    PRIVATE                                # WE use BOOST, any USERS DO NOT need to `#include` it, therefore, make it PRIVATE.
        Boost::boost)


target_include_directories(youtube_searcher
    PUBLIC
        $<INSTALL_INTERFACE:include>                            # When installing, look inside the `<prefix>/include` directory for header files.
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>  # When building, look inside `${CMAKE_CURRENT_SOURCE_DIR}/include`
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src                         # We use `youtube_searcher_utilities.hpp`, any users do not, hence, use PRIVATE.
)

install(TARGETS youtube_searcher
    EXPORT youtube_searcherTargets         # This will generate the file `youtube_searcher.lib` from the target `add_library(youtube_searcher ...)`.
    DESTINATION lib                        # When installed, will go to ${CMAKE_INSTALL_PREFIX}/lib.
)

install(EXPORT youtube_searcherTargets
    FILE youtube_searcherTargets.cmake      # Generates, youtube_searchersTargets.cmake.
    DESTINATION lib/cmake/youtube_searcher  # When installed, will go to ${CMAKE_INSTALL_PREFIX}/lib/cmake/youtube_searcher.
)

# ---------- Installation of CMake config file ----------
# --- Generate all necessary .cmake files to that users of our library can simply call `find_package(youtube_searcher REQUIRED)`.

include(CMakePackageConfigHelpers)

# --- Create via build, not install. This is responsible for creating `youtube_searcherTargets.cmake` when BUILDING.
export(EXPORT youtube_searcherTargets
  FILE ${CMAKE_CURRENT_BINARY_DIR}/cmake/youtube_searcher/youtube_searcherTargets.cmake
)

# --- Generate the `Config.cmake` file when building from the given `Config.cmake.in` file.
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/youtube_searcherConfig.cmake.in                # Input file.
    ${CMAKE_CURRENT_BINARY_DIR}/cmake/youtube_searcher/youtube_searcherConfig.cmake  # Output file.
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/youtube_searcher               # When installing, place into `lib/cmake/youtube_searcher`.
)

# --- Generates the `ConfigVersion.cmake` file when building.
write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/cmake/youtube_searcher/youtube_searcherConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY AnyNewerVersion
)

# --- After building, we can now install the previously generated `Config.cmake` and `ConfigVersion.cmake`.
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/cmake/youtube_searcher/youtube_searcherConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/cmake/youtube_searcher/youtube_searcherConfigVersion.cmake
    DESTINATION lib/cmake/youtube_searcher     # Place the FILES into `${CMAKE_INSTALL_PREFIX}/lib/cmake/youtube_searcher`.
  )

# -- Install the header files for our users to `#include "youtube_searcher.hpp" and correctly link.
install(
    FILES include/youtube_searcher.hpp
    DESTINATION include
)