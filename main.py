import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("The bot is now ready for use")

@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")
    await bot.process_commands(message)

@bot.command(name='hello', aliases=['hi', 'hey', 'Hello', 'alo'])
async def greeting(ctx):
    await ctx.send("Hi, I'm a bot!")

@bot.command(name='test', aliases=['t'])
async def test(ctx):
    await ctx.send("ha")
    

bot.run('MTE2NDEyMDgyNjM4ODQxODU2MQ.GptAvR.vfQcCzayEDHmqu-eJPqBNNKZle_cNDFx1FUKMY')
