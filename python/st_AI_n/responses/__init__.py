import random

import st_AI_n.lists
import st_AI_n.responses.lists

def response(prompt):
    st_AI_n.lists.checklists(prompt)
    if st_AI_n.lists: answer = random.choice(st_AI_n.responses.lists.hello)