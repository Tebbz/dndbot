#!/usr/bin/env python
# coding: utf-8

# In[10]:


# D&D Bot.
# A bot for your discord that can do D&D related things. Have fun!

import os
import random

from discord.ext import commands

import discord
from dotenv import load_dotenv

# 1
# Get information from our .env to run D&D Bot.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
# Initiate D&D Bot.
bot = commands.Bot(command_prefix = '.')

# We need an 'Initiative List' to be available in between commands.
bot.init_list = dict()

# Show that D&D Bot has connected successfully.
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# r
#
# Simulates a die roll, or several.
# Can add modifiers to the die roll, as well.
@bot.command(name = 'r', help = 'Simulate a die roll, or multiple.\n\n.r <die> <x> <mod>\nYou must pick a kind of die: d4, d6, d8, d10, d12, d20, or d100.\nYou can choose to roll it multiple times with <x>.\nYou can choose to add modifiers to it with <mod>.')
async def r(ctx, *param):
    
    # r (die)
    # Roll the (die).
    # 
    # Assess the proper die to use.
    # Roll it.
    # Send the result as a message.
    if len(param) == 1:
        if param[0].lower() == "d4":
            await ctx.send(random.randint(1, 4))
            
        elif param[0].lower() == "d6":
            await ctx.send(random.randint(1, 6))
            
        elif param[0].lower() == "d8":
            await ctx.send(random.randint(1, 8))
            
        elif param[0].lower() == "d10":
            await ctx.send(random.randint(1, 10))
            
        elif param[0].lower() == "d12":
            await ctx.send(random.randint(1, 12))
            
        elif param[0].lower() == "d20":
            await ctx.send(random.randint(1, 20))
            
        elif param[0].lower() == "d100":
            await ctx.send(random.randint(1, 100))
            
        else:
            await ctx.send('Error: ' + param[0] + ' isn\'t a real kind of die!')

    # r (die) (x)
    # Roll the (die) (x) amount of times.
    #
    # Get the value for (x) as an int.
    # Create a list to hold the results of the dice.
    # Assess the proper die to use.
    # Roll it (x) times.
    # Send the list as a message, formatted.
    elif len(param) == 2:
        rollList = []
        
        try:
            x = int(param[1])
        except ValueError:
            await ctx.send('Error: we can\'t roll it ' + param[1] + ' amount of times!')
            return
    
        if param[0].lower() == "d4":
            for i in range(x):
                rollList.append(random.randint(1, 4))
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d6":
            for i in range(x):
                rollList.append(random.randint(1, 6))
            
            await ctx.send(rollList)
        
        elif param[0].lower() == "d8":
            for i in range(x):
                rollList.append(random.randint(1, 8))
            
            await ctx.send(rollList)
            
        elif param[0].lower() == "d10":
            for i in range(x):
                rollList.append(random.randint(1, 10))
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d12":
            for i in range(x):
                rollList.append(random.randint(1, 12))
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d20":
            for i in range(x):
                rollList.append(random.randint(1, 20))
            
            await ctx.send(rollList)
            
        elif param[0].lower() == "d100":
            for i in range(x):
                rollList.append(random.randint(1, 100))
                
            await ctx.send(rollList)
            
        else:
            await ctx.send('Error: ' + param[0] + ' isn\'t a real kind of die!')
    
    # r (die) (x) (mod)
    # Roll the (die) (x) amount of times with (mod) added to it.
    #
    # Get the value for (x) as an int.
    # Get the value for (mod) as an int.
    # Create a list to hold the results of the dice.
    # Assess the proper die to use.
    # Roll it (x) times adding (mod) to it.
    # Send the list as a message, formatted.
    elif len(param) == 3:
        rollList = []
        
        try:
            x = int(param[1])
        except ValueError:
            await ctx.send('Error: we can\'t roll it ' + param[1] + ' amount of times!')
            return
            
        try:
            mod = int(param[2])
        except ValueError:
            await ctx.send('Error: we can\'t add ' + param[2] + ' number to the rolls!')
            return
            
        if param[0].lower() == "d4":
            for i in range(x):
                rollList.append(random.randint(1, 4) + mod)
                
            await ctx.send(rollList)
        
        elif param[0].lower() == "d6":
            for i in range(x):
                rollList.append(random.randint(1, 6) + mod)
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d8":
            for i in range(x):
                rollList.append(random.randint(1, 8) + mod)
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d10":
            for i in range(x):
                rollList.append(random.randint(1, 10) + mod)
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d12":
            for i in range(x):
                rollList.append(random.randint(1, 12) + mod)
                
            await ctx.send(rollList)
        
        elif param[0].lower() == "d20":
            for i in range(x):
                rollList.append(random.randint(1, 20) + mod)
                
            await ctx.send(rollList)
            
        elif param[0].lower() == "d100":
            for i in range(x):
                rollList.append(random.randint(1, 100) + mod)
                
            await ctx.send(rollList)
            
        else:
            await ctx.send('Error: ' + param[0] + ' isn\'t a real kind of die!')
        
    else:
        await ctx.send("Error: invalid number of parameters.")

# r
#
# A new roll function

@bot.command(name = 'roll', help = 'Roll some damn dice.')
async def roll(ctx, *param):
    
    message = ""
    x = 1
    m = 0
    
    # We LOOPING.
    for d in param:
        
        message = str(d) + ": "
        
        # Find a '+' for <m>.
        # If we don't, it is fine.
        if d.find('+') != -1:
            try:
                await ctx.send(d[:d.find('+')])
                
                m = int(d[d.find('+'):])
            
                d = d[:d.find('+') - 1]
            
            except ValueError:
                await ctx.send('Error: we can\'t set <m> to ' + d[d.find('+'):] + '.')
                return
    
        # Find a '-' for <m>.
        # If we don't, it is fine.
        if d.find('-') != -1:
            try:
                await ctx.send(d[:d.find('+') - 1])
                
                m = int(d[d.find('-'):])
            
                d = d[:d.find('-') - 1]
            
            except ValueError:
                await ctx.send('Error: we can\'t set <m> to ' + d[d.find('-'):] + '.')
                return
        
        await ctx.send(d)
        
        # Is 'd' in the command?
        # If not, throw an error and exit.
        if d.lower().find('d') == -1:
            await ctx.send('Error: we lost your dice.')
            return
        
        #help me
        elif d.lower().find('d') == 1:
            try:
                x = int(d[0])
                
                d = d[1:]
            except ValueError:
                await ctx.send('Error: we can\'t roll it ' + d[0] + ' times.')
                return
            
        # Is 'd' at an index > 1
        #
        elif d.lower().find('d') > 1:
            try:
                await ctx.send(d[:d.lower().find('d') - 1])
                
                x = int(d[:d.lower().find('d') - 1])
            
                d = d[d.lower().find('d'):]
            
            except ValueError:
                await ctx.send('Error: we can\'t roll it ' + d[:d.lower().find('d') - 1] + ' times.')
                return
            
        # Let's roll.
        # If our <x> wasn't set in the previous block, it is set to 1 by default.
        if d.lower() == "d4":
            for i in range(x):
                message = message + str(random.randint(1, 4) + m)
                message = message + ", "
            
        elif d.lower() == "d6":
            for i in range(x):
                message = message + str(random.randint(1, 6) + m)
                message = message + ", "
        
        elif d.lower() == "d8":
            for i in range(x):
                message = message + str(random.randint(1, 8) + m)
                message = message + ", "
            
        elif d.lower() == "d10":
            for i in range(x):
                message = message + str(random.randint(1, 10) + m)
                message = message + ", "
            
        elif d.lower() == "d12":
            for i in range(x):
                message = message + str(random.randint(1, 12) + m)
                message = message + ", "
        
        elif d.lower() == "d20":
            for i in range(x):
                message = message + str(random.randint(1, 20) + m)
                message = message + ", "
            
        elif d.lower() == "d100":
            for i in range(x):
                message = message + str(random.randint(1, 100) + m)
                message = message + ", "
            
        message = message + "\n"
    
    await ctx.send(message)
        
        
            
        

        
        
# il
#
# Sort and print the current 'Initiative List'.
@bot.command(name = 'il', help = 'Show the \'Initiative List\'!')
async def il(ctx):
    
    await ctx.send(reversed(sorted(bot.init_list.items(), key = lambda kv: (kv[1], kv[0]))))
        
# iladd
#
# Add an item to the 'Initiative List'.
@bot.command(name = 'iladd', help = 'Add a name and initiative to the \'Initiative List\'.\n.iladd <init> <name>')
async def iladd(ctx, init, *name):
    
    try:
        bot.init_list[' '.join(name)] = int(init)
        
        await ctx.send('Added ' + ' '.join(name) + ' to the \'Initiative List\'!')
        
    except ValueError:
        await ctx.send('Error: there was a problem adding that to the initiative list.')
        
        
# ilflush
#
# Remove all items from the 'Initiative List'.
@bot.command(name = 'ilflush', help = 'Flush the \'Initiative List\'!')
async def ilflush(ctx):
    bot.init_list.clear()
    
    await ctx.send('Cleared the \'Initiative List!\'')

# ilrem
#
# Remove an item from the 'Initiative List'.
@bot.command(name = 'ilrem', help = 'Remove a name and initiative from the \'Initiative List\'.\n.ilrem <name>\n')
async def ilrem(ctx, *name):
    
    try:
        del bot.init_list[' '.join(name)]
        
        await ctx.send('We deleted ' + ' '.join(name) + ' from the \'Initiative List\'!')
    except:
        await ctx.send('Error: we couldn\'t delete ' + ' '.join(name) + ' from the \'Initiative List\'!')
        
        
        
        
bot.run(TOKEN)


# In[ ]:




