from st_AI_n.lists.lists import listwithpromts



def checkindir(prompt):
    listing = listwithpromts.keys()
    if prompt in listing: return True