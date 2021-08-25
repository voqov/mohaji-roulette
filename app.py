import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$모하지'):
        embed=discord.Embed(title="굴려굴려 모하지 룰-렛", description="오늘도 무얼 해야할지 고민인 당신을 위해 제가 골라왔어요!")
        embed.add_field(name="청마도사 1렙업하기", value="가 나왔어요!")
        embed.set_footer(text="엥? 이미 해버린거라구요? 그럼 다시 굴려굴려 모하지 룰-렛")
        await message.channel.send(embed=embed)

client.run(os.environ['token'])
