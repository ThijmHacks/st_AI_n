import time
import os


def toolazy():
    print("I will not do that, I am to lazy for that.")

def givemetoast():
    print("I want toast, \nbut bread is nice as well")
    print("Give me the toast emoji.")
    toastemoji = input("BREADEMOJI: ")
    if toastemoji != "🍞":
        os.system("cls")
        print("That's not a bread emoji\nFuck you")
        print("Now I will die of hunger...")
        time.sleep(5)
        quit("st_AI_n died")
    else:
        print("Thx, now I am not a hungry person anymore.")

def pauseneeded():
    print("I will have a 2 minute break now.")
    time.sleep(120)