#!/bin/sh
rm -rf cmake_build cmake_install
build_dir=`pwd`/cmake_build
install_dir=`pwd`/cmake_install
#cmake --build -B cmake_build -DCMAKE_INSTALL_PREFIX=../cmake_install -DCMAKE_BUILD_TYPE=Debug
cmake -B${build_dir} -DCMAKE_BUILD_TYPE=Debug
cmake --build ${build_dir} -j -v
cmake --install ${build_dir} --prefix ${install_dir} -v