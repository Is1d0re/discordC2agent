import re
import os
import subprocess
import discord
import time
import asyncio


def run_command(cmd):
    output = subprocess.check_output(cmd)
    output_stripped = str(output.rstrip())
    end = len(output_stripped) - 1
    stdout = output_stripped[2:end]
    print(stdout)
    return(stdout)

if __name__ == "__main__":
    
    TOKEN = '' #Add your discord bot token here

    client = discord.Client()

    @client.event
    async def on_message(message):
    # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content.startswith('!'):
            channel = client.get_channel(CHANNEL ID GOES HERE!)
            new_cmd = message.content[1:]
            cmd = new_cmd[0:].split()
            print(cmd)
            command_output = run_command(cmd)
            msg = command_output
            await message.channel.send(msg)
            print(message.author.id)

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        channel = client.get_channel(CHANNEL ID GOES HERE!)
    client.run(TOKEN)