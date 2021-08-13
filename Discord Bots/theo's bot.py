import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')



@client.command
async def on_ready():
    general_channel = client.get_channel(786211277172768781)
    await general_channel.send(' The bot is ready!')






@client.command(name='info_server')
async def info_server(context):

    my2Embed = discord.Embed(title='Server', description='Server Info', color=0x00ff00)
    my2Embed.add_field(name='Members', value='3', inline=False)
    my2Embed.add_field(name='Was Created', value='December 9th, 2020', inline=False)
    my2Embed.set_footer(text='This is info about the server')
    my2Embed.set_author(name='theo trg')
    await context.message.channel.send(embed=my2Embed)


client.run('NzE3MDI3Nzk0MjE5MTcxODQw.XtUWKw.937edX2nkUv0xYNrKdOtm2iHHfY')


