cmake_minimum_required(VERSION 3.0)

project(GCNN)

add_executable(GCNN
    main.cpp
    GraphResourceFactory.cpp
    GraphService.cpp
    GraphServiceSettingsFactory.cpp
)


target_link_libraries(GCNN restbed)

target_include_directories(GCNN PUBLIC $(CMAKE_SOURCE_DIR)/include)

set_propert(TARGET GCNN PROPERTY CXX_STANDARD 17)