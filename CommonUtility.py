from os import system, name
from time import sleep



class CommonUtility:
    
    @staticmethod
    def Cls():
        if name == 'nt':
            system('cls')
        else:
            system('clear')
            
        
    
    
    @staticmethod
    def Pause(sec):
        sleep(int(sec))
    
    
    
    
    @staticmethod
    def PrintLine():
        print("----------------------------")
        
        
        
    @staticmethod
    def PrintExitKey(key):
        print("\nPress {0} to EXIT.".format(key))
        
        
    
    @staticmethod
    def PrintOS():
        if name == 'nt':
            print("Windows")
        else:
            print("Linux")
            
            
    
    @staticmethod
    def WelcomeScreen():
        print("------------------------------------------")
        print("|   RealSense Face Recognition Example   |")
        print("|   Luka Grubić                          |")
        print("|   v0.1                                 |")
        print("|   2022.                                |")
        print("------------------------------------------")
        
        CommonUtility.Pause(3)
        CommonUtility.Cls()