import discord
import os
from discord_slash import SlashCommand

client = discord.Client()
slash = SlashCommand(client)

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
        embed=discord.Embed(title="굴려굴려 모하지 룰-렛", description="오늘도 무얼 해야할지 고민인 당신을 위해 제가 골라왔어요!", color=0x38d7ff)
        embed.add_field(name="청마도사 1렙업하기", value="가 나왔어요!")
        embed.set_footer(text="엥? 이미 해버린거라구요? 그럼 다시 굴려굴려 모하지 룰-렛")
        await message.channel.send(embed=embed)

@slash.slash(
    name="모하지",
    description="무얼할지 못 정한 당신을 위해 룰-렛을 굴려드립니다."
)
async def command_mohaji():
    pass

client.run(os.environ['token'])
