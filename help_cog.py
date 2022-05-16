import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
```
commands:
/help - displays this
/p <words> - plays song
/q - displays queue
/skip - skips song (currently broken probs wont be fixed lmao)
/clear - clears queue
/leave - makes bot leave
/pause - pauses music
/resume - resumes music
```
        """

    @commands.command(name="help", help="displays commands (unless adrian doesnt update the list")
    async def help(self, ctx):
        await ctx.send(self.help_message)