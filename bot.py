import discord

TOKEN = "MTA0MjE2MjY0NTU1MTI5MjQ4Ng.Gjg9PA.IKew4hOjZSC-iEyCVg4TTDEmJ7UHoqJCvk5c1U"



client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f"Bot dziala!")


client.run(TOKEN)