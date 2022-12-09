import interactions

bot = interactions.Client(token="the token")

@bot.command(
    name="vibrate",
    description="initiates the VIBRATION!!",
    scope=729431325991239681,
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("https://tenor.com/view/arimura-hinae-vibrating-gif-24618638")

bot.start()
