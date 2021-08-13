import discord
from discord.ext import commands
import random

#Client
client = commands.Bot(command_prefix='--')


@client.command(name='version')
async def version(context):
    
    myEmbed = discord.Embed(title='Current Version', description='The bot is in version  1.0', color=0x00ff00)
    myEmbed.add_field(name='Version Code', value='v1.0.0', inline=False) 
    myEmbed.add_field(name='Date Released', value='December 9th, 2020', inline=False)
    myEmbed.set_footer(text='This is a sample footer')
    myEmbed.set_author(name='theo trg')

    await context.message.channel.send(embed=myEmbed)



@client.event
async def on_ready():
    general_channel = client.get_channel(786211277172768781)
    await general_channel.send("The bot is ready!")



@client.command(name="randimg")
async def randimg(context):

    images = ["paokfc.jpg", "rubiks cube.jpeg", "giphy.gif"]
    
    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))



@client.command(name='kick', pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):

    await member.kick()
    await context.send('User ' + member.display_name + ' has been kicked')


@client.command(name='ban', pass_context=True)
@commands.has_permissions(kick_members=True)
async def ban(context, member: discord.Member, *, reason=None ):
    
    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned')


@client.event
async def on_disconnect():
    general_channel = client.get_channel(786211277172768781)
    await general_channel.send('Goodbyeee!')


@client.event
async def on_message(message):
    
    if message.content == 'what is the version':
        general_channel = client.get_channel(786211277172768781)

        myEmbed = discord.Embed(title='Current Version', description='The bot is in version  1.0', color=0x00ff00)
        myEmbed.add_field(name='Version Code', value='v1.0.0', inline=False) 
        myEmbed.add_field(name='Date Released', value='December 9th, 2020', inline=False)
        myEmbed.set_footer(text='This is a sample footer')
        myEmbed.set_author(name='theo trg')

        await general_channel.send(embed=myEmbed)

    if message.content == 'Send a DM':
        await message.author.send('This is a DM, have a good day!')
 
    await client.process_commands(message)

    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Visual Studio Code'))


    
    
    
#Run the client on the server
client.run('Nzg2MjExMTEyMTE4MTI0NTQ3.X9DGKA.ZPzIiw07-RUwy9JRtfAq5m6M0zI')