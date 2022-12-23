# source-servers-monitor-discord
source-servers-monitor-discord

# What does this do?
This is a discord bot that counts number of connected players/map played on your source servers, with some useful commands.

# How does this look like on discord

![This is an image](https://i.imgur.com/qbFtS11.png)

# Ways of working

1) For every individual source server you have.
2) For multiple servers, with changing status.
3) All servers statistics in the status. (soon)

# How to configure the bot

## Configuration of settings.json
Grab your bot token from discord developers (https://discord.com/developers/applications) and put it in the token line.
Put the prefix that you want at the bot in the prefix line.
Put the community name in the community-name line.

## Configuration of servers.cfg
Here you can put your server's DNS/IP and the server name or all your server's if you want the bot to count a total of players.

## Installation of dependencies (Root VPS)

```
git clone https://github.com/moongetsu/source-servers-bot-discord
cd source-servers-monitor-discord
apt install screen
apt install python3 python3-pip
pip3 install python-a2s discord.py
pip3 install colorama
screen python3 main.py
```

## Installation of dependencies (Pterodactyl Panel)

```
Add in the start-up: 
python-a2s discord.py==1.7.3 asyncio colorama
```
# License

```
#   MIT License
#   
#   Copyright (c) 2022 - Stan '(xSLOW)' Valentin-Alexandru 
#   Copyright (c) 2022 - Stan '(moongetsu)' Mario-Daniel

#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
```
