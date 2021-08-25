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

    if message.content.startswith('#모하지'):
        embed=discord.Embed(title="굴려굴려 모하지 룰렛", description="삥-뽕- >>청마도사 1렙업하기<<입니다", color=0x00aaaa)
        # embed.set_author(name="작성자의 이름",icon_url=message.author.avatar_url)
        embed.set_footer(text="엥? 이미 해버린거라구요? 그럼 다시 굴려굴려 모하지 룰렛")
        await message.channel.send(embed=embed)

client.run(os.environ['token'])
