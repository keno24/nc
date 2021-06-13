from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
import discord
import asyncio
import ctx
import random
import json

client = commands.Bot(command_prefix="nc!")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Official Night Community Bot'))
    print("Night Community")

@client.command(aliases=['pitanja'])
@commands.has_permissions(administrator=True)
async def staff(ctx):
    em = discord.Embed(title="Pitanja za Staff:")
    em.add_field(name="1. Koliko imate godina ?", value="** **", inline=False)
    em.add_field(name="2. Imate li mikrofon ?", value="** **", inline=False)
    em.add_field(name="3. Da li ste bili staff i na kojem serveru (koliko clanova,ime,pozicija:admin mod) ?", value="** **", inline=False)
    em.add_field(name="4. Znate li raditi sa botovima ?", value="** **", inline=False)
    em.add_field(name="5. Koliko ste dugo na serveru ?", value="** **", inline=False)
    em.add_field(name="6. Koji ste level na mee6 botu ?", value="** **", inline=False)
    em.add_field(name="7. Zašto baš vas da izaberemo ?", value="** **", inline=False)
    em.add_field(name="8. Da li si procitao/la pravila servera ?", value="** **", inline=False)
    await ctx.send(embed=em)

@staff.error
async def staff_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Ova komanda je namjenjena za Staff Team!")

client.run()