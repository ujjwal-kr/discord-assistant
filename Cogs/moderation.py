import discord,asyncio,json
from discord.ext import commands

## Configuration by TheEmperor342

class Logs(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        with open("Configuration/ModConfig.json") as f: self.CONFIG = json.loads(f.read())
        self.illegal_words=['Nigger','Nigga','N1gg3r','N1gger','Nigg3r','N1gga','N1gg@','Dick','Fuck','F U C K','f u c k','fuck','nigger','nigga','n1gg3r','n1gga','n1gg@','dick']
        
    ## ==> THIS FUNCTION BANS CERTAIN WORDS. IF YOU WANT TO BAN SOME MORE WORDS, ADD THEM TO THE LIST ABOVE
    #############################################################################################
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if str(message.guild.id) in self.CONFIG.keys():
            if self.CONFIG[str(message.guild.id)]["toggled"] and self.CONFIG[str(message.guild.id)]["channel"] != None:
                if any(word in message.content for word in self.illegal_words):
                    user=message.author
                    await message.delete() #This command deletes the messages if it contains those words
                    await user.send('Your message was deleted due to use of illegal words and you get muted role for 10 mins. So Enjoy')#This line sends a dm to user
                    role=discord.utils.get(message.guild.roles,name='muted') #This command gives the user a muted role, you can change the muted role with any role you want to give but the name is case sensitive
                    await message.author.add_roles(role)
                    await asyncio.sleep(600.0) #this is  a timer of 10 mins, after 10 mins the role gets removed automatically.
                    await message.author.remove_roles(role)
    
    #############################################################################################
        
    ## ==>  THIS FUNCTION SENDS LOGS IN A SPECIFIC CHANNEL IF A MESSAGE IS EDITED
    #############################################################################################
    
    @commands.Cog.listener()
    async def on_message_edit(self,message_before,message_after):
        if str(message_before.guild.id) in self.CONFIG.keys():
            if self.CONFIG[str(message_before.guild.id)]["toggled"] and self.CONFIG[str(message_before.guild.id)]["channel"] != None:        
                emb=discord.Embed(title=f'Message Edited in {message_after.channel}',description='',color=discord.Color.red())
                emb.set_author(name=message_after.author,icon_url=message_after.author.avatar_url)
                emb.add_field(name='Old message',value=message_before.content)
                emb.add_field(name='Edited Message',value=message_after.content)
                try: await self.bot.get_channel(self.CONFIG[str(message_before.guild.id)]["channel"]).send(embed=emb)
                except KeyError: pass
    
    #############################################################################################
        
    ## ==> THIS FUNCTION SENDS LOG WHEN A MESSAGE GETS DELETED
    #############################################################################################
    
    @commands.Cog.listener()
    async def on_message_delete(self,message):
        if str(message.guild.id) in self.CONFIG.keys():
            if self.CONFIG[str(message.guild.id)]["toggled"] and self.CONFIG[str(message.guild.id)]["channel"] != None:
                emb=discord.Embed(title='Deleted Message', description=f'Message in {message.channel.mention} sent by {message.author} is deleted.',color=discord.Color.red())
                emb.set_author(name=message.author,icon_url=message.author.avatar_url)
                emb.add_field(name='Message',value=message.content)
                emb.timestamp=message.created_at
                try: await self.bot.get_channel(self.CONFIG[str(message.guild.id)]["channel"]).send(embed=emb)
                except KeyError: pass
        
    #############################################################################################
    
    ## ==> CONFIGURATION
    #############################################################################################
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def toggleLog(self,ctx: commands.Context):
        if str(ctx.guild.id) in self.CONFIG.keys():
            self.CONFIG[str(ctx.guild.id)]["toggled"] = True if not self.CONFIG[str(ctx.guild.id)]["toggled"] else False
        else:
            self.CONFIG[str(ctx.guild.id)] = {"channel": None, "toggled": True}
            
        with open("Configuration/ModConfig.json",'w') as f: f.write(json.dumps(self.CONFIG))
        await ctx.send(embed=discord.Embed(color=ctx.author.color, title="MODERATION", description="Logs Have Been Toggled"))
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setLogChannel(self,ctx: commands.Context, channel: discord.TextChannel):
        if channel in ctx.guild.channels:
            if str(ctx.guild.id) not in self.CONFIG.keys(): self.CONFIG[str(ctx.guild.id)] = {"channel": channel.id, "toggled":False}
            else: self.CONFIG[str(ctx.guild.id)]["channel"] = channel.id
            
            with open("Configuration/ModConfig.json",'w') as f: f.write(json.dumps(self.CONFIG))
            embed = discord.Embed(title="MODERATION",description=f"Logs set to <#{channel.id}> !", color=ctx.author.color)
            await ctx.send(embed=embed)
        else: return
        
    #############################################################################################

def setup(bot):
    bot.add_cog(Logs(bot))