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


def setup(bot):
    bot.add_cog(Mod(bot))