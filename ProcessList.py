import datetime
import sys
import Scanner
import StatusLog
import platform
import ProtecTool
from Process import Process
import csv
import os.path

lastChanged=""

def RLScanner():
    process = []
    date = ""
    with open("MonitorState/processList.csv", 'rb') as a:
        bufferReader = csv.reader(a)
        for line in reversed(list(bufferReader)):
            p = Process(line[0],line[1])
            if not process:
                process.append(p)
                date = line[2]
            else:
                if date == line[2]:
                    process.append(p)
                else:
                    return process
    return process

def WriteCsv():

    currentDate=datetime.datetime.now().strftime("%y-%m-%d %H-%M")
    list = Scanner.ProcessList()
    if lastChanged=="" or (os.stat("MonitorState/processList.csv").st_mtime == lastChanged) :
        lastProc = RLScanner()
        StatusLog.WriteLogFile(list, lastProc, currentDate)
        with open("MonitorState/processList.csv", 'ab') as ocsv:
            bufferWriter = csv.writer(ocsv, delimiter=',')
            for proc in list:
                bufferWriter.writerow([proc.pid, proc.name, currentDate])
    else:
        print "nothing change"
        sys.exit(1)

def DateInList(date):

    processList=[]

    if platform.system() is "windows":
        ProtecTool.Open()
    with open("MonitorState/processList.csv", 'rb') as rb:
        bufferReader=csv.reader(rb)
        for i in bufferReader:
            if i[2]==date:
                processList.append(Process(i[0],i[1]))

        ProtecTool.Close()
    return  processList


