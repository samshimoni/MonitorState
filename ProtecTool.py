import os
import sys

def Close():
    os.popen('attrib +h MonitorState.{645ff040-5081-101b-9f08-00aa002f954e}')
def Open():
    os.popen('attrib -h MonitorState.{645ff040-5081-101b-9f08-00aa002f954e}')
    os.rename("MonitorState.{645ff040-5081-101b-9f08-00aa002f954e}", "MonitorState")
def Create_Linux():
    if not os.path.exists("MonitorState"):
        os.mkdir("MonitorState")
        with open("MonitorState/Status_Log.txt",'w'): pass
        with open("MonitorState/Status_Log.txt", 'w'): pass
        with open("MonitorState/processList.csv",'wb'):pass
        Close()

def HackerRemovedFolder(path):
    if not os.path.exists(path) :
        print"the foder was deleted by Hacker  "
        sys.exit(1);

