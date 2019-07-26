cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
get_filename_component(solution_name ${CMAKE_CURRENT_LIST_DIR} NAME)
project(${solution_name})

set(CMake_DIR ${CMAKE_CURRENT_LIST_DIR}/cmake)
message(STATUS "${PROJECT_NAME}: CMake tools directory ${CMake_DIR}")

if(NOT EXISTS "${CMake_DIR}/conan.cmake")
    message(STATUS "${PROJECT_NAME}: Downloading conan.cmake from https://github.com/memsharded/cmake-conan")
    file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/master/conan.cmake" "${CMake_DIR}/conan.cmake")
endif()

include(${CMake_DIR}/conan.cmake)
include(${CMake_DIR}/parse.cmake)
include(${CMake_DIR}/repositories.cmake)

initialize_conan_repositories()

conan_cmake_run(CONANFILE conanfile.txt)
conan_basic_setup()

include(${CMAKE_BINARY_DIR}/conanbuildinfo_multi.cmake)

include_directories(source)

add_recursive(source PARSED_SOURCE)
add_executable(${PROJECT_NAME} ${PARSED_SOURCE})

foreach(header_directory ${CONAN_INCLUDE_DIRS})
    include(${header_directory})
endforeach()

foreach(debug_lib ${CONAN_LIBS_DEBUG})
    target_link_libraries(${PROJECT_NAME} debug ${debug_lib})
endforeach()

foreach(release_lib ${CONAN_LIBS_RELEASE})
    target_link_libraries(${PROJECT_NAME} optimized ${release_lib})
endforeach()