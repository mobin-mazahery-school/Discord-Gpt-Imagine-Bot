import discord, os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intent = discord.Intents.default()
intent.message_content = True
bot = commands.Bot(command_prefix=os.environ.get("PEREFIX"), help_command=None, intents=intent)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def imagine(ctx, *args):
    message = ' '.join(args)
    embed = discord.Embed()
    embed.description = "<html><body><h1>"+message+"</h1></body></html>"
    await ctx.send(embed=embed)

bot.run(os.environ.get("TOKEN"))