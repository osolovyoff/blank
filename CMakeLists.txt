#_________________________________________________________________________________________
#source_groups(src/ PROJECT_SOURCE_FILES)
macro(source_groups current_dir)
    file(GLOB children RELATIVE ${PROJECT_SOURCE_DIR}/${current_dir}
    ${PROJECT_SOURCE_DIR}/${current_dir}/*)

    foreach(child ${children})
        if(IS_DIRECTORY ${PROJECT_SOURCE_DIR}/${current_dir}/${child})
            source_groups(${current_dir}/${child})
        else()
            if(MSVC)
                string(REPLACE "/" "\\" groupname ${current_dir})
                string(REPLACE "src" "" groupname ${groupname})
            endif()
            source_group(${groupname} FILES ${PROJECT_SOURCE_DIR}/${current_dir}/${child})
        endif()
    endforeach()
endmacro()
#_________________________________________________________________________________________
#add_recursive(src/ PROJECT_SOURCE_FILES)
macro(add_recursive current_dir)
    file(GLOB_RECURSE PROJECT_SOURCE_FILES ${current_dir}/*.h ${current_dir}/*.cpp) 

    file(GLOB children RELATIVE ${PROJECT_SOURCE_DIR}/${current_dir}
    ${PROJECT_SOURCE_DIR}/${current_dir}/*)

    foreach(child ${children})
        if(IS_DIRECTORY ${PROJECT_SOURCE_DIR}/${current_dir}/${child})
            source_groups(${current_dir}/${child})
        else()
            if(MSVC)
                string(REPLACE "/" "\\" groupname ${current_dir})
                string(REPLACE "src" "" groupname ${groupname})
            endif()
            source_group(${groupname} FILES ${PROJECT_SOURCE_DIR}/${current_dir}/${child})
        endif()
    endforeach()

    source_group("" FILES ${current_dir}/main.cpp PARENT_SCOPE)
endmacro()
#_________________________________________________________________________________________
cmake_minimum_required(VERSION 2.7)
get_filename_component(SolutionName ${CMAKE_CURRENT_LIST_DIR} NAME)
project(${SolutionName})

option(USE_BOOST "Setup to On for use Boost library" OFF)
if (USE_BOOST)
    set(BOOST_ROOT $ENV{BOOST_DIR})
    if (NOT EXISTS ${BOOST_ROOT})
        message(FATAL_ERROR "Please, set path to boost library into 'BOOST_DIR' environment variable")  
    else()
        string( REPLACE "\\" "/" BOOST_ROOT ${BOOST_ROOT})
        message(STATUS       "BOOST_ROOT directory was found is ${BOOST_ROOT}")
    endif()
    
    option(Boost_USE_STATIC_LIBS    "Set to ON to force the use of the static libraries."                                                  ON)
    option(Boost_USE_MULTITHREADED  "Set to OFF to use the non-multithreaded libraries                                         ('mt' tag)" ON)  
    option(Boost_USE_STATIC_RUNTIME "Set to ON or OFF to specify whether to use libraries linked statically to the C++ runtime ('s' tag) " ON)
    option(Boost_USE_DEBUG_RUNTIME  "Set to ON or OFF to specify whether to use libraries linked to the MS debug C++ runtime   ('g' tag) " ON)
endif()

add_recursive(src/)

set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG}   /MTd /Zi /Ob0 /Od /EHsc /RTC1 /D_DEBUG /D_ITERATOR_DEBUG_LEVEL=2 /DBoost_DEBUG=ON")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT /O2 /Ob2") 

add_definitions(-D _CRT_SECURE_NO_WARNINGS)
add_definitions(-D _WIN32_WINNT=0x0501)

include_directories("src/")
if(USE_BOOST)
    find_package(Boost COMPONENTS regex system chrono date_time filesystem program_options serialization REQUIRED)
    include_directories(${Boost_INCLUDE_DIR})
endif()
    
add_executable(Project ${PROJECT_SOURCE_FILES})

if (USE_BOOST)
    target_link_libraries(Project ${Boost_LIBRARIES})
endif()