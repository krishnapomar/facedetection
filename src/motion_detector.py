import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
        
    def get_frame(self):
        ret, frame = self.video.read()
        frame = cv2.resize(frame, None, fx=0.6, interpolation=cv2.INTER_AREA)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontfalface_default.xml')
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            break
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
