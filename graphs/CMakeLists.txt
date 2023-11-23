cmake_minimum_required(VERSION 3.0)

project(GCNN_API)

add_executable(GCNN_API
    src/main.cpp
    src/GraphResourceFactory.cpp
    src/GraphService.cpp
    src/GraphServiceSettingsFactory.cpp
)


target_link_libraries(GCNN_API restbed)

target_include_directories(GCNN_API PUBLIC $(CMAKE_SOURCE_DIR)/include)

set_property(TARGET GCNN_API PROPERTY CXX_STANDARD 17)