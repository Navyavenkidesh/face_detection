import cv2

cap = cv2.VideoCapture('/home/navya/Documents/to_study/opencv/yes.mp4')
face_cascade = cv2.CascadeClassifier('/home/navya/Documents/to_study/face_detection/data/haarcascade_frontalface_default.xml')
eye =cv2.CascadeClassifier('/home/navya/Documents/to_study/face_detection/data/haarcascade_eye.xml')

#to read frames

while True:  
    success,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame)
    eyes =eye.detectMultiScale(gray)
    print(len(faces))
    print(len(eyes))
    for (x,y,w,h) in faces:  
     cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
    for (x,y,w,h) in eyes:   #width hight eplum add akanam
     cv2.rectangle(frame,(x,y),(x+w,y+h),color=(255,0,0),thickness=2)

#detect face in frace in real time 
    cv2.imshow('vedio cap',frame)

    if cv2.waitKey(1) & 0XFF == 27:
        break
     
cap.release()

cv2.destroyAllWindows()     
