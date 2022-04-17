cmake_minimum_required(VERSION 3.0)

project(MyProject)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${MyProject_SOURCE_DIR}/bin)

find_package(PythonInterp REQUIRED)
execute_process(
  COMMAND python3 ${MyProject_SOURCE_DIR}/A/preparing.py 
  WORKING_DIRECTORY ${MyProject_SOURCE_DIR}/A
)

include_directories(${MyProject_SOURCE_DIR}/A)
add_subdirectory(${MyProject_SOURCE_DIR}/B ${MyProject_SOURCE_DIR}/lib)
include_directories(${GTEST_INCLUDE_DIRS})

add_executable(C ${CMAKE_SOURCE_DIR}/C/main.cpp)
target_link_libraries(C Blib) 
target_include_directories(C PUBLIC ${CMAKE_CURRENT_LIST_DIR})

add_executable(CTest ${CMAKE_SOURCE_DIR}/C/main_test.cpp)
target_link_libraries(CTest Blib)
target_link_libraries(CTest gtest gtest_main pthread)
target_include_directories(CTest PUBLIC ${CMAKE_CURRENT_LIST_DIR})