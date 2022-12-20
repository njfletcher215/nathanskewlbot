import discord

from discord.ext import commands
from config import TOKEN, COMMAND_PREFIXES, STRIP_AFTER_PREFIX
from music_player import Music

bot = commands.Bot(command_prefix=COMMAND_PREFIXES, strip_after_prefix=STRIP_AFTER_PREFIX,
                   intents=discord.Intents.all())


@bot.command()
async def hello(ctx: commands.Context):
    await ctx.reply('Hello, {0}'.format(ctx.author))

bot.add_cog(Music(bot))
bot.run(TOKEN)
