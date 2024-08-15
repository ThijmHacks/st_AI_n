import time


def tolazy():
    print("I will not do that, I am to lazy for that.")

def givemetoast():
    print("I want toast, \nbut bread is nice as well")
    print("Give me the toast emoji.")
    toastemoji = input("BREADEMOJI: ")
    if toastemoji != "🍞": quit()
    else: print("Thx, now i am not a hungry person anymore.")

def pauseneeded():
    print("I will have a 2 minute break now.")
    time.sleep(120)