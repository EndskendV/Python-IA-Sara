# CMake generated Testfile for 
# Source directory: /home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core
# Build directory: /home/jesusdiaz/Escritorio/Linux/modules/core
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_core "/home/jesusdiaz/Escritorio/Linux/bin/opencv_test_core" "--gtest_output=xml:opencv_test_core.xml")
set_tests_properties(opencv_test_core PROPERTIES  LABELS "Main;opencv_core;Accuracy" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1352;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core/CMakeLists.txt;175;ocv_add_accuracy_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core/CMakeLists.txt;0;")
add_test(opencv_perf_core "/home/jesusdiaz/Escritorio/Linux/bin/opencv_perf_core" "--gtest_output=xml:opencv_perf_core.xml")
set_tests_properties(opencv_perf_core PROPERTIES  LABELS "Main;opencv_core;Performance" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/performance" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1251;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core/CMakeLists.txt;176;ocv_add_perf_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core/CMakeLists.txt;0;")
add_test(opencv_sanity_core "/home/jesusdiaz/Escritorio/Linux/bin/opencv_perf_core" "--gtest_output=xml:opencv_perf_core.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_core PROPERTIES  LABELS "Main;opencv_core;Sanity" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/sanity" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1252;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core/CMakeLists.txt;176;ocv_add_perf_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/core/CMakeLists.txt;0;")