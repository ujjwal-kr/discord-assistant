import discord
from discord.ext import commands

class Miscellaneous(commands.Cog):
    def __init__(self,bot: commands.Bot) -> None: 
        self.bot = bot
        
    ## ==> ERROR HANDLING
    #############################################################################################
    
    # @commands.Cog.listener()
    # async def on_command_error(self,ctx,error): await error.channel.send(embed=discord.Embed(title="Whoops",color=discord.Color.red(),description=f"An error occured while trying to run that command\n{error}"))
    
    #############################################################################################
    
    ## ==> HELP COMMAND
    #############################################################################################
    
    @commands.command()
    async def help(self, ctx: commands.Context) -> None:
        embed = discord.Embed(title="HELP",color=ctx.author.color)
        embed.set_footer(text="Developed By [ᴛʜᴇ ᴇᴍᴘᴇʀᴏʀ]")
        
        embed.add_field(
            name=":partying_face: **WELCOMER**",
            value="""
**[ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴏʀ ᴏɴʟʏ]**

:white_check_mark: `>toggle`:
    To Toggle Welcomer On or Off

:scroll: `>SetWelcomeMessage <message>`:
    To Set the Welcome Message
    Using `|user|` in message will replace it with a mention of the new user    -> Important
    Using `|guild|` in message will replace it with the name of the server
    
:dart: `>SetChannel <Channel>`:
    To Set the channel to send Welcome message in
    Mention channel as #<channel name>
"""
        )
        await ctx.send(embed=embed)
    
    #############################################################################################

## ==> ADDING THE COG TO BOT
#############################################################################################

def setup(bot:commands.Bot) -> None: bot.add_cog(Miscellaneous(bot))

#############################################################################################