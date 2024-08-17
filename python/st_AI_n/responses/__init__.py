import st_AI_n.lists
from st_AI_n.lists import randomunknownprompt
from st_AI_n.devil_st_AI_n.brownies import very_normal_brownies
from st_AI_n.games.guess_number import guess_number

def response(prompt):
    randomanswervar = st_AI_n.lists.checkindir(prompt)

    if randomanswervar is not None:
        if randomanswervar <= 99:
            return  st_AI_n.lists.randomanswer(randomanswervar)
        elif randomanswervar == 100:
            very_normal_brownies()
        elif randomanswervar == 200:
            guess_number()
    else:
        return randomunknownprompt()