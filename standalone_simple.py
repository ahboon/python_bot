# Simple Chat Bot
# A stupid Chat Bot that replies from greetings list


import random

greetings = ['Hello there!','Good day!','Hello','Hey..','Hi','hi','hello']

while True:
    userInput = input("\n" + "Your Input:")
    if userInput in greetings:
        random_res = random.choice(greetings)
        print(random_res)
    else:
        print("I did not get what you say....")
        
        
