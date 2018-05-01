import re
import ProcessList
import os


def Path():
    while 1:
        path = int(raw_input("Please Enter Direction to Files  "))
        if os.path.exists(path):
            os.chdir(path)
            break
        else:
            print ("Bad input Inserted.. PRESS AGAIN PLEASE")

def Date():
    while 1:
        date =raw_input("Enter date in order : YYYY-MM-DD H-M ")
        y = re.compile('.{4}-.{2}-.{2} .{2}:.{2}')
        if y.match(date):
            processlist=ProcessList.DateInList(date)
            if (processlist):
                return processlist
            else :
                print ("there is no such date ")
        else :
            print ("Bad input Inserted.. PRESS AGAIN PLEASE")


def Time():
    while 1:

        try:

            x=int (raw_input("Enter Time To Scan (: "))

        except ValueError:
            print ("Bad input Inserted.. PRESS AGAIN PLEASE ")
            continue
        else:

            return x

def Choice():
    while 1:
        try:
            x=int(raw_input("What Is Your Choice "))
            if (x>0 and x<3):

                return x
            else:
                print (" worng input enter num between 0 to 3 ")
        except ValueError:
            print ("Bad input Inserted.. PRESS AGAIN PLEASE")
            continue

