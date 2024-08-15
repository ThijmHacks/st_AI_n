import time
import os


def wait(totaldots,timebetween):
    i = 0
    while i != totaldots:
        print(".")
        time.sleep(timebetween)
        os.system("cls")
        i = i + 1
        print("..")
        time.sleep(timebetween)
        os.system("cls")
        print("...")
        time.sleep(timebetween)
        os.system("cls")