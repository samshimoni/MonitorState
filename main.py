import sys
import keyboard
import Tool


def main_func():

    print ("Welcome to the Monitor state")

    keyboard.Path()

    print ("Select Menu:\n1. Monitor State\n2. Manual Mode\n3. Exit\n")

    c=keyboard.Choice()
    if c==1:
        Tool.start_tool()
    else:
        sys.exit(0)

main_func()

