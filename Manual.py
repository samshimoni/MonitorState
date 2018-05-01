import keyboard
import main

def manual_start():

    print" Enter the first date "

    first = keyboard.Date()

    print" Enter the Second "

    second =keyboard.Date()

    for i in first :
        if second not in second:

            print ("process {0} number {1} was created\n ".format(i.name, i.pid))

    main.main_func()




