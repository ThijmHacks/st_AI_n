import st_AI_n.lists
from st_AI_n.lists import randomunknownprompt


def response(prompt):
    randomanswervar = st_AI_n.lists.checkindir(prompt)

    if randomanswervar is not None:
        print(st_AI_n.lists.randomanswer(randomanswervar))
    else: print(randomunknownprompt())