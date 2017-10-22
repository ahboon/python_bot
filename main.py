# Version: 0.1.0
# Note: Remember to do: pip install microsoftbotframework
# http://localhost:5000/api/message

import random
from microsoftbotframework import ReplyToActivity
from microsoftbotframework import MsBot
import apiReader
import envBotOne


def echo_response(message):
    """
    This function processes the user inputs.
    """
    random_number = str(random.randint(0, 10))
    if message["type"] == "message":
        ReplyToActivity(fill=message,
                        text="WHAT THE").send()                   
    if message["text"] == "Hello":
        ReplyToActivity(fill=message,
                        text=random_number).send()
    if message["text"] == "/getwestpm":
        pm = "The pm2.5 reading at west is: " + apiReader.ReadPM25Api("west")
        ReplyToActivity(fill=message,
                        text=pm).send()

# This is where the bot starts running
bot = MsBot()
bot.add_process(echo_response)

if __name__ == '__main__':
    bot.run()
    