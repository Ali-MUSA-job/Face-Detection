import cv2
import os
import numpy as np
import face_recognition

path = 'dataset/train'
images = []
className = []
myList = os.listdir(path)
#print(myList)


for clss in myList:
    curImg = cv2.imread(f'{path}/{clss}')
    images.append(curImg)
    className.append(os.path.splitext(clss)[0])
print(className)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

getEncodeList = findEncodings(images)
print('Encodeing Complete')


                                                        #Detect Faces From WebCam (Reat Time)
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    rtImg = cv2.resize(img,(0,0),None,0.5,0.5)
    rtImg = cv2.cvtColor(rtImg, cv2.COLOR_BGR2RGB)

    curFacesFrame = face_recognition.face_locations(rtImg)
    curEncodesFrame = face_recognition.face_encodings(rtImg)

    for encodeFace,faceLoc in zip(curEncodesFrame,curFacesFrame):
        matches = face_recognition.compare_faces(getEncodeList,encodeFace)
        faceDis = faceDis = face_recognition.face_distance(getEncodeList,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = className[matchIndex]
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img,name,(x1+6, y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


    cv2.imshow('Live Video', img)
    k = cv2.waitKey(1)
    if k == 27 or k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

                                                        #Detect Faces From a Static Video

"""cap = cv2.VideoCapture('dataset/test/bill_gates.mp4')

while True:
        ret, img = cap.read()
        rtImg = cv2.resize(img, (0, 0), None, 0.5, 0.5)
        rtImg = cv2.cvtColor(rtImg, cv2.COLOR_BGR2RGB)

        curFacesFrame = face_recognition.face_locations(rtImg)
        curEncodesFrame = face_recognition.face_encodings(rtImg)

        for encodeFace,faceLoc in zip(curEncodesFrame,curFacesFrame):
            matches = face_recognition.compare_faces(getEncodeList,encodeFace)
            faceDis = faceDis = face_recognition.face_distance(getEncodeList,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = className[matchIndex]
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 2, x2 * 2, y2 * 2, x1 * 2
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img,name,(x1+6, y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


        cv2.imshow('Static Video', img)
        k = cv2.waitKey(1)
        if k == 27 or k == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()"""


