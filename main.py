# https://discordapp.com/api/oauth2/authorize?client_id=642149752951144468&permissions=8&scope=bot main bot
# https://discordapp.com/api/oauth2/authorize?client_id=651226650616528907&permissions=8&scope=bot test bot
#
#Hey! What are you doing here? The code is private! I'm fine with you looking over here as long as you don't copy anything.
#This code was 90% done by me with help of mazman and a website that got me started.
#So, if you found this, do not share it, please. This is private.
#Thank you for understanding,
#           -megamaz
import os.path, random, discord, sys, time, asyncio, random, traceback, datetime
from discord.ext import commands
from discord import member
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.utils import find
from pathlib import Path

env_path = Path(__file__).parents[0] / ".env"
prefix = '>'
is_in_conv = False
caller = 'megamaz#1020'
megamaz = 'change me pls'
load_dotenv(dotenv_path=env_path)
token = os.getenv('BOT_TOKEN')
client = discord.Client()
reply_request = []
last_message = 'BLANK'
wants_talk = 651226650616528907 #AdminBOT id
reason_request = []
user = client.get_user(12345678910)
trusted_users = "megamaz#1020".split()
number = False
start = time.time()
server_censor = []
char_list = [chr(x) for x in range(255)]
def get_milestone():
    milestone_reach = 1
    while milestone_reach < len(client.guilds):
        milestone_reach *= 10
    return milestone_reach


@client.event
async def on_ready():
    # ehehehheheeheh 42
    global prefix
    # DM call variables.
    global is_in_conv
    global caller
    global megamaz
    global presence
    global debug
    presence = r'Discord in {servers} servers'
    is_in_conv = False
    if str(client.user.name) == 'AdminBOT experimental':
        prefix = '<'
        version = input(f'Test Messge > ')
        
        await client.change_presence(activity=discord.Game(name=f"{version}"))
        megamaz = client.get_user(604079048758394900)
    if str(client.user.name).lower() == 'adminbot':
        prefix = '>'
        version = '1.1'
        await client.change_presence(activity=discord.Game(name=f'Discord in {len(client.guilds)} Servers'))
        megamaz = client.get_user(604079048758394900)
    print(f'{client.user.name} Is online and usable.')
    caller = client.get_user(604079048758394900)

    debug = client.get_channel(736419014171164683)
    await DebugMess('info', 'AdminBOT has come online')

async def DebugMess(debugtype, text):
    
    debugtype = str(debugtype)
    with open(get_local_path('debug.txt'), 'a') as debugtext:
        debugtext.write((f'{debugtype.upper()} ({datetime.datetime.now()}):    {text}\n'))

    return await debug.send(f'{debugtype.upper()} ({datetime.datetime.now()}):    `{text}`')

def ChangePresence(presence):
    presence = presence.split()
    for x in presence:
        if x.startswith('{') and x.endswith('}'):
            x.replace('{', '').replace('}', '')
            if x == 'servers':
                x = len(client.guilds)
    DebugMess('INFO', 'Updated presence')
    return ' '.join(presence)


@client.event
async def on_guild_join(guild):
    channel = client.get_channel(656176573703127042)
    await channel.send(f"{client.user.name} just joined a server! Server number {len(client.guilds)}")
    await client.change_presence(activity=discord.Game(name=ChangePresence(presence)))
    milestone = client.get_channel(659839146449305635)
    if len(client.guilds) == get_milestone():
        await milestone.send(f'Congratulations, server `{guild.name}` for being the **__{get_milestone()}th__** Server!')
    
    DebugMess('INFO', 'AdminBOT has joined a server')

def check_admin(author):
    return (author).guild_permissions.administrator

def get_random_message():
    random_message = get_local_path('failsafe-random.md')
    random_desc = []
    with open(random_message, 'r') as random_mess:
        random_mess_len = random_mess.read().splitlines()
        for check in random_mess_len:
            if check.startswith('||'):
                continue
            else:
                random_desc.append(check)
    return random_desc


def help_page(page):
    pages = [
        discord.Embed(title="Help Page 1", description="*For more help, join the [Support Server](https://discord.gg/z76mn4r)*", colour=discord.Color.from_rgb(255,180,0))
        .add_field(value=f"[Argument] *This argument is **required** for the command to work.*\n(Argument) *This argument is **optional** and command will work even without it.*", name="Legend")
        .add_field(name="Admins Command", value="*Prefix `>`*\n", inline=False)
        .add_field(name=f'censor [word]', value="Will add a word to the censored list.", inline=False)
        .add_field(name=f'uncensor [word]', value="Will remove a word from the censored list", inline=False)
        .add_field(name=f"censored (word)", value="Will send you a list of the censored words / check if the word is censored.", inline=False)
        .add_field(name="announce [channel ID] [announcement] ", value="Will make an announcement in the specified channel", inline=False)
        .add_field(name="kick [user mention]", value="Will kick the specified user from the server", inline=False)
        .add_field(name="ban [user mention]", value="Will ban the specified user from the server", inline=False)
        .add_field(name="clear_data", value="Will completely clear AdminBOT's data on the server.", inline=False)
        .set_footer(text="AdminBOT", icon_url="https://cdn.discordapp.com/avatars/642149752951144468/2e61dc7181901f3e491100522b700eb4.png?size=128"),


        discord.Embed(name="Help Page 2", description="*For more help, join the [Support Server](https://discord.gg/z76mn4r)*", colour=discord.Color.from_rgb(255,180,0))
        .add_field(value=f"[Argument] *This argument is **required** for the command to work.*\n(Argument) *This argument is **optional** and command will work even without it.*", name="Legend")
        .add_field(name="Everyone Command", value="*Prefix `>`*\n", inline=False)
        .add_field(name="changelog", value="Will give you AdminBOT's latest changelog", inline=False)
        .add_field(name="uptime", value="Will give you AdminBOT's uptime", inline=False)
        .add_field(name="help (page number)", value="Will give you this list.", inline=False)
        .add_field(name="population", value="Will give you your server's population (includes bots.)", inline=False)
        .add_field(name="failsafe", value="Will tell you what the failsafe does.", inline=False)
        .set_footer(text="AdminBOT", icon_url="https://cdn.discordapp.com/avatars/642149752951144468/2e61dc7181901f3e491100522b700eb4.png?size=128"),

    ]
    return pages[page]
def get_local_path(filename):
    return Path(__file__).parents[0] / filename


def time_convert(sec):
  mins = int(sec / 60)
  hours = int(mins // 60)
  days = int(hours // 24)
  sec = sec % 60
  mins = mins % 60
  hours = hours % 24
  return f'{days} days, {hours}h {mins}min {int(sec)}sec'


                
def update_censor(server, AR, censor=''):
    words = []
    server = str(server)
    censor_path = get_local_path(f'{server}.txt')
    if os.path.exists(censor_path):
        with open(censor_path, 'r') as list_censor:
            words = list_censor.read().splitlines()
    else:
        with open(censor_path, 'w'):
            True
    if AR == 'add':
        if censor in words:
            return 'double'

        elif len(words) >= 25:
            return 'limit'
        else:
            with open(censor_path, 'a') as censor_fd:
                censor_fd.write(f'{censor}\n')
    elif AR == 'remove':
        if censor in words:
            words.remove(censor)
            with open(censor_path, 'w') as censor_fd:
                words = list(words)
                for x in range(len(words)):
                    censor_fd.write(f'{words[x]}\n')
        else:
            return 'not_in_list'
    elif AR == 'read':
        with open(censor_path, 'r') as censor_fd:
            words = censor_fd.read().splitlines()
            return words
    elif AR == 'clear':
        with open(censor_path, 'w') as censor_fd:
            censor_fd.truncate()
            return 'complete'
    


def Get_Commands(): # Simplest way I could think of that could get all the commands down to one list.
    bot_commands = "censor uncensor censored clear_censor announce kick ban join clear_data".split()
    return bot_commands

    

def random_char():
    return str(random.choice(char_list))

# All commands are stored in on_message
@client.event
async def on_message(message):
    try:

        breaking = False
        global start

        if str(message.channel.type) == 'text':
            
            global last_message
            breaking = False
            def check_message(command):
                return message.content.lower() == f'{prefix}{command}'
            
            if message.author == client.user:
                return
            
            
            if message.author.bot:
                return
            else:
                # creator specific commands.


                if int(message.author.id) == 604079048758394900:
                    if str(message.content).lower() == f'{prefix}embed':
                        DebugMess('info', 'Debug command triggered')
                        await message.channel.send(content="content", embed=discord.Embed(type="rich", title="title", description="description [Google](http://google.com)", colour=discord.Color.from_rgb(255,180,0)).set_footer(text="FooterText", icon_url="https://cdn.discordapp.com/attachments/643995974007652353/729431318198222939/unknown.png").set_image(url="https://cdn.discordapp.com/attachments/643995974007652353/729432020744142848/unknown.png").set_thumbnail(url="https://cdn.discordapp.com/attachments/643995974007652353/729432224709083336/unknown.png").set_author(name="AuthorName", icon_url="https://cdn.discordapp.com/attachments/643995974007652353/729431085490110495/unknown.png", url="http://google.com").add_field(name='FieldName', value="FieldValue [Google](http://google.com)", inline=True))
                
                
                
                
                number = False
                # Normal user commands
                last_message = message.content
                if str(message.content).startswith(f'{prefix}help'):
                    if str(message.content) == f'{prefix}help':
                        await message.channel.send(embed=help_page(0))
                    else:
                        if not str(message.content)[6:] in "1 2".split():
                            return
                        else:
                            page_number = int(str(message.content)[6:])
                            await message.channel.send(embed=help_page(page_number-1))

                if check_message('population'):
                    await message.channel.send(f"checking...")
                    check_start = time.time()
                    for y in range(len(client.guilds)):
                        if str(message.guild) == str(client.guilds[y].name):
                            await message.channel.send(f'{client.guilds[y].member_count}. Respond Time:{(time.time() - check_start)*100}ms')
                        else:
                            continue
                if str(message.content).lower() == f'{prefix}failsafe':
                    emoji = '\N{Warning Sign}'
                    await message.channel.send(embed=
                    discord.Embed(title="Failsafe", description="Whenever the failsafe is triggered, AdminBOT will react to the message with :warning:. A message will be sent to the creator, so worry not!", colour=discord.Color.from_rgb(255,180,0))
                    )
                
                if str(message.content).lower().startswith(f'{prefix}uptime'):
                    current = time.time() - start
                    current = time_convert(current)
                    await message.channel.send(embed=discord.Embed(title='Uptime', description=f'The current uptime is {current}', colour=discord.Color.from_rgb(255,180,0)))
                
                if str(message.content).startswith(f'{prefix}changelog'):
                    changelog = get_local_path('changelog.txt')
                    with open(changelog, 'r') as changelog_fd:
                        text_change = changelog_fd.read().splitlines()
                        date = text_change[0]
                        text_change.remove(date)
                        text_change = '\n'.join(text_change)
                    await message.channel.send(embed=discord.Embed(title='Changelog').add_field(name=f'{date}', value=text_change), colour=discord.Color.from_rgb(255,180,0))
                
                if str(message.content).startswith(f"{prefix}feedback"):
                    await message.channel.send(embed=discord.Embed(title="Feedback", description="Thank you for the feedback! Click [Here](https://forms.gle/mzDMTPsE8WXiKYZ39) for the form."))
                
                if str(message.content).startswith(f"{prefix}destroy"):
                    
                    
                    
                    if str(message.content) == f"{prefix}destroy":
                        await message.channel.send(embed=discord.Embed(title="Fail", description="Could not delete message as there was no content and no timestamp.", colour=discord.Color.from_rgb(150,0,0)))
                        await message.delete()
                    else:
                        limit = await message.channel.send(f'Your message will be deleted in {str(message.content).split()[1]} seconds.')
                        await asyncio.sleep(int(str(message.content).split()[1]))
                        await message.delete()
                        await limit.delete()
                
                if str(message.content).startswith(f'{prefix}privacy') or str(message.content).startswith(f"{prefix}policy"):
                    await message.channel.send(embed=discord.Embed(title="Privacy Policy", description='*If you have any question, join the [Support Server](https://discord.gg/z76mn4r)*.', colour=discord.Color.from_rgb(255,180,0))
                    .add_field(name="Policy", value="""
-AdminBOT will not send any information about the user to the creator, unless a bug has been triggered in which case **Message content (exluding images), server name, username/ID** will be sent to the creator.
-Censored word list will remain private to server and will not be shared in any way.
-Any sort of command usage will not be shared unless it has triggered a bug.
-AdminBOT will save server data after being kicked or banned. To clear data, use `clear_data` **Warning: Usage of this command cannot be undone.**
""",

inline=False)
                    )


                #Admin only commands
                if message.content.lower().startswith(f"{prefix}censor") and message.content.lower()[:9] != f'{prefix}censored' and check_admin(message.author):
                    if len(message.content) == 7:
                        # await message.channel.send(embed=discord.Embed/
                        None
                    else:
                        if update_censor(int(message.guild.id), 'add', str(message.content[8:].lower())) == 'double':
                            await message.channel.send(embed=discord.Embed(title="Fail", description="Could not add censored word as it is already in the list.", colour=discord.Color.from_rgb(150,0,0)))
                        elif update_censor(int(message.guild.id), 'add', str(message.content)[8:].lower()) == 'limit':
                            await message.channel.send(embed=discord.Embed(title="Fail", description='It seems you have reached your limit of 25 words. There is currently no way of pushing that limit higher.'))
                        else:
                            await message.channel.send(embed=discord.Embed(title='Success', colour=discord.Color.from_rgb(255,180,0), description='A word was successfully added to your censored word list.'))
                            await message.delete()
                            return
                elif message.content.lower().startswith(f"{prefix}uncensor") and check_admin(message.author):
                    if update_censor(int(message.guild.id), 'remove', message.content.lower()[10:]) == 'not_in_list':
                        await message.channel.send(embed=discord.Embed(title="Fail", description="Could not remove word as it is not in list.", colour=discord.Color.from_rgb(150,0,0)))
                    else:
                        await message.channel.send(embed=discord.Embed(title='Success',colour=discord.Color.from_rgb(250,180,0), description='Successfully removed a word from the list.'))
                elif message.content.lower().startswith(f"{prefix}censored") and check_admin(message.author):
                    if len(message.content) == 9: 
                        words = update_censor(int(message.guild.id), 'read')
                        censored_call = client.get_user(message.author.id)
                        await censored_call.create_dm()
                        await censored_call.send(f'Your censored list is: `{words}`')
                        await message.channel.send("Dm'ed you the censored words!")
                        await message.delete()
                    else:
                        if str(message.content).lower()[10:] in update_censor(int(message.guild.id), 'read'):
                            await message.channel.send(embed=discord.Embed(title='Word is in list', description='Word checked was in the lsit.'))
                            return
                        else:
                            await message.channel.send(embed=discord.Embed(title='Word is not in list', description='Word checked was not in censored list.'))
                elif message.content.lower().startswith(f"{prefix}clear_censor") and check_admin(message.author):
                    list_length = len(update_censor(int(message.guild.id), 'read'))
                    update_censor(int(message.guild.id), 'clear')
                    await message.channel.send(embed=emb_text('Success', 'Successfully cleared a list', f'Successfully cleared the censored list that contained {list_length} items.'))
                elif message.content.lower()[:9] == f"{prefix}announce" and check_admin(message.author):
                    if len(message.content) == 9:
                        await message.channel.send(embed=emb_text('Error to send announcement', 'Could not send announcement', 'Specify channel ID', 'fail'))
                    elif len(message.content) <= 28:
                        await message.channel.send(embed=emb_text('Error to send announcement', 'Could not send announcement', 'Channel ID not long enough' , 'fail'))
                    if True:
                        for check_id in range(len(message.content[10:28])):
                            if not message.content.lower()[10:28][check_id] in "1 2 3 4 5 6 7 8 9 0".split():
                                await message.channel.send(embed=emb_text('Error to send announcement', 'Could not send announcement', 'Channel ID must contain numbers only', "fail"))
                                number = True
                                break
                            else:
                                continue
                    if not number:
                        number = False
                        channel = client.get_channel(int(message.content[10:28]))
                        try:
                            if message.guild != channel.guild:
                                await message.channel.send(embed=emb_text('Error', 'Could not send announcement', 'Channel ID from different server.'))
                            await channel.send(f'Announcement from {message.author.mention}: {message.content[28:]}')
                            await message.channel.send(embed=emb_text('Success', 'Successfully sent announcement', f'Successfully sent announcement in `#{channel}`'))                      
                        except:
                            await message.channel.send(embed=emb_text('Error', 'Could not send announcement', 'Channel ID from different server.'))
                
                elif str(message.content).lower().startswith(f"{prefix}kick") and check_admin(message.author):
                    if len(message.content) == len(f'{prefix}kick'):
                        await message.channel.send(embed=emb_text("Error", 'Could not kick', 'Specify a user to kick', 'fail'))
                    elif len(message.mentions) == 0:
                        await message.channel.send(embed=emb_text("Error", 'Could not kick', 'There was no user to kick', 'fail'))
                    else:
                        await message.guild.kick(message.mentions[0], reason=str(message.author)+str(message.content)[len(str(message.mentions[0].id))+5+len(f'{prefix}kick'):])
                        await message.channel.send(embed=emb_text('Success', f'Successfully kicked {message.mentions[0]}', f'{message.mentions[0]} was successfully kicked from {message.guild.name}'))
                    
                elif str(message.content).lower().startswith(f"{prefix}ban") and check_admin(message.author):
                    if len(message.content) == len(f'{prefix}ban'):
                        await message.channel.send(embed=emb_text("Error", 'Could not ban', 'Specify a user to ban', 'fail'))
                    elif len(message.mentions) == 0:
                        await message.channel.send(embed=emb_text("Error", 'Could not ban', 'There was no user to ban', 'fail'))
                    else:
                        await message.guild.ban(message.mentions[0], reason=str(message.author)+str(message.content)[len(str(message.mentions[0].id))+5+len(f'{prefix}ban'):])
                        await message.channel.send(embed=emb_text('Success', f'Successfully banned {message.mentions[0]}', f'{message.mentions[0]} was successfully banned from {message.guild.name}'))
                
                elif str(message.content).startswith(f"{prefix}reaction_role") and check_admin(message.author):
                    if str(message.content) == (f"{prefix}reaction_role"):
                        await message.channel.send(embed=emb_text('Error', 'Could Not Add Reaction Role', 'Please Specify Channel ID and Emoji.'))

                elif str(message.content).startswith(f'{prefix}join') and check_admin(message.author):
                    if str(message.content) == f'{prefix}join':
                        await message.channel.send(embed=emb_text('Could Not Set', 'Include Channel ID', 'Please include channel ID along with the command', 'fail'))
                    else:
                        channel_found = False
                        JoinsPath = get_local_path('ChannelJoins.txt')
                        # Grab all the list items 
                        with open(JoinsPath, 'r') as joins:
                            JoinsList = joins.read().splitlines()
                        # Then write (this it to make sure the guild isn't already registered)
                        # The info will be written as [Server ID|Channel ID]
                        with open(JoinsPath, 'w+') as joins2:
                        
                            for x in range(len(JoinsList)):
                                
                                if int(JoinsList[x].split('|')[0]) == int(message.guild.id):
                                    await message.channel.send('Your server was already found. Updating to new channel.')
                                    JoinsList[x] = f'{message.guild.id}|{(str(message.content).split())[1]}'
                                    channel_found = True
                                    joins2.write('\n'.join(JoinsList))
                                    break
                                else:
                                    continue
                            if not channel_found:
                                JoinsList.append(f'{message.guild.id}|{str(message.content).split()[1]}')
                                joins2.write('\n'.join(JoinsList))
                                await message.channel.send('Your Channel was successfully registered.')
                            else:
                                await message.channel.send('Your Channel was successfully registered.')
                            
                elif str(message.content) == f"{prefix}clear_data" and check_admin(message.author):
                    await message.channel.send(embed=discord.Embed(title=":warning: WARNING :warning:", description=f"This action cannot be undone! If you are sure you want to do this, type in `{prefix}clear_data confirm` which will remove all your censored words, user prefs, and `{prefix}join` command data. If you have a problem with my bot, you can join the [Support Server](https://discord.gg/z76mn4r) or [Give Feedback](https://forms.gle/mzDMTPsE8WXiKYZ39).", colour=discord.Color.from_rgb(150,0,0)))
                
                elif str(message.content) == f'{prefix}clear_data confirm' and check_admin(message.author):
                    status = await message.channel.send("Clearing Data...")
                    os.remove(get_local_path(str(message.guild.id) + ".txt"))
                    await status.edit(content="Removed censored words...")

                elif str(message.content).startswith(f'{prefix}clean') and check_admin(message.author):
                    if str(message.content) == f'{prefix}clean':
                        message.channel.send(embed=discord.Embed(title="Please include an amount", description="Please include an amount of message to remove."))
                    else:
                        try:
                            amount = int(str(message.content).split()[1])
                            if amount > 100:
                                await message.channel.send("Amount to delete was too big.")
                                return
                            else:
                                async for message in message.channel.history(limit=amount, oldest_first=False):
                                    await message.delete()
                        except:
                            message.channel.send(embed=discord.Embed(title="Please make amount number", description="Could not delete messages because amount wasn't a number"))

                elif not check_admin(message.author):
                    bot_commands = Get_Commands()
                    for check in bot_commands:
                        if str(message.content).startswith(f'{prefix}{check}'):
                            await message.channel.send(embed=emb_text('Could Not Use Command', 'Not Enough Permission', f"It seems you don't have permission to use this command. Oops!", 'fail'))
                            break

                            
       
       

       # this is my most proud area!! 
                if not check_admin(message.author):
                    if not message.guild.owner == message.author.id:

                        for list_fd in range(len(update_censor(int(message.guild.id), 'read'))):
                        
                            for _ in range(len(update_censor(int(message.guild.id), 'read')[list_fd])):
                        
                                for message_fd in range(len(''.join(str(message.content).split()))):
                                    
                                    if ''.join(str(message.content).lower().split())[message_fd:message_fd+len(update_censor(int(message.guild.id), 'read')[list_fd])].lower() == update_censor(int(message.guild.id), 'read')[list_fd].lower():
                                        censoring = await message.channel.send(embed=emb_text('User said a censored word', f'{message.author} said a censored word', f'Hey {message.author.mention}, you said a censored word! Your message has been removed.'))
                                        await message.delete()
                                        breaking = True
                                        await asyncio.sleep(30)
                                        await censoring.delete()
                                        break
                                    else:
                                        continue 
                                if breaking:
                                    break
                            if breaking:
                                breaking = False
                                break            
        # DM section
        if str(message.channel.type) == "private":
            global is_in_conv
            global caller
            global megamaz
            global presence
            if int(message.author.id) == int(client.user.id):
                DebugMess('INFO', 'detected self DM')
                return
            if message.author.id == caller.id and is_in_conv:
                await megamaz.send(f"{caller.name} says: `{message.content}`")
            elif int(message.author.id) != 604079048758394900: # my ID
                if int(message.author.id) == client.user.id:
                    return
                else:
                    if str(message.content).startswith(f'{prefix}help'):
                        if str(message.content).endswith('DM'):
                            await message.channel.send("use `>help [command]` get help on a certain command. ")
                            await message.channel.send("use `>contact [message]` To contact the creator.")
                            await message.channel.send("use `>call` to have a live conversation with the creator.")
                        elif str(message.content).endswith(f'population'):
                            await message.channel.send('Simply type in `>population`, and the amount of people (both bot and user) will be counted. Respond time is pretty useless on its own.')
                        elif str(message.content).endswith(f'uptime'):
                            await message.channel.send("Gives the bot's uptime since it's last launch.")
                        elif str(message.content).endswith(f'changelog'):
                            await message.channel.send("Changelog very simply gives my latest changes to you in a nice changelog.")
                        elif str(message.content).endswith(f'censor'):
                            await message.channel.send("Censor a word by using this command. (Very simply type `>censor` then the word you want)")
                        elif str(message.content).endswith(f'uncensor'):
                            await message.channel.send("I'm not even sure that's a word. Anyways, this uncensors a word in your list. Use by typing  `uncensor [word]` and replacing [word] with a word in your list.")
                        elif str(message.content).endswith(f'censored'):
                            await message.channel.send("DM's you the list of censored words, or include a word afterwards to check if it's censored.")
                        elif str(message.content).endswith(f'announce'):
                            await message.channel.send("Complicated command to use. First, type `>announce`. Then, right-click on the channel where you want the announcement to go in, and click `copy ID`. Then, paste the ID by doing `ctrl+v` and type in the announcement. Simple!")
                        elif str(message.content).endswith(f'kick'):
                            AdminBOT = client.get_user(642149752951144468)
                            await message.channel.send(f"Type in `>kick` and then mention the user you want to kick (to mention, type in @ and then the user you want to kick. E.X: {AdminBOT.mention})")
                        elif str(message.content).endswith(f'ban'):
                            AdminBOT = client.get_user(642149752951144468)
                            await message.channel.send(f"Type in `>ban` and then mention the user you want to ban (to mention, type in @ and then the user you want to ban. E.X: {AdminBOT.mention})")
                        elif str(message.content).endswith('join'):
                            await message.channel.send('Will send a message for every user that joins the server in the specified channel. Use by doing `>join [Channel ID]`. (To unregister, you can just delete the channel. Will get on update on that soon.)')
                        else: 
                            await message.channel.send('Please specify what you need help with, or just include command name (exclude the [])')
                    else:
                        await message.channel.send("Sorry, I didn't recognize that command. Do `>help DM` for DM commands, or be sure that the command starts with `>`")
                if str(message.content).startswith(f'{prefix}contact'):
                    megamaz = client.get_user(604079048758394900)
                    await megamaz.send(str(message.content)[len('>contact'):])
                    await message.channel.send(f'Your message `{str(message.content)[len(">contact"):]}` has been sent to megamaz. If you want a response, do join my support server; https://discord.gg/z76mn4r')
                
                elif str(message.content).startswith(f'{prefix}call'):
                    await message.channel.send(f'Calling `megamaz` (my creator) with reason {str(message.content)[len(">call"):]}...')
                    await caller.send('Your call was overwritten by someone else'+"'s"+' call. Try again later.')
                    caller = client.get_user(message.author.id)
                    megamaz = client.get_user(604079048758394900)
                    if not is_in_conv:
                        await megamaz.send(f'{message.author} wants to speak with reason `{str(message.content)[len(">call"):]}`. Type `>accept` to accept or `>deny` to deny.')
                    if is_in_conv:
                        await message.channel.send('megamaz is already in a call. Try again later.')
                

            elif int(message.author.id) == 604079048758394900:
                if str(message.content).startswith(f'{prefix}accept'):
                    await caller.send('megamaz accepted!')
                    await megamaz.send('You accepted successfuly')
                    is_in_conv = True
                
                if str(message.content).startswith(f'{prefix}deny'):
                    await caller.send('megamaz denied.')
                    await megamaz.send('You denied successfuly')
                
                if str(message.content).startswith(f'{prefix}end'):
                    is_in_conv = False
                    await caller.send('megamaz ended the call.')
                    await megamaz.send('call ended.')
                
                if is_in_conv:
                    await caller.send(f"megamaz says: `{message.content}`")
                

                if str(message.content) == f'{prefix}update':
                    await client.change_presence(activity=discord.Game(name=f'DM for help|{len(client.guilds)} Servers'))
                    await message.channel.send("Updated server number")
                

                if str(message.content).startswith(f"{prefix}status"):
                    if str(message.content).endswith("reset"):
                        await client.change_presence(activity=discord.Game(name=f'Discord in {len(client.guilds)} Servers'))
                        await message.channel.send('Status reset')
                    else:
                        await client.change_presence(activity=discord.Game(name=ChangePresence(' '.join(str(message.content).split()[1:]))))
                        presence = ' '.join(str(message.content).split()[1:])
                 
    
    
    
    #EEEEEEEEEE, I BUG-ged!
    except Exception as error:
        DebugMess('warn', "AdminBOT's failsafe has been triggered")
        random_desc = get_random_message()
        channel = client.get_channel(650837623295705118)
        # the beneath line is the old failsafe. It was too big and got replaced with a simple warning reaction. Emb_text no longer exists.
        #await message.channel.send(embed=emb_text('Failsafe', random.choice(random_desc), f'It seems your message has bugged me out! A message has been sent to the creator. To see if it will get fixed, join my support server at: https://discord.gg/z76mn4r', 'fail'))
        emoji = '\N{Warning Sign}'
        await message.add_reaction(emoji)
        await channel.send(embed=discord.Embed(title=random.choice(random_desc), description=f'''Message: "{str(message.content)}"
Channel Type: "{message.channel.type}"
Channel Name: "{message.channel}"
Server: "{str(message.guild)}"
Is bot: "{message.author.bot}"
Author name: "{message.author}"
Author ID: "{message.author.id}"\n
Error message: `{error}`''', colour=discord.Color.from_rgb(150,0,0)))


@client.event
async def on_message_edit(before, after):
    if not check_admin(after.author):
        breaking = False
        if not after.guild.owner == after.author.id:
            for list_fd in range(len(update_censor(int(after.guild.id), 'read'))):
                for len_item in range(len(update_censor(int(after.guild.id), 'read')[list_fd])):
                    len_item = len_item # Clearing up the 'unused variable' error. Makes code look cleaner.
                    for after_fd in range(len(''.join(str(after.content).split()))):
                        if ''.join(str(after.content).lower().split())[after_fd:after_fd+len(update_censor(int(after.guild.id), 'read')[list_fd])].lower() == update_censor(int(after.guild.id), 'read')[list_fd].lower():
                            censoring = await after.channel.send(embed=emb_text('User said a censored word', f'{after.author} said a censored word', f'Hey {after.author.mention}, you said a censored word! Your message has been removed.'))
                            await after.delete()
                            breaking = True
                            await asyncio.sleep(30)
                            await censoring.delete()
                            break
                        else:
                            continue 
                    if breaking:
                        break
                if breaking:
                    breaking = False
                    break         
@client.event
async def on_member_join(member):
    JoinsPath = get_local_path('ChannelJoins.txt')
    with open(JoinsPath, 'r') as joins2:
        JoinsList2 = joins2.read().splitlines()
        for x in range(len(JoinsList2)):
            if int(JoinsList2[x].split('|')[0]) == int(member.guild.id):
                join = client.get_channel(int(JoinsList2[x].split("|")[1]))
                await join.send(f'{member.mention} just joined the server!')
            else:
                continue



if __name__ == "__main__":
    print("Starting...")
    client.run(token)