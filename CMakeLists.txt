function(add_recursive current_dir sources)
    file(GLOB files ${current_dir}/*.[h|cpp])
    file(GLOB children RELATIVE ${PROJECT_SOURCE_DIR}/${current_dir} ${PROJECT_SOURCE_DIR}/${current_dir}/*)

    foreach(child ${children})
        if(IS_DIRECTORY ${PROJECT_SOURCE_DIR}/${current_dir}/${child})
            add_recursive(${current_dir}/${child} ${sources})
        else()
            if(MSVC)
                string(REPLACE "/" "\\" groupname ${current_dir})
                string(REPLACE "src" "" groupname ${groupname})
            endif()
            set(filename ${PROJECT_SOURCE_DIR}/${current_dir}/${child})
            source_group(${groupname} FILES ${filename})
            set(${sources} ${${sources}} ${filename})
        endif()        
    endforeach()
    set(${sources} ${${sources}} PARENT_SCOPE)
endfunction(add_recursive)
#_________________________________________________________________________________________
cmake_minimum_required(VERSION 2.8)
get_filename_component(SolutionName ${CMAKE_CURRENT_LIST_DIR} NAME)
project(${SolutionName})

add_recursive(src PROJECT_SOURCE_FILES)
include_directories("src/")

set(CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG}   /MTd /Zi /Ob0 /Od /EHsc /RTC1 /D_DEBUG /D_ITERATOR_DEBUG_LEVEL=2 /DBoost_DEBUG=ON")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT /O2 /Ob2") 

add_definitions(-D _CRT_SECURE_NO_WARNINGS)
add_definitions(-D _WIN32_WINNT=0x0501)
    
add_executable(Project ${PROJECT_SOURCE_FILES})