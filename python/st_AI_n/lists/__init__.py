import secrets

from st_AI_n.lists.answers import unknownprompt, answers
from st_AI_n.lists.prompts import listwithpromts


def checkindir(prompt):
    listing = listwithpromts.keys()
    if prompt in listing:
        return listwithpromts[prompt]
    else: print(secrets.choice(unknownprompt))

def randomanswer(number):
    string = str(number)
    returnanswer = answers[string]
    answer = secrets.choice(returnanswer)
    return answer