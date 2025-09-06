
cmake_minimum_required(VERSION 3.5)
project(pass_stub)
add_executable(apply_pass src/apply_pass.cpp src/pass_stub.cpp)
set_target_properties(apply_pass PROPERTIES CXX_STANDARD 17)
