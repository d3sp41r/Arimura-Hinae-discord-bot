import discord

bot = discord.Client(intents=discord.Intents.default())

intents = discord.Intents.all()
intents.messages = True

client = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("Arimura Hinae is in " + str(guild_count) + " clubs!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "sono me":
        await message.channel.send("dare no meeee????")
    if message.content == "VIBRATE!":
        await message.channel.send("https://tenor.com/view/arimura-hinae-vibrating-gif-24618638")
    if message.content == "https://tenor.com/view/arimura-hinae-vibrating-gif-24618638":
        await message.channel.send("https://tenor.com/view/arimura-hinae-vibrating-gif-24618638")



bot.run("the token")
