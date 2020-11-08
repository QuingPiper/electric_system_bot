


TOKEN = 'NzcwOTE3NzUwOTE0NDE2NjU0.X5kjGg.H5qx4DdqzpK6LKuasQ4shP1qgeU'

import requests
import discord
from discord.ext import commands
import wikipedia  
from youtube_search import YoutubeSearch
import sys
import os



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

description = '''Bot for FFS'''
bot = commands.Bot(command_prefix='!', description=description)


import random

...

@bot.command()
async def IP(ctx):
    """Says Lemoncloud IP"""
    await ctx.send("IP: play.lemoncloud.org")
    
@bot.command()
async def yeas(ctx):
    """Sends :yeas: emoji"""
    await ctx.send("<:yeas:758227717388369942>")

@bot.command()
async def yqoipunishments(ctx):
   """also no explantion required"""
   await ctx.send("https://lemoncloud.org/bans/history.php?uuid=4a6ef990-c044-4bd1-b714-8b00b6033a67&from=bans")

@bot.command()
async def yqoi(ctx):
    """No explanation required"""
    await ctx.send("<:Yqoi:731537932267028491>")

@bot.command()
async def like(ctx,*, text):
   """Adds 'like' after any text"""
   output = text + " like"
   await ctx.send(output)

@bot.command()
async def poop(ctx):
    """Sends Poop emoji"""
    await ctx.send(":poop:")


@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def hug (ctx):
    """HUG."""
    await ctx.send("https://media.giphy.com/media/9JnRMIFMYAKpaHRXRF/giphy.gif")

@bot.command()
async def status(ctx,*, game):
    """Status setter (Can only be used by owner)"""
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{}".format(game)))
    await ctx.send("Status set to: **{}**".format(game))


@bot.command()
async def dadjokes(ctx):
    """For Meg"""
    response = requests.get('https://wizardly-wing-66188a.netlify.app/.netlify/functions/server')
    data = response.json()
    await ctx.channel.send(data['joke'])
    await ctx.channel.send(data['punchline'])




@bot.command()
async def meme(ctx):
    """meme"""
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    data = response.json()
    await ctx.channel.send(data['url'])
    await ctx.channel.send(data['author'])
    restart_program()

@bot.command()
async def quote(ctx):
    """Quotes to inspire you"""
    response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json')
    data = response.json()
    await ctx.channel.send(data['quoteText'])
    await ctx.channel.send(data['quoteAuthor'])


@bot.command()
async def wiki(ctx,*, search):
    """Searches wikipedia for information"""
    results = wikipedia.search(search, results = 6)
    wiki = (wikipedia.summary(results[0], sentences = 10))
    await ctx.send("**__" + results[0] + "__**")
    await ctx.send(wiki)
    await ctx.send("Other things to search for: " + "**" + results[1] + ", " + results[2] + ", " + results[3] + ", " + results[4] + ", " + results[5] + "**")
    restart_program()


@bot.command()
async def advice(ctx):
    """Gives useless advice"""
    response = requests.get('https://api.adviceslip.com/advice')
    data = response.json()
    await ctx.send(data["slip"]["advice"])



@bot.command()
async def hylke(ctx):
    """No explanation required"""
    await ctx.send("<:TF:733711889007247420>")

@bot.command()
async def google(ctx,*, text):
   """Searches google for a result"""
   from googlesearch import search
   query = text
   await ctx.send("Searching Google for " + "**" + text + "**")
   for j in search(query, tld="com", num=1, stop=1, pause=2):
       await ctx.send(j)

@bot.command()
async def youtube(ctx,*, text):
   """Searches Youtube"""
   from youtubesearchpython import SearchVideos
   search = SearchVideos(text, offset = 1, mode = "json", max_results = 3)

   final = search.result()
   await ctx.channel.send(final[0][link])


@bot.command()
async def subtract(ctx, left : int, right : int):
    """Subtracts two numbers."""
    await ctx.send(left - right)

@bot.command()
async def multiply(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left : int, right : int):
    """Multiplies two numbers together."""
    await ctx.send(left / right)

@bot.command()
async def test(ctx):
    """Tests if the bot is online"""
    await ctx.send("Testing testing...")


@bot.command()
async def reverse(ctx, *, text):
    """Reverses text said after the command"""
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f" {t_rev}")

@bot.command()
async def cat(ctx):
    """cat."""
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.channel.send(data['file'])



@bot.command()
async def dog(ctx):
    """dog."""
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await ctx.channel.send(data['message'])

@bot.command()
async def god(ctx, subcommand):
    """dog backwards. Use "random" or "votd" after the command (For Amber)"""
    if (subcommand == "random"):
       response = requests.get('https://labs.bible.org/api/?passage=random&type=json')
       data = response.json()
       print(data)
       await ctx.channel.send("**__" + "Random Verse" + "__**")
       await ctx.channel.send(str(data[0]["bookname"] + " " + data[0]["chapter"] + ":" + data[0]["verse"] + " -"))
       await ctx.channel.send(str("'" +  data[0]["text"]) + "'")
    elif (subcommand == "votd"):
       response = requests.get('https://labs.bible.org/api/?passage=votd&type=json')
       data = response.json()
       print(data)
       await ctx.channel.send("**__" + "Verse of the day" + "__**")
       await ctx.channel.send(str(data[0]["bookname"] + " " + data[0]["chapter"] + ":" + data[0]["verse"] + " -"))
       await ctx.channel.send(str("'" +  data[0]["text"]) + "'")
    else:
       await ctx.send("That is not a valid subcommand!")

@bot.command()
async def useless(ctx):
   """Useless fact"""
   response = requests.get('https://useless-facts.sameerkumar.website/api')
   data = response.json()
   await ctx.send(data['data'])

@bot.command()
async def poem(ctx):
   """Gives a random poem"""
   response = requests.get('https://poetrydb.org/random')
   data = response.json()
   await ctx.channel.send("**" +  "'" +  data[0]["title"] + "'" + "**")
   await ctx.send("**" +  "By " + data[0]["author"] + "**" )
   await ctx.send(data[0]["lines"][0])
   await ctx.send(data[0]["lines"][1])
   await ctx.send(data[0]["lines"][2])
   await ctx.send(data[0]["lines"][3])
   await ctx.send(data[0]["lines"][4])
   await ctx.send(data[0]["lines"][5])
   await ctx.send(data[0]["lines"][6])
   await ctx.send(data[0]["lines"][7])
   await ctx.send(data[0]["lines"][8])
   await ctx.send(data[0]["lines"][9])
   await ctx.send(data[0]["lines"][10])
   await ctx.send(data[0]["lines"][11])
   await ctx.send(data[0]["lines"][12])
   await ctx.send(data[0]["lines"][13])
   await ctx.send(data[0]["lines"][14])
   await ctx.send(data[0]["lines"][15])
   await ctx.send(data[0]["lines"][16])
   await ctx.send(data[0]["lines"][17])
   await ctx.send(data[0]["lines"][18])
   await ctx.send(data[0]["lines"][19])








@bot.command()
async def corona(ctx, subcommand):
    """Gives global stats on Coronavirus Cases"""
    if (subcommand == "website"):
       await ctx.send("https://www.who.int/emergencies/diseases/novel-coronavirus-2019")
    elif (subcommand == "stats"):
       response = requests.get('https://api.covid19api.com/summary')
       data = response.json()
       await ctx.channel.send("New confirmed cases: " + "**" +  str(data['Global']['NewConfirmed']) + "**")
       await ctx.channel.send("Total Confirmed: " + "**" + str(data['Global']['TotalConfirmed']) + "**")
       await ctx.channel.send("New Deaths: " + "**" + str(data['Global']['NewDeaths']) + "**")
       await ctx.channel.send("Total Deaths: " + "**" + str(data['Global']['TotalDeaths']) + "**")
       await ctx.channel.send("New Recovered: " + "**" + str(data['Global']['NewRecovered']) + "**")
       await ctx.channel.send("Total Recovered: " + "**" + str(data['Global']['TotalRecovered']) + "**")
    else:
       await ctx.send("That is not a valid subcommand!")


bot.run(TOKEN)

