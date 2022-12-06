import pyrealsense2 as rs
from CommonUtility import *


class CameraUtility:
    
    def __init__(self, ctx):
        self.ctx = ctx
        #self.SelectCamera()
        #self.PrintCameraInfo()
        
        
        
    def CameraCount(self):
        return len(self.ctx.query_devices())
    
    
    
    def GetCameraSerial(self):
        return self.camera.get_info(rs.camera_info.serial_number)
    
    
    
    def PrintCameraInfo(self):
        print("Camera information:")
        CommonUtility.PrintLine()
        print("- NAME:", self.camera.get_info(rs.camera_info.name))
        print("- SERIAL:", self.camera.get_info(rs.camera_info.serial_number))
        print("- HOST OS: ", end="")
        CommonUtility.PrintOS()
        CommonUtility.PrintLine()
    
    
    
    def SelectCamera(self):
        cameraCount = self.CameraCount()
        
        if(cameraCount == 0):
            print("No cameras found!")
            quit()
        elif(cameraCount == 1):
            self.camera = self.ctx.query_devices()[0]
        else:
            i = int(0)
            print("Available cameras:")
            CommonUtility.PrintLine()
            for c in self.ctx.query_devices():
                print("{0}. {1}".format(i, c.get_info(rs.camera_info.name)))
                i = i+1
            CommonUtility.PrintLine()
            choice = int(input("Select camera: "))
            if(choice < 0 and choice > i):
                self.camera = self.ctx.query_devices()[0]
            else:
                self.camera = self.ctx.query_devices()[choice]
            CommonUtility.Cls()
            