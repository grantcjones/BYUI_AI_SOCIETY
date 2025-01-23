#--------------------------------------------------------------------------------------------------------------
#?   Dependancies
#--------------------------------------------------------------------------------------------------------------

import sys
import time

#--------------------------------------------------------------------------------------------------------------
#?   Functions
#--------------------------------------------------------------------------------------------------------------

def wait(duration=0.1):
    "Waits a specified time."
    time.sleep(duration)

def clear():
    "Clears the console."
    print("\033[H\033[J", flush=False)

def hide_cursor():
    "Hides the console cursor."
    sys.stdout.write("\033[?25l")

def show_cursor():
    "Unhides the console cursor."
    sys.stdout.write("\033[?25h")
