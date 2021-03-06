import discord, config, asyncio, os

from flask import Flask

from threading import Thread

app = Flask('')

@app.route('/')

def main():
    
    return "Thanks for support my channel - Zac"

def run():
    
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    
    server = Thread(target=run)
    
    server.start()
    
bot = discord.Client()

async def status():
  
  while True:
    
    StatusContent1 = config.StatusContent1

    StatusContent2 = config.StatusContent2
    
    if StatusContent1 == None:

      StatusContent1 = os.getenv("StatusContent1")

    if StatusContent2 == None:

      StatusContent2 = os.getenv("StatusContent2")

    await bot.change_presence(
        
        status=discord.Status.dnd,
#You can also use `online`, `invisible` and `idle` here.        
        activity=discord.Activity(
            
            type=discord.ActivityType.watching,
#You can also use `listening` here.          
            name=StatusContent1))
        
    await asyncio.sleep(10)
        
    await bot.change_presence(
        
        status=discord.Status.dnd,
#You can also use `online`, `invisible` and `idle` here.      
        activity=discord.Activity(
            
            type=discord.ActivityType.watching,
#You can also use `listening` here.            
            name=StatusContent2))
    
    await asyncio.sleep(10)

    #`Playing` status
    #await bot.change_presence(activity=discord.Game(name="a game"))

    #`Streaming` status
    #await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))


@bot.event

async def on_ready():
    
    bot.loop.create_task(status())

    print(f"Website: {config.Website}")

    print("Ready!")

if config.Website == 'true':

  keep_alive()

bot.run(config.Token)
