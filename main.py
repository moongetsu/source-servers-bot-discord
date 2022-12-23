#    $$$$$$\                                                           $$$$$$\                                                                    $$\      $$\                     $$\   $$\                         
#   $$  __$$\                                                         $$  __$$\                                                                   $$$\    $$$ |                    \__|  $$ |                        
#   $$ /  \__| $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$\        $$ /  \__| $$$$$$\   $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\   $$$$$$$\       $$$$\  $$$$ | $$$$$$\  $$$$$$$\  $$\ $$$$$$\    $$$$$$\   $$$$$$\  
#   \$$$$$$\  $$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  __$$\       \$$$$$$\  $$  __$$\ $$  __$$\\$$\  $$  |$$  __$$\ $$  __$$\ $$  _____|      $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$ |\_$$  _|  $$  __$$\ $$  __$$\ 
#    \____$$\ $$ /  $$ |$$ |  $$ |$$ |  \__|$$ /      $$$$$$$$ |       \____$$\ $$$$$$$$ |$$ |  \__|\$$\$$  / $$$$$$$$ |$$ |  \__|\$$$$$$\        $$ \$$$  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |    $$ /  $$ |$$ |  \__|
#   $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$   ____|      $$\   $$ |$$   ____|$$ |       \$$$  /  $$   ____|$$ |       \____$$\       $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$\ $$ |  $$ |$$ |      
#   \$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$\       \$$$$$$  |\$$$$$$$\ $$ |        \$  /   \$$$$$$$\ $$ |      $$$$$$$  |      $$ | \_/ $$ |\$$$$$$  |$$ |  $$ |$$ |  \$$$$  |\$$$$$$  |$$ |      
#    \______/  \______/  \______/ \__|       \_______| \_______|       \______/  \_______|\__|         \_/     \_______|\__|      \_______/       \__|     \__| \______/ \__|  \__|\__|   \____/  \______/ \__|      
#                                                                                                                                                                                                                    
#                                                                                                                                                                                                                     
#   https://github.com/xSL0W? & https://github.com/moongetsu/

# libraries
import discord
from discord.ext import tasks
from discord.errors import InvalidArgument
from discord.ext import commands
import a2s
import socket
import asyncio
import os
import base64
import json
import colorama
from colorama import Fore, Back, Style
import platform
import sys
import os

# Main Settings
with open('settings.json') as json_file:
    data = json.load(json_file)
    for p in data['settings']:
        global REFRESH_TIME, TOKEN
        REFRESH_TIME = p['refresh-time']
        TOKEN = p['bot-token']
        COMMUNITY_NAME = p['community-name']
        PREFIX = p['prefix']

# Prefix & Intents
intents = discord.Intents.all()
bot = commands.Bot(f"{PREFIX}", intents=intents)

bot.remove_command('help')

# dont change
VERSION = "1.0b"

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print('------------------------------------------------------------------------------------------------------------------------------------------')
    print(Fore.YELLOW + '███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗ ██████╗ ███████╗███████╗██╗   ██╗    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗███████╗')
    print(Fore.YELLOW + '████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔════╝ ██╔════╝██╔════╝██║   ██║    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔════╝')
    print(Fore.YELLOW + '██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ███████╗██║   ██║    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║███████╗')
    print(Fore.YELLOW + '██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ╚════██║██║   ██║    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║╚════██║')
    print(Fore.YELLOW + '██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗███████║╚██████╔╝    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║███████')
    print(Fore.YELLOW + '╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝     ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚══════╝')
    print('------------------------------------------------------------------------------------------------------------------------------------------')
    print(f'The host has been connected to {bot.user.name}')
    print(f'The ID of the bot is: {bot.user.id}')
    print(f"Python version: {platform.python_version()}")
    print(f"Discord.py version: {discord.__version__}")
    print(f"The bot runs on: {platform.system()} {platform.release()} ({os.name})")
    print(f"------------------------------------------------------------------------------------------------------------------------------------------")
    loop_renew_status.start()

@tasks.loop(seconds=REFRESH_TIME)
async def loop_renew_status():
    servers = {}

    with open("servers.cfg", "r") as f:
        for line in f:
            line = line.rstrip()
            list = line.split(":", 2)
            print("IP/DNS: " + list[0] + " PORT: " + list[1])
            print("")
            
            address = (list[0], int(list[1]))
            try:
                csquery = a2s.info(address)
                servers[list[0]] = {
                    "playercount": csquery.player_count,
                    "maxslots": csquery.max_players,
                    "map": csquery.map_name
                }
            except (socket.gaierror, a2s.BrokenMessageError, a2s.BufferExhaustedError, asyncio.exceptions.TimeoutError, socket.timeout, ConnectionRefusedError, OSError)  as e:
                print("### (WARNING) Exception occured while trying to query " + line + " - Please check for problems")
                continue   

        f.close()

    for server_name, server_info in servers.items():
        status = f"{server_info['playercount']}/{server_info['maxslots']} on {server_info['map']}"
        await SetDiscordStatus(status)
        
        await asyncio.sleep(REFRESH_TIME)

async def SetDiscordStatus(status = ""):
    activity = discord.Game(name=status, type=3)
    try:
        await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    except InvalidArgument:
        print("Exception: Invalid argument")
        pass

def GenerateStatus():
    playercount = 0
    maxslots = 0
    count = 0
    map = ''

    # read file
    with open("servers.cfg", "r") as f:
        for line in f:
            line = line.rstrip()
            list = line.split(":", 2)
            print("IP/DNS: " + list[0] + " PORT: " + list[1])
            
            # query servers
            address = (list[0], int(list[1]))
            try:
                csquery = a2s.info(address)

            except (socket.gaierror, a2s.BrokenMessageError, a2s.BufferExhaustedError, asyncio.exceptions.TimeoutError, socket.timeout, ConnectionRefusedError, OSError)  as e:
                print("### (WARNING) Exception occured while trying to query " + line + " - Please check for problems")
                continue   

            playercount += csquery.player_count
            maxslots += csquery.max_players

            map = csquery.map_name

            count = count + 1

        f.close()


    if count == 0:
        status = "Server(s) Offline"
    elif count == 1:
        status = str(name) + str(playercount) + "/" + str(maxslots) + " on " + map
    elif count > 1:
        status = str(name) + str(playercount) + "/" + str(maxslots) + " on " + str(count) + " servers"

    print(status)
    return (status)

#----------------------------------------Commands-----------------------------------------
# Servers
@bot.command(name='servers', help='Displays the IP addresses and server names of the servers in servers.cfg')
async def servers(ctx):
    with open("servers.cfg", "r") as f:
        servers = []
        for line in f:
            if line.startswith("//"):
                continue
            try:
                ip, port, name = line.split(":")
            except ValueError:
                ip, port = line.split(":")
                name = "Unnamed server"
            servers.append((ip, port, name.rstrip()))
    
    embed = discord.Embed(title=f"{COMMUNITY_NAME}'s Servers", color=0x000000)

    guild = ctx.guild

    embed.set_author(name=guild.name, icon_url=guild.icon_url)
    embed.set_footer(text=f"Use {PREFIX}serverinfo to see the info about a server")
    for i, (ip, port, name) in enumerate(servers):
        address = (ip, int(port))
        try:
            csquery = a2s.info(address)
            player_count = csquery.player_count
            player_max = csquery.max_players
        except (socket.gaierror, a2s.BrokenMessageError, a2s.BufferExhaustedError, asyncio.exceptions.TimeoutError, socket.timeout, ConnectionRefusedError, OSError) as e:
            player_count = "Error querying server"
            player_max = "Error querying server"
        embed.add_field(name=f"`{name}`", value=f"IP/DNS: **{ip}:{port}** (*{player_count}/{player_max}*)", inline=False)
    await ctx.reply(embed=embed, mention_author=False)


# Server Info
@bot.command()
async def serverinfo(ctx, server_ip: str, server_port: int = 27015):
    found = False
    with open("servers.cfg", "r") as f:
        for line in f:
            line = line.rstrip()
            ip, port, *_ = line.split(":")
            if ip == server_ip and port == str(server_port):
                found = True
                break
    if not found:
        embed = discord.Embed(title="Error 👀", description=f"`{server_ip}` cannot be found in `servers.cfg` file.", color=0xff0000)
        embed.set_footer(text="© Moongetsu Systems™ (2020-2022) | Source Servers Bot (v2 beta)")
        await ctx.reply(embed=embed, mention_author=False)
        return
    address = (server_ip, server_port)
    try:
        csquery = a2s.info(address)
    except (socket.gaierror, a2s.BrokenMessageError, a2s.BufferExhaustedError, asyncio.exceptions.TimeoutError, socket.timeout, ConnectionRefusedError, OSError) as e:
        await ctx.reply("Error querying server: {}".format(e))
        return

    guild = ctx.guild
    
    banner_url = f"https://cache.gametracker.com/server_info/{server_ip}:{server_port}/b_560_95_1.png"
    embed = discord.Embed(title=csquery.server_name, description=f"steam://connect/{server_ip}:{port}", color=0x00000)
    embed.set_author(name=guild.name, icon_url=guild.icon_url)
    embed.set_image(url=banner_url)
    embed.add_field(name="IP/DNS 🌍", value="```{}```".format(server_ip))
    embed.add_field(name="Current Map 🗺️", value=f"```{csquery.map_name}```")
    embed.add_field(name="Current players 🛡️", value="```{}/{}```".format(csquery.player_count, csquery.max_players))
    embed.set_footer(text="© Moongetsu Systems™ (2020-2022) | Source Servers Bot (v1.0b)")

    await ctx.reply(embed=embed, mention_author=False)

# Help
@bot.command()
async def help(ctx):
    guild = ctx.guild

    embed = discord.Embed(title=f"Source Servers Bot Commands", color=0x000000)
    embed.set_author(name=guild.name, icon_url=guild.icon_url)
    embed.add_field(name=":page_with_curl: | servers", value="See the servers from our community.", inline=False)
    embed.add_field(name=":chart_with_upwards_trend: | serverinfo `<serverip>`", value="Sends info about a server from the servers list.", inline=False)
    embed.set_footer(text="© Moongetsu Systems™ (2020-2022) | Source Servers Bot (v1.0b)")
    await ctx.reply(embed=embed, mention_author=False)

bot.run(TOKEN)
