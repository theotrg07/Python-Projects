import discord
from discord.ext import commands

client = discord.Bot(commands_prefix='..')

@client.command(name='kick', pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):

    await member.kick()
    await context.send('User ' + member.display_name + ' has been kicked')



@clietn.command(name='ban', pass_context=True)
@commands.has_permissions(kick_members=True)
async def ban (context, member: discord.Member, *, reason=None)

await member.ban(reason=reason)
await context.send('User ' + member.display_name + 'has been banned')    


client.run('Nzg3NDUyNTA3NTYzNDkxNDAw.X9VKSw.IQqrJubdn9QprkC3qnU-yTfJJZM')
   