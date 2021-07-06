import cv2

WebCamLink = input("Enter Webcam Link :")
CascadePath = input("enter path detection xml file :")
face_cascade = cv2.CascadeClassifier(CascadePath)
capture = cv2.VideoCapture(WebCamLink)

while True :
    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4 )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y) ,(x+w,y+h), (255,0,0),2 )
    cv2.imshow('livestream',frame)
    if cv2.waitKey(1) == ord("s"):
        break




capture.release()
cv2.destroyAllWindows()


