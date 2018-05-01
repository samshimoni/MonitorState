import ProtecTool
import ProcessList
import platform
import time
import keyboard

def start_tool():

    x = keyboard.Time()



    if platform.system() is "windows":

        ProtecTool.Create_Windows()
        while 1:
            ProtecTool.HackerRemovedFolder("MonitorState.{645ff040-5081-101b-9f08-00aa002f954e}")
            ProtecTool.Open()
            ProcessList.WriteCsv()
            ProtecTool.Close()
            time.sleep(x * 60)

    else:

        ProtecTool.Create_Linux()

        while 1 :
            ProtecTool.HackerRemovedFolder("MonitorState")
            ProcessList.WriteCsv()
            time.sleep(x*60)








