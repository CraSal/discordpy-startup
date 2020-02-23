from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def sensi(ctx):
    await ctx.send('他ゲームとのマウスの感度を揃えたいならココ！(※一部課金必※)\nhttps://www.mouse-sensitivity.com/')
    
@bot.command()
async def aiming(ctx):
    await ctx.send('ブラウザで出来るaim練習！(※一部課金必※)\nhttps://aiming.pro/dashboard')

bot.run(token)
