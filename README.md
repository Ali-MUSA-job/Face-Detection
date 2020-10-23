- Face Detection (Recognition) Using OpenCV.

- in this project we used Python(OpenCV) and Pycharm editor.

- To do the faces Recognition we used the (face_recognition) library:
  - First we fetch the images from (dataset/train) file.
  - spilt people names from the names of photos.
  - We do the encode for images to use that for recognition.
  - Finally we use the webcam or static video for do the test (recognition).
  
- if you need to use your own dataset for train and test you need just for change content of (dataset) file.
- for train a project with your own photos you need to upload the photos for (dataset/train) file, for test a project with a static videos you need to upload your own videos for (dataset/test).

- Please note, the names of people must be written on the images to be used because the program has been configured to take people names from the names of the images.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Requirement libraries for building this project in a fresh environment:
  - NumPy
  - Dlib
  - cmake
  - face_recognition

- To install (dlib) you just need to install Visual Studio Community and add (Desktop Development with c++) package. (we will not use VS just we need to install that to own dlib library).
- To install (cmake) you can use (pip install cmake).
- To install (NumPy) you can use (pip install numpy).
- To install (face_recognition) you can use (pip install face_recognition).

- if you need another way to install (cmake - numpy - face_recognition) from pychram:
    - make a new project.
    - follow this install roadmap : File -> Settings -> Project :(your project name) -> Project Interpreter -> press (+) -> (Type library name in the search) -> install.
    - Please note : when you search for (face recognition) library You will see a lot of libraries, please install this library (face-recognition) 

- Please attention : to install face_recognition library you must own (dlib) library before, please first install VS Community and add (Desktop Development with c++) package.

Thanks for reading ....

