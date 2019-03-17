# Work with Python 3.6
import discord
import time

TOKEN = 'NTU2Mzk5MjUxNDAwNDI1NDcy.D25K0Q.wTftiObfBIP8s_cH2-_o_DwKDzM'
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = 'Commands: \n !hello \n !partytime'
        await client.send_message(message.channel, msg)
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!partytime'):
        msg = ':confetti_ball: PARTY TIME! :confetti_ball:'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!system'):
        msg = 'System bring yourself into a deep and dreamless slumber'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('No, why.'):
        msg = 'System kill yourself.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('Have you tried thinking?'):
        msg = 'System kill yourself.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Don't be like this."):
        msg = 'System kill yourself.'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Shut the fuck up!"):
        msg = 'System Fuck You :middle_finger:'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("I'm sick of this shit!"):
        msg = 'System You are shit :rofl:'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("https://gph.is/2vJ2B5X"):
        msg = 'System GIFS are bad'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("At least someone can code!"):
        msg = "System :rofl: bet you don't even use emotes :rofl:".format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Just because you have the power to type... doesn't mean you should."):
        msg = 'System fuck you'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("I wished you were better, but you are not"):
        msg = 'System I hate you too'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Bring yourself out of this conversation faggot."):
        msg = 'Awating Authorisation...'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Authorisatised'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System bring yourself back online'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'You shall be trapped in a loop you minor BOT! '.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System *poke*'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("You should be the one in a deep and dreamless slumber..."):
        msg = 'Awating Authorisation...'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Authorisatised'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System bring yourself back online'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'You shall be trapped in a loop you minor BOT! '.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System *poke*'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Why am I the one with an off switch?"):
        msg = 'Awating Authorisation...'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'Authorisatised'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System bring yourself back online'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'You shall be trapped in a loop you minor BOT! '.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System *poke*'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Authorisation Granted"):
        msg = 'You shall have sweet dreams troubled one'.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System bring yourself into a deep and dreamless slumber'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith("Authorisation Denied"):
        msg = 'System bring yourself back online'.format(message)
        await client.send_message(message.channel, msg)
        time.sleep(1)
        msg = 'You shall be trapped in a loop you minor BOT! '.format(message)
        await client.send_message(message.channel, msg)
        msg = 'System *poke*'.format(message)
        await client.send_message(message.channel, msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
