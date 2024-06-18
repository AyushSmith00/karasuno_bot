import nextcord
import random
from nextcord.ext import commands
import requests
import env

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is Online......")

@bot.command()
async def Hi(ctx):
    greetings = [
        "Hello!",
        "Hi there!",
        "Hey!",
        "Good morning!",
        "Howdy!",
        "Yo!",
        "Hi!",
        "What's up?",
        "Nice to see you!",
        "Bonjour!",
        "Hola!",
        "Ciao!",
        "Namaste!",
        "Konnichiwa!",
    ]

    await ctx.send(random.choice(greetings))

@bot.command()
async def neko(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    res  = requests.get(url)
    data = res.json()
    await ctx.send(data[0]["url"])

@bot.command()
async def neko10(ctx):
    url = "https://api.thecatapi.com/v1/images/search?limit=10"
    res  = requests.get(url)
    data = res.json()

    for i in data:
        await ctx.send(i["url"])

@bot.command()
async def code(ctx,*,args):
    code = args
    await ctx.message.delete()
    await ctx.send(f"```python\n{code}\n```")
    await ctx.channel.send(f'Author:<@{ctx.author.id}>')

bot.run(env.TOKEN)
