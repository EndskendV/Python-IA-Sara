# CMake generated Testfile for 
# Source directory: /home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo
# Build directory: /home/jesusdiaz/Escritorio/Linux/modules/photo
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_photo "/home/jesusdiaz/Escritorio/Linux/bin/opencv_test_photo" "--gtest_output=xml:opencv_test_photo.xml")
set_tests_properties(opencv_test_photo PROPERTIES  LABELS "Main;opencv_photo;Accuracy" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1352;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1110;ocv_add_accuracy_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo/CMakeLists.txt;7;ocv_define_module;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo/CMakeLists.txt;0;")
add_test(opencv_perf_photo "/home/jesusdiaz/Escritorio/Linux/bin/opencv_perf_photo" "--gtest_output=xml:opencv_perf_photo.xml")
set_tests_properties(opencv_perf_photo PROPERTIES  LABELS "Main;opencv_photo;Performance" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/performance" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1251;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1111;ocv_add_perf_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo/CMakeLists.txt;7;ocv_define_module;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo/CMakeLists.txt;0;")
add_test(opencv_sanity_photo "/home/jesusdiaz/Escritorio/Linux/bin/opencv_perf_photo" "--gtest_output=xml:opencv_perf_photo.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_photo PROPERTIES  LABELS "Main;opencv_photo;Sanity" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/sanity" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1252;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1111;ocv_add_perf_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo/CMakeLists.txt;7;ocv_define_module;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/photo/CMakeLists.txt;0;")