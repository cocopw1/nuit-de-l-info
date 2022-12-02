import discord
from discord.ext import commands
import csv
from random import randint 
#csv lib
def addincsv(url,content:str):
    file = open(url,mode='a')
    file.write(content+'\n')
    file.close()
def import_csv(url_file, delimiter) :
    with open(url_file, newline='', encoding='utf-8') as csvfile :
        file = csv.reader(csvfile, delimiter=delimiter)
        list_list = []
        for row in file :
            list_list.append(row)
    return list_list
def suprligne(url, n):
    f = open(url,"r+")
    d = f.readlines()
    f.seek(0)
    for i in range(len(d)):
        
        if i != n:
            f.write(d[i])
    f.truncate()
    f.close()
#main


intents = discord.Intents.default()

bot = commands.Bot(command_prefix='$',intents=intents)
@bot.event
async def on_message(message):
    luck= randint(0,1)
    if(luck ==00):
        if (message.author==bot.user):
            return
        mst  = import_csv("mst.csv",";")
        ms = mst[randint(0,len(mst)-1)]
        color = 0xFFFFFF
        if(ms[2]=='5'):
            color = 0xFF00FF
        elif (ms[2]=='2'):
            color =0x00FF00
        elif (ms[2]=='3'):
            color = 0xFFFF00
        elif (ms[2]=='4'):
            color = 0xFF0000
        george = discord.Embed(title = "how sad ... you got a new mst ",description="["+ms[1]+"]("+ms[5]+")",color=color)
        george.set_footer(text=message.author,icon_url=message.author.avatar)
        george.add_field(name="description :",value=ms[3])
        george.set_image(url = ms [4])
        text = str(message.author.id)+';'+ms[0]+";"+str(message.author.avatar)
        addincsv("user.csv",text)
        await message.channel.send(embed = george)


bot.run('MTA0Nzk4MjY0MjU2MzQwMzgyOA.GHQ2Xe.aa9cy2CkcvlS_7Cmn9jSsOk_AWOf_kiLvi5gRg')

