import pyrealsense2 as rs
import cv2
import numpy as np
from CommonUtility import *
from CameraUtility import *

def main():
    CommonUtility.Cls()
    CommonUtility.WelcomeScreen()
    
    ctx = rs.context()
    cameraUtility = CameraUtility(ctx)
    cameraUtility.SelectCamera()
    
    cfg = rs.config()
    cfg.enable_device(cameraUtility.GetCameraSerial())
    cfg.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
    
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    pipeline = rs.pipeline()
    pipeline.start(cfg)
    
    cameraUtility.PrintCameraInfo()
    CommonUtility.PrintExitKey('q')
    
    while(True):
        frame = pipeline.wait_for_frames().get_color_frame()
        frame = np.asanyarray(frame.get_data())
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.namedWindow('RealSense Face Recognition Example', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense Face Recognition Example', frame)
        
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
        
    pipeline.stop()
    cv2.destroyAllWindows()
    CommonUtility.Cls()



if __name__ == "__main__":
    main()