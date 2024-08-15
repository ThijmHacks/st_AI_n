import st_AI_n.lists.lists


def checklists(prompt):
    hello = True
    unknown = False
    if prompt in lists.hello: return True
    else: unknown = True