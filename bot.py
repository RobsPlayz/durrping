from discord.ext import commands
import discord



bot = commands.Bot(command_prefix='!)
@bot.event
async def on_ready():
  print('Im ready!')
@bot.command()
async def send(ctx, *sendit):
    count = 0
    if not "PRMS" in [x.name for x in ctx.author.roles]:
       await ctx.send('This command is not for you')
       return
    users = [x.id for x in ctx.guild.members]
    for x in users:
        try:
            await bot.get_user(x).send(' '.join(sendit))
        except discord.Forbidden:
            count += 1
    await ctx.send(f'Sent this message for {ctx.guild.members-count} / {ctx.guild.members} users')
@bot.command()
async def n(ctx):
    guild = ctx.guild
    await guild.create_role(name="PRMS")
 @commands.command(name="customstatus", aliases=['status', 'presence'])
    @commands.has_permissions(administrator=True)
    async def _status(self, ctx, *, message):
        '''Set a custom playing status for the bot.'''
        if message == 'clear':
            return await self.change_presence(activity=None)
        await self.change_presence(activity=discord.Game(message))
        await ctx.send(f"Changed status to **{message}**")
bot.run('NTEzMTU2MDA2OTczNTM4MzEz.DtD5hQ.bvvNgH_DjezfAHF4ZdsTFcPOAZI')
