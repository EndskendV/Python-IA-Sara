# CMake generated Testfile for 
# Source directory: /home/jesusdiaz/Escritorio/Linux/opencv-master/modules/highgui
# Build directory: /home/jesusdiaz/Escritorio/Linux/modules/highgui
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_highgui "/home/jesusdiaz/Escritorio/Linux/bin/opencv_test_highgui" "--gtest_output=xml:opencv_test_highgui.xml")
set_tests_properties(opencv_test_highgui PROPERTIES  LABELS "Main;opencv_highgui;Accuracy" WORKING_DIRECTORY "/home/jesusdiaz/Escritorio/Linux/test-reports/accuracy" _BACKTRACE_TRIPLES "/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVUtils.cmake;1763;add_test;/home/jesusdiaz/Escritorio/Linux/opencv-master/cmake/OpenCVModule.cmake;1352;ocv_add_test_from_target;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/highgui/CMakeLists.txt;309;ocv_add_accuracy_tests;/home/jesusdiaz/Escritorio/Linux/opencv-master/modules/highgui/CMakeLists.txt;0;")
