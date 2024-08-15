import time

import st_AI_n

promptslimited = 10

#When not yet st_AI_n__PLUS:
def reachedlimited():
    print("It seems like you have reached the maximum of prompts for now\nI will take a 3 minute break, then I will come back.")
    time.sleep(120)
    st_AI_n.st_AI_n__PLUS.promptslimited = 10

def proptslimiteddef():
    st_AI_n.st_AI_n__PLUS.promptslimited = st_AI_n.st_AI_n__PLUS.promptslimited - 1
    if st_AI_n.st_AI_n__PLUS.promptslimited == 0: st_AI_n.st_AI_n__PLUS.reachedlimited()