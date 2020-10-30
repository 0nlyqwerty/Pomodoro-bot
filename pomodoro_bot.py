import discord
from discord.ext import commands
import os
import platform
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime

# Get token from ./token.txt
CURRENT_DIR_PATH = os.path.dirname(__file__)
if CURRENT_DIR_PATH == "":
    CURRENT_DIR_PATH = "."
if platform.system() == "Linux":
    CURRENT_DIR_PATH = CURRENT_DIR_PATH + "/"
elif platform.system() == "Windows":
    CURRENT_DIR_PATH = CURRENT_DIR_PATH + "\\"
t = open(CURRENT_DIR_PATH + "token.txt", "r", encoding="utf-8")
TOKEN = t.read().split()[0]

version = '1.0.0'
intents = discord.Intents.default()
intents.members = True
intents.presences = True
game = discord.Game(f"Pomodoro Bot {version}")
bot = commands.Bot(command_prefix='!', status=discord.Status.online,
                   activity=game, help_command=None, intents=intents)

sched = AsyncIOScheduler()


@bot.event
async def on_ready():
    print(" ---------------------")
    print(" POMODORO BOT on_ready")
    print(" ---------------------")
    sched.start()


@bot.command(name='pmdr_help')
async def send_help_message(ctx):
    """ Pomodoro bot help command
    Action:
        Send Pomodoro command help message
    """

    await ctx.channel.send(
        f"```css\n[Pomodoro Timer]\n - Start command : !pmdr_start [work_min] [break_min]\n     ex) !pmdr_start 25 "
        f"5\n -  Stop command : !pmdr_stop```")


@bot.command(name='pmdr_start')
async def start_pomodoro_timer(ctx, work_time: int, break_time: int):
    """ Start pomodoro timer
    Action:
        Start break_time timer after work_time timer
    Args:
        work_time : work timer (minute)
        break_time : break timer after work_time (minute)
    """

    if len(sched.get_jobs()) > 0:
        await ctx.channel.send(
            f"```css\n[⚠️Pomodoro timer already working!]\n - stop command : !pmdr_stop```")
        return

    async def break_schedule(work_time, break_time):
        print('Enter break schedule')
        await ctx.channel.send(
            f"{ctx.author.mention}```css\n[🔥Break time end!] Let's work :)```")
        work_expire_time = get_expire_time(work_time)
        sched.add_job(work_schedule, 'date', run_date=work_expire_time, args=[
                      work_time, break_time], misfire_grace_time=300)
        pass

    async def work_schedule(work_time, break_time):
        print('Enter work schedule')
        await ctx.channel.send(
            f"{ctx.author.mention}```css\n[🏁Work time end!] Let's break :)```")
        break_expire_time = get_expire_time(break_time)
        sched.add_job(break_schedule, 'date', run_date=break_expire_time,
                      args=[work_time, break_time], misfire_grace_time=300)
        pass

    work_expire_time = get_expire_time(work_time)
    sched.add_job(work_schedule, 'date', run_date=work_expire_time,
                  args=[work_time, break_time], misfire_grace_time=300)

    await ctx.channel.send(
        f"```css\n[Work {work_time}min, Break {break_time}min] Pomodoro Timer START.\n - stop command : !pmdr_stop```")


@bot.command(name='pmdr_stop')
async def stop_pomodoro_timer(ctx):
    """ Stop pomodoro timer
    Action:
        Stop pomodoro timer
    """
    sched.remove_all_jobs()
    await ctx.channel.send(
        f"```css\nPomodoro Timer STOP.\n - start command : !pmdr_start [work_min] [break_min]```")


def get_expire_time(minutes: int):
    now = datetime.datetime.now()
    expire_time = now + datetime.timedelta(minutes=minutes)
    return expire_time


bot.run(TOKEN)
