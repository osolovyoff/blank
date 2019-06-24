cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
get_filename_component(solution_name ${CMAKE_CURRENT_LIST_DIR} NAME)
project(${solution_name})

if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
    message(STATUS "Downloading conan.cmake from https://github.com/memsharded/cmake-conan")
    file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/master/conan.cmake" "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(conan.cmake)
include(CMake/parse.cmake)
include(CMake/repositories.cmake)

initialize_conan_repositories()

conan_cmake_run(CONANFILE conanfile.txt)
conan_basic_setup()

include(${CMAKE_BINARY_DIR}/conanbuildinfo_multi.cmake)

include_directories(source)

add_recursive(source PARSED_SOURCE)
add_executable(${PROJECT_NAME} ${PARSED_SOURCE})

foreach(debug_lib ${CONAN_LIBS_DEBUG})
    target_link_libraries(${PROJECT_NAME} debug ${debug_lib})
endforeach()

foreach(release_lib ${CONAN_LIBS_RELEASE})
    target_link_libraries(${PROJECT_NAME} optimized ${release_lib})
endforeach()