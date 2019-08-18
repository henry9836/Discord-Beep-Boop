# Work with Python 3.6
import discord
import time
from random import randint

TOKEN = 'XXXXXXXXXXX'
client = discord.Client()
triggerchar = '!'

#Game Data
'''

Active users States:

0 - no game active, no Welcome
1 - Welcomed, no game active
2 - Game 1 Active

saves_game1:
0 - No Save


'''


saves_game1 = {}
active_games = {}


def text_game(message, user):
    msg = 'There was an error with your request {0.author.mention}'
    print(user)
    print(message)
    print(saves_game1.get(user))
    if user not in saves_game1:
        saves_game1[user] = 0
        active_games[user] = 1
        print("new user " + user + "Added!")
        msg = 'Welcome to the games room {0.author.mention} \n Please select a game ('+triggerchar+'game <option>) \n ``` 1.  Something```'
    else:
        if (active_games[user] == 0):
            msg = 'Welcome back to the games room {0.author.mention} \n Please select a game ('+triggerchar+'game <option>) \n ``` 1.  Something```'
            active_games[user] = 1
        elif (active_games[user] == 1):
             if (message == (triggerchar+'game 1')):
                active_games[user] = 2
                msg = 'W.I.P'
             else:
                msg = 'Please select a game ('+triggerchar+'game <option>) {0.author.mention} \n ``` 1.  Something```'
        else:
            #start/continue game
            msg = 'Welcome back to the game room {0.author.mention}'
    print(saves_game1)
    return msg

@client.event
async def on_message(message): #when we see a message
    if message.author == client.user: #do not reply to self
        return
    if message.content.startswith(triggerchar + 'help'): #is the message help?
        await client.send_message(message.author, "Commands: ```\n !help \n !8ball <Question>```")
    elif message.content.startswith(triggerchar + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith(triggerchar + '8ball' + ' '):
        tmp = randint(0, 18)
        if tmp == 1:
                msg = 'It is certain. {0.author.mention}'.format(message)
        elif tmp == 2:
                msg = 'It is decidedly so. {0.author.mention}'.format(message)
        elif tmp == 3:
                msg = 'Without a doubt. {0.author.mention}'.format(message)
        elif tmp == 4:
                msg = 'Yes - definitely. {0.author.mention}'.format(message)
        elif tmp == 5:
                msg = 'Most likely. {0.author.mention}'.format(message)
        elif tmp == 6:
                msg = 'As I see it, yes. {0.author.mention}'.format(message)
        elif tmp == 7:
                msg = 'Outlook good. {0.author.mention}'.format(message)
        elif tmp == 8:
                msg = 'Yes. {0.author.mention}'.format(message)
        elif tmp == 9:
                msg = 'Signs point to yes. {0.author.mention}'.format(message)
        elif tmp == 10:
                msg = 'Reply hazy, try again. {0.author.mention}'.format(message)
        elif tmp == 11:
                msg = 'Better not tell you now. {0.author.mention}'.format(message)
        elif tmp == 12:
                msg = 'Cannot predict now. {0.author.mention}'.format(message)
        elif tmp == 13:
                msg = 'Concentrate and ask again. {0.author.mention}'.format(message)
        elif tmp == 14:
                msg = "Don't count on it. {0.author.mention}".format(message)
        elif tmp == 15:
                msg = 'My reply is no. {0.author.mention}'.format(message)
        elif tmp == 16:
                msg = 'My sources say no. {0.author.mention}'.format(message)
        elif tmp == 17:
                msg = 'Outlook not so good. {0.author.mention}'.format(message)
        elif tmp == 18:
                msg = 'Very doubtful. {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith(triggerchar + 'game'):
        msg = text_game(message.content, message.author.id);
        msg = msg.format(message)
        await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

try:
    client.run(TOKEN)
except:
    print("Could not create the client token check that the TOKEN KEY is valid")
