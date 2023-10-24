# CMake generated Testfile for 
# Source directory: /home/jesusdiaz/Escritorio/Linux/opencv-master/modules/flann
# Build directory: /home/jesusdiaz/Escritorio/Linux/modules/flann
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_flann "/home/jesusdiaz/Escritorio/Linux/bin/opencv_test_flann" "--gtest_output=xml:opencv_test_flann.xml")
set_tests_properties(opencv_test_flann PROPERTIES  LABELS "Main;opencv_flann;Accuracy" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1352;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1110;ocv_add_accuracy_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/flann/CMakeLists.txt;2;ocv_define_module;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/flann/CMakeLists.txt;0;")
