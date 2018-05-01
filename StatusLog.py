import os.path
import sys

lastChanged=""
def WriteLogFile(oldP,newP,time):
    if ((os.stat("MonitorState/Status_Log.txt").st_mtime==lastChanged) or (lastChanged=="") ):
        with open("MonitorState/Status_log.txt", 'a') as of:
            of.write("modified time was {0}\n".format(time))


            for proc in newP:
                if proc not in oldP:
                    of.write("process {0} no {1} was created ".format(proc.name,proc.pid))
                    print("process {0} no {1} was created ".format(proc.name,proc.pid))

            for proc in oldP:

                if proc not in newP:

                    print("problem with process no {0} whos name is {1}\n".format(proc.name,proc.pid))
                    of.write("problem with process no {0} whos name is {1}\n".format(proc.name,proc.pid))


            of.write("\n")

    else:
        sys.exit(1)