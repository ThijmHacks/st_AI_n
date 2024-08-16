import random

import st_AI_n.lists
import st_AI_n.responses.lists

def response(prompt):
    if st_AI_n.lists.checkindir(prompt): return "This is an available command"
    else: return "I do not know this command"