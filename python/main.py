import os
import random
import time

import st_AI_n.wait
import st_AI_n.lazyness
import st_AI_n.st_AI_n__PLUS
import st_AI_n.lists
import st_AI_n.responses
import st_AI_n.lazyness.lazychances


os.system("cls")

while True:
    print("If you need help with anything feel free to ask.")

    prompt = input("Your prompt: ").lower()

    if st_AI_n.lazyness.lazychances.lazyapproach():
        continue

    if prompt == "bread":
        st_AI_n.lazyness.givemetoast()


    #Waiting for response
   #totaldots = random.randint(1,5) #1,60
   #timebetween = random.randint(1,1) / 10 #1,4 /10

   #st_AI_n.wait.wait(totaldots,timebetween)



    #The response
    print(st_AI_n.responses.response(prompt))
    time.sleep(2)
    os.system("cls")

    #AI needs a break
    st_AI_n.st_AI_n__PLUS.proptslimiteddef()