import discord, json, os
from discord.ext import commands

with open("config.json") as f:
    TOKEN = json.loads(f.read())["token"]

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())
bot.remove_command("help")

for i in os.listdir("Cogs"):
    if i.endswith(".py"):
        bot.load_extension(F"Cogs.{i[:-3]}")

@bot.event
async def on_ready(): print("The Bot is Ready")

# @bot.command()
# async def reload(ctx,cog):
#     if ctx.author.id in [Uncomment and put your id here if you want to use this function :p]:
#         if cog.lower() == "all":
#             for i in os.listdir("Cogs"):
#                 if i.endswith(".py"):
#                     bot.unload_extension(F"Cogs.{i[:-3]}")
#                     bot.load_extension(F"Cogs.{i[:-3]}")
#         await ctx.send("Reloaded all Cogs")
#     else:
#         bot.unload_extension(F"Cogs.{cog}")
#         bot.load_extension(F"Cogs.{cog}")
        

bot.run(TOKEN)