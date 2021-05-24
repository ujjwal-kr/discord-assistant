import discord,asyncio,json
from discord.ext import commands
id = 845654928336748554
illegal_words=['Nigger','Nigga','N1gg3r','N1gger','Nigg3r','N1gga','N1gg@','Dick','Fuck','fuck','nigger','nigga','n1gg3r','n1gga','n1gg@','dick']
class Logs(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
   
    @commands.Cog.listener()
    async def on_message(self,message):
        '''This Function is a moderation features and it ban certain words, for more restricted words you can add those in above list'''
        if any(word in message.content for word in illegal_words):
            user=message.author
            await message.delete()#This command deletes the messages if it contains those words
            await user.send('Your message was deleted due to use of illegal words and you get muted role for 10 mins. So Enjoy.')#This line sends a dm to user
            role=discord.utils.get(message.guild.roles,name='muted')#This command gives the user a muted role, you can change the muted role with any role you want to give but the name is case sensitive
            await message.author.add_roles(role)
            await asyncio.sleep(600.0)#this is  a timer of 10 mins, after 10 mins the role gets removed automatically.
            await message.author.remove_roles(role)
        else:
            await self.bot.process_commands(message)
        
    @commands.Cog.listener()
    async def on_message_edit(self,message_before,message_after):
        '''This function sends logs in a specific channel if a message is edited by user.To change the channel just change the channel id in line 3'''
        emb=discord.Embed(title=f'Message Edited in {message_after.channel}',description='',color=discord.Color.red())
        emb.set_author(name=message_after.author,icon_url=message_after.author.avatar_url)
        emb.add_field(name='Old message',value=message_before.content)
        emb.add_field(name='Edited Message',value=message_after.content)
        await self.bot.get_channel(id).send(embed=emb)
    @commands.Cog.listener()
    async def on_message_delete(self,message):
        '''This function sends log when a message gets deleted.'''
        emb=discord.Embed(title='Deleted Message', description=f'Message in {message.channel.mention} sent by {message.author} is deleted.',color=discord.Color.red())
        emb.set_author(name=message.author,icon_url=message.author.avatar_url)
        emb.add_field(name='Message',value=message.content)
        emb.timestamp=message.created_at
        await self.bot.get_channel(id).send(embed=emb)

        

def setup(bot):
    bot.add_cog(Logs(bot))