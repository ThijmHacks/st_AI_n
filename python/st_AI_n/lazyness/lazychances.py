import random

import st_AI_n.lazyness



def lazyapproach():
    lazyapproachrandom = random.randint(1,10)
    if lazyapproachrandom == 8:
        whatapproachdef()
        return True
    else: return False

def whatapproachdef():
    whatapproach = random.randint(1,2)
    if whatapproach == 1: st_AI_n.lazyness.toolazy()
    if whatapproach == 2: st_AI_n.lazyness.givemetoast()
