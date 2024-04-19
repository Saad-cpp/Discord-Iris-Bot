import discord
import json
import requests

from disc_func import *
import lriris
import nbiris
import knniris

global model
model = 1
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


def get_quotes():
    req = requests.get("https://zenquotes.io/api/random")
    data = json.loads(req.text)
    quote = data[0]["q"] + " - " + data[0]["a"]
    return quote


def get_help():
    cmd = (
        "$quote: To get a quote\n"
        "$LR: to choose Logistic Regression Model\n"
        "$NB: to choose Naive Bayes Model\n"
        "$KNN: to choose K-Nearest Model\n"
        "$predict val1, val2, val3, val4: to predict"
    )
    return cmd


def separate(message):
    msg = str(message.content[9:])
    msg = msg.split(",")
    msg = list(map(float, msg))
    print(msg)
    return msg


@client.event
async def on_message(message):
    global model
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        print("Hello received")
        await message.channel.send("Hello!")

    if message.content.startswith("$help"):
        await message.channel.send(get_help())

    if message.content.startswith("$quote"):
        await message.channel.send(get_quotes())

    if message.content.startswith("$LR"):
        model = 1
        await message.channel.send(lriris.get_accuracy())

    if message.content.startswith("$NB"):
        model = 2
        await message.channel.send(nbiris.get_accuracy())

    if message.content.startswith("$KNN"):
        model = 3
        await message.channel.send(knniris.get_accuracy())

    if message.content.startswith("$predict"):
        x = separate(message)

        if model == 1:
            await message.channel.send(lriris.predict_result(x))
        elif model == 2:
            await message.channel.send(nbiris.predict_result(x))
        else:
            await message.channel.send(knniris.predict_result(x))

    if message.content.startswith("$bye"):
        await message.channel.send(byebye())


client.run("----")
