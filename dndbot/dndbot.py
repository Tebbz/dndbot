#!/usr/bin/env python
# coding: utf-8

# In[30]:


import os
import sys
import random
import asyncio

import discord
from discord import opus
from discord.ext import commands

from dotenv import load_dotenv




load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix = '.')



bot.dm = None
bot.il = []



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord.')


# .r
#
# Parses a list of roll commands.
# On success: sends a message containing the results of the dice rolls.
# On failure: sends an error message for each failed command.
#
# Input: *param ==> a list of commands for the .r function. // d4 1d4 1d4+1
@bot.command(name = 'r', help = 'Rolls a die or dice.\n\n.r (#)(die)(modifier) ...\nYou must select an accepted \'die\'.\nYou can input a # to roll that die a certain number of times.\nYou can input a modifier to be added to those rolls.\n\nExample: .r 2d4+2')
async def _r(ctx, *param):
    embed = discord.Embed(title = ctx.author.name + ' Rolled...', description = '', color = 0xffffff)

    for cmd in param:
        cmd = cmd.lower()
        d = ""
        m = 0
        x = 1
        t = 0
        rlist = []

        if cmd.count('d') != 1:
            embed.add_field(name = 'Error: invalid command.', value = 'We skipped *' + cmd + '*.', inline = False)
            continue
        
        else:
            if '+' in cmd:
                if cmd.find('+') < cmd.find('d'):
                    embed.add_field(name = 'Error: that '+' is in the wrong place.', value = 'We skipped *' + cmd + '*.', inline = False)
                    continue

                else:
                    try:
                        m = int(cmd[cmd.find('+'):])

                    except ValueError:
                        embed.add_field(name = 'Error: invalid modifier.', value = 'We skipped *' + cmd + '*.', inline = False)
                        continue
            
            elif '-' in cmd:
                if cmd.find('-') < cmd.find('d'):
                    embed.add_field(name = 'Error: that '-' is in the wrong place.', value = 'We skipped *' + cmd + '*.', inline = False)
                    continue
                
                else:
                    try:
                        m = int(cmd[cmd.find('-'):])

                    except ValueError:
                        embed.add_field(name = 'Error: invalid modifier.', value = 'We skipped *' + cmd + '*.', inline = False)
                        continue

            if cmd.find('d') > 2:
                embed.add_field(name = 'Error: TOO MANY DICE.', value = 'We skipped *' + cmd + '*.', inline = False)
                continue

            elif cmd.find('d') > 0:
                try:
                    x = int(cmd[:cmd.find('d')])

                except ValueError:
                    embed.add_field(name = 'Error: invalid # of dice.', value = 'We skipped *' + cmd + '*.', inline = False)
                    continue

            if 'd100' in cmd:
                d = 'd100'
            
            elif 'd20' in cmd:
                d = 'd20'
            
            elif 'd12' in cmd:
                d = 'd12'

            elif 'd10' in cmd:
                d = 'd10'

            elif 'd8' in cmd:
                d = 'd8'

            elif 'd6' in cmd:
                d = 'd6'

            elif 'd4' in cmd:
                d = 'd4'

            elif 'd2' in cmd:
                d = 'd2'

            elif 'dfaggot' in cmd:
                d = 'dfaggot'

            elif 'dcrit' in cmd:
                d = 'dcrit'

            elif 'dsmoke' in cmd:
                d = 'dsmoke'

            else:
                embed.add_field(name = 'Error: that\'s not a real die.', value = 'We skipped *' + cmd + '*.', inline = False)
                continue

        if d == 'dfaggot':
            for i in range(x):
                rlist.append('**faggot**')

        elif d == 'dcrit':
            for i in range(x):
                rlist.append('**' + str(20 + m) + '**')

            d = 'd20'
        
        elif d == 'dsmoke':
            for i in range(x):
                rlist.append('**420**')

        else:
            t = 0

            for i in range(x):
                f = int(d[d.find('d') + 1:])
                g = random.randint(1, f)

                if g == f:
                    g = g + m
                    t = t + g

                    rlist.append('**' + str(g) + '**')

                else:
                    g = g + m
                    t = t + g

                    rlist.append(str(g))
            
            rlist.append('(**' + str(t) + '**)')
           
        embed.add_field(name = str(d) + ' ' + str(m) if m < 0 else str(d) + ' +' + str(m), value = '_' + str(rlist).translate(str.maketrans({"'" : None, "]" : None, "[" : None})) + '_', inline = False)

    await ctx.send(embed = embed, delete_after = 60.0)

    if isinstance(ctx.channel, discord.DMChannel):
        return

    await ctx.message.delete()
    return



# .dm
#
# Shows the current 'Dungeon Master'.
#
# Input: none.
@bot.command(name = 'dm', help = 'Shows the current *Dungeon Master*.')
async def _dm(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        errembed = discord.Embed(title = 'S- s... Sorry', description = 'I- I... don\'t think we should talk about *this* in *private*.', color = 0xffffff)
        errembed.set_footer(text = 'U- uh... See you in the other channel.')

        await ctx.send(embed = errembed, delete_after = 60.0)
        return  

    if bot.dm is None:
        embed = discord.Embed(title = 'Dungeon Master', description = '*There is no Dungeon Master at the moment*.', color = 0xffffff)

        await ctx.send(embed = embed, delete_after = 60.0)
        await ctx.message.delete()
        return

    else:
        embed = discord.Embed(title = 'Dungeon Master', description = '**' + str(bot.dm) + '** is the current *Dungeon Master*.', color = 0xffffff)

        await ctx.send(embed = embed, delete_after = 60.0)
        await ctx.message.delete()
        return



# .dmrem
#
# Removes the current 'Dungeon Master' if possible.
# Sends a confirmation message on success.
# Sends an error message on failure.
#
# Input: none.
@bot.command(name = 'dmrem', help = 'Removes the current *Dungeon Master*.')
async def _dmrem(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        errembed = discord.Embed(title = 'S- s... Sorry', description = 'I- I... don\'t think we should talk about *this* in *private*.', color = 0xffffff)
        errembed.set_footer(text = 'U- uh... See you in the other channel.')

        await ctx.send(embed = errembed, delete_after = 60.0)
        return  

    if bot.dm is None:
        errembed = discord.Embed(title = 'Dungeon Master', description = '**Error**: *Couldn\'t remove the current Dungeon Master*.', color = 0xffffff)
        errembed.set_footer(text = 'Was there even a DM in the first place? Probably not...')

        await ctx.send(embed = errembed, delete_after = 60.0)
        await ctx.message.delete()
        return
    
    else:
        embed = discord.Embed(title = 'Dungeon Master', description = '**' + str(bot.dm) + '** is no longer the current *Dungeon Master*.', color = 0xffffff)
        embed.set_footer(text = '... Finally...')

        bot.dm = None

        await ctx.send(embed = embed, delete_after = 60.0)
        await ctx.message.delete()
        return



# .dmset
#
# Sets the 'Dungeon Master' as the User who sent the command.
#
# Input: none.
@bot.command(name = 'dmset', help = 'Sets the *Dungeon Master* to the user that calls the command if possible.')
async def _dmset(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        errembed = discord.Embed(title = 'S- s... Sorry', description = 'I- I... don\'t think we should talk about *this* in *private*.', color = 0xffffff)
        errembed.set_footer(text = 'U- uh... See you in the other channel.')

        await ctx.send(embed = errembed, delete_after = 60.0)
        return       

    if bot.dm is None:
        bot.dm = ctx.author

        embed = discord.Embed(title = 'Dungeon Master', description = '**' + str(bot.dm) + '** *has been selected as the Dungeon Master*.', color = 0xffffff)
        embed.set_footer(text = 'Have FUN with their campaign! ... I hope it\'s fun...')

        await ctx.send(embed = embed, delete_after = 60.0)
        await ctx.message.delete()
        return

    else:
        errembed = discord.Embed(title = 'Dungeon Master', description = '**Error**: We can\'t set *' + str(ctx.author) + '* as the Dungeon Master because **' + str(bot.dm) + '** is the Dungeon Master!', color = 0xffffff)
        errembed.set_footer(text = 'There can ONLY be one.')

        await ctx.send(embed = errembed, delete_after = 60.0)
        await ctx.message.delete()
        return



# .il
#
# Shows the 'Initiative List' if the command wasn't send in a DM Channel.
#
# Input: none.
@bot.command(name = 'il', help = 'Shows the *Initiative List*.')
async def _il(ctx):
    embed = discord.Embed(title = 'Initiative List', description = 'Let\'s see who\'s at the top of the order.')

    tl = []

    if bot.il == []:
        errembed = discord.Embed(title = 'Initiative List', description = 'We couldn\'t show the *Initiative List*.')
        errembed.set_footer(text = 'I\'ll bet it doesn\'t have anyone in it...')

        await ctx.send(embed = errembed, delete_after = 60.0)
        await ctx.message.delete()
        return

    for x in bot.il:
        if tl == []:
            if x[2] == True:
                if len(x[0]) == 1:
                    tl.append([x[1], x[0] + '***'])
                
                else:
                    tl.append([x[1], x[0].replace(x[1:], '***')])
            
            else:
                tl.append([x[1], x[0]])

        else:
            for i in range(len(tl)):
                if x[1] == tl[i][0]:
                    if x[2] == True:
                        if len(x[0]) == 1:
                            tl[i].append(x[0] + '***')
                            break

                        else:
                            tl[i].append(x[0].replace(x[0][1:], '***'))
                            break

                    else:
                        tl[i].append(x[0])
                        break
                
            else:
                if x[2] == True:
                    if len(x[0]) == 1:
                        tl.append([x[1], x[0] + '***'])

                    else:
                        tl.append([x[1], x[0].replace(x[0][1:], '***')])

                else:
                    tl.append([x[1], x[0]])

    tl.sort(key = lambda k: k[0], reverse = True)

    for i in range(len(tl)):
        embed.add_field(name = str(tl[i][0]), value = str(tl[i][1:]).translate(str.maketrans({'[' : None, ']' : None, "'" : None})) , inline = False)

    await ctx.send(embed = embed, delete_after = 60.0)

    if isinstance(ctx.channel, discord.DMChannel):
        return

    await ctx.message.delete()
    return



# .iladd
#
# Attempts to create an item in the 'Initiative List' with <i> as their 'Initiative' value and <name> as their 'Name'.
# If this command was sent in a DM Channel: the item will be 'Hidden'.
# Otherwise: the item will be 'Shown'.
#
# Input: <i> and <name>.
# <i> is the 'Initiative' of the element.
# <name> is the 'Name' of the element.
@bot.command(name = 'iladd', help = 'Attempts to add an item to the *Initiative List*.\n\n.iladd (initiative) (name...)')
async def _iladd(ctx, init, *name):
    try:
        init = int(init)

    except ValueError:
        errembed = discord.Embed(title = 'Initiative List', description = '**Error**: We encountered a *Value Error*.', color = 0xffffff)

        await ctx.send(embed = errembed, delete_after = 60.0)
        
        if isinstance(ctx.channel, discord.DMChannel):
            return

        await ctx.message.delete()
        return

    try:
        name = ' '.join(name)

    except Exception:
        errembed = discord.Embed(title = 'Initiative List', description = '**Error**: We encountered an *Error*.', color = 0xffffff)

        await ctx.send(embed = errembed, delete_after = 60.0)
        
        if isinstance(ctx.channel, discord.DMChannel):
            return

        await ctx.message.delete()
        return

    if isinstance(ctx.channel, discord.DMChannel):
        bot.il.append([name, init, True])

        embed = discord.Embed(title = 'Initiative List', description = 'We added **_' + str(name) + '_** to the list. **_' + str(name) + '_** will show up as:', color = 0xffffff)

        if len(name) == 1:
            embed.add_field(name = str(init), value = name + '***', inline = False)
        
        elif len(name) > 1:
            embed.add_field(name = str(init), value = name.replace(name[1:], '***'), inline = False)

        else:
            print('We had an error.')

        await ctx.send(embed = embed, delete_after = 60.0)
        return

    else:
        bot.il.append([name, init, False])

        embed = discord.Embed(title = 'Initiative List', description = 'We added **_' + str(name) + '_** to the list. **_' + str(name) + '_** will show up as:', color = 0xffffff)
        embed.add_field(name = str(init), value = str(name), inline = False)

        await ctx.send(embed = embed, delete_after = 60.0)
        await ctx.message.delete()
        return



# .ilflush
#
# Flush the current 'Initiative List'.
#
# Input: none.
@bot.command(name = 'ilflush', help = 'Flushes the current *Initiative List*.')
async def _ilflush(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        errembed = discord.Embed(title = 'S- s... Sorry', description = 'I- I... don\'t think we should talk about *this* in *private*.', color = 0xffffff)
        errembed.set_footer(text = 'U- uh... See you in the other channel.')

        await ctx.send(embed = errembed, delete_after = 60.0)
        return

    bot.il.clear()

    embed = discord.Embed(title = 'Initiative List', description = 'We flushed the *Initiative List*.', color = 0xffffff)
    embed.set_footer(text = '... You\'re welcome.')

    await ctx.send(embed = embed, delete_after = 60.0)
    await ctx.message.delete()
    return



# .ilshow
#
# Searches for a <Name> to be 'shown' within the 'Initiative List'.
# If found: determines whether the 'Hidden' value is 'True' or 'False'.
# If True: change it to 'False'.
# If False: send an error message.
# If not found: sends an error message.
#
# Input: <name>
# <Name> is the 'Name' of the element to be shown.
@bot.command(name = 'ilshow', help = 'Show an item on the *Initiative List*.')
async def _ilshow(ctx, *name):
    try:
        name = ' '.join(name)

    except Exception:
        return
    
    for x in range(len(bot.il)):
        if bot.il[x][0] == name:
            if bot.il[x][2] == True:
                bot.il[x][2] = False

                embed = discord.Embed(title = 'Initiative List', description = '*' + str(bot.il[x][0]) + '* is now shown.', color = 0xffffff)

                await ctx.send(embed = embed, delete_after = 60.0)

                if isinstance(ctx.channel, discord.DMChannel):
                    return

                await ctx.message.delete()
                return
            
            else:
                errembed = discord.Embed(title = 'Initiative List', description = '**Error**: We couldn\'t show *' + str(bot.il[x][0]) + '*.', color = 0xffffff)

                await ctx.send(embed = errembed, delete_after = 60.0)
                await ctx.message.delete()
                return
       
    errembed = discord.Embed(title = 'Initiative List', description = '**Error**: We couldn\'t find *' + name + '*.', color = 0xffffff)

    await ctx.send(embed = errembed, delete_after = 60.0)

    if isinstance(ctx.channel, discord.DMChannel):
        return

    await ctx.message.delete()
    return
    


# .ilrem
#
# Searches for a <Name> within the <Initiative List>.
# If found: it deletes it and sends a confirmation message.
# If not found: it sends an appropriate error message.
#
# Input: <Name>
# <Name> is the name of the item to be removed.
@bot.command(name = 'ilrem', help = 'Removes an item from the *Initiative List*.\n\n.ilrem (name)')
async def _ilrem(ctx, *name):
    try:
        name = ' '.join(name)

    except Exception:
        return

    for x in range(len(bot.il)):
        if bot.il[x][0] == name:
            embed = discord.Embed(title = 'Initiative List', description = 'We deleted **_' + str(bot.il[x][0]) + '_** from the list.', color = 0xffffff)
            embed.set_footer(text = 'R.I.P.')

            await ctx.send(embed = embed, delete_after = 60.0)
            del bot.il[x]

            if isinstance(ctx.channel, discord.DMChannel):
                return
            
            await ctx.message.delete()
            return
       
    errembed = discord.Embed(title = 'Initiative List', description = '**Error**: We couldn\'t find *' + name + '*.', color = 0xffffff)

    await ctx.send(embed = errembed, delete_after = 60.0)

    if isinstance(ctx.channel, discord.DMChannel):
        return

    await ctx.message.delete()
    return





# .s
#
# Will play a file from the \sound folder.
#
# Input: <name>
# <name> is the 'Name' of the file to be played.
@bot.command(name = 's')
async def _s(ctx, filename):
    if isinstance(ctx.channel, discord.DMChannel):
        errembed = discord.Embed(title = 'S- s... Sorry', description = 'I- I... don\'t think we should talk about *this* in *private*.', color = 0xffffff)
        errembed.set_footer(text = 'U- uh... See you in the other channel.')

        await ctx.send(embed = errembed, delete_after = 60.0)
        return    

    if ctx.message.author.voice.channel is not None:
        await ctx.message.author.voice.channel.connect()

        filename = 'res\\sound\\' + filename + '.mp3'

        src = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(filename))
        ctx.voice_client.play(src, after = lambda e: print('Player error: %s' % e) if e else None)

        await ctx.message.delete()

        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)
        
        await ctx.voice_client.disconnect()
        return

    else:
        errembed = discord.Embed(title = "Error:", description = ctx.author.name + ' is not connected to a voice channel.', color = 0xffffff)
        errembed.set_footer(text = 'Connect to a voice channel and do it again!')

        await ctx.send(embed = errembed, delete_after = 60.0)
        await ctx.message.delete()
        return






bot.run(TOKEN)


# In[ ]:




