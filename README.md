# Discord C2 Agent
This script can be run on a remote PC to achieve RCE via a private discord channel

I used [this guide](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) to help create the bot and then integrate it to python.

This project is still under development.

## Configuration 
1. Create a discord bot as outlined in the guide linked above.
2. Change the following lines:

You can get the token from the bot settings. The guide shows you where it is.
```python
TOKEN = '' #Add your discord bot token here
```

There are two instances of the following line that need to be updated with the ID for the channel you want to C2 the bot from. You can [turn on developer mode](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/) in discord and then just right click on the channel to "Copy ID".
```python
channel = client.get_channel(CHANNEL ID GOES HERE!)
```