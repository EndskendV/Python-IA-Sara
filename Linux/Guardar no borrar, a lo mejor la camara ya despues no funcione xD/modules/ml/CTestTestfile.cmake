# CMake generated Testfile for 
# Source directory: /home/jesusdiaz/Escritorio/Linux/opencv-master/modules/ml
# Build directory: /home/jesusdiaz/Escritorio/Linux/modules/ml
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_ml "/home/jesusdiaz/Escritorio/Linux/bin/opencv_test_ml" "--gtest_output=xml:opencv_test_ml.xml")
set_tests_properties(opencv_test_ml PROPERTIES  LABELS "Main;opencv_ml;Accuracy" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1352;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1110;ocv_add_accuracy_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/ml/CMakeLists.txt;2;ocv_define_module;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/ml/CMakeLists.txt;0;")
