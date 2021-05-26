import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Cog, cog
from discord.ext.commands import MemberConverter

class Mod(Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,user:MemberConverter,*,reason=None):
        '''This commands kick a user. This command takes 2 arguments in input,out of these two only one argument user is important'''
        if user==None:
            await ctx.send('Please specify a user')
            return
        if reason==None:
            await user.kick(reason='Unspecified')
        else:
            await user.kick(reason=reason)
        await ctx.send(f'{user} has been kicked from your server')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,user:MemberConverter,*,reason=None):
        '''This command ban a user. This command takes 2 argument out of which only one is important'''
        if user==None:
            await ctx.send('Please specify a user')
            return
        if reason==None:
            await user.ban(reason='Unspecified')
        else:
            await user.ban(reason=reason)
        await ctx.send(f'{user} has been banned from your server.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        """This command unban a banned member.You must supply the user parameter like this 'PHÄÑTÖM KÑÏGHT
#9152'"""
        banned_users=await ctx.guild.bans()#This command will fetch all the banned users from guild/server
        member_name,member_disc=member.split('#')#This command will split the member name and its discriminator
        for banned_entry in banned_users:
            user=banned_entry.user
            if (user.name,user.discriminator)==(member_name,member_disc):#This line checks if the given user is in banned users list if yes the next line unban them.
                await ctx.guild.unban(user)
                await ctx.send(member_name+'has been unbanned')
                return
        await ctx.send(member+'was not found')#and if the given user is not in banned users list it just send this message.




def setup(bot):
    bot.add_cog(Mod(bot))