import discord
import os
from discord_slash import SlashCommand
import random

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)
list = ["고된무기: 제타",
"고된무기: 아니마",
"고된무기: 에우레카",
"고된무기: 레지스탕스",
"디아뎀 채집물 500개",
"쿠로수첩",
"총당님",
"용작",
"트트카드",
"골드소서 일주",
"인벤토리 정리",
"군힐드",
"재생일반",
"고된도구"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

guild_ids = [518373344072957952]

@slash.slash(
    name="모하지",
    description="무얼할지 못 정한 당신을 위해 룰-렛을 굴려드립니다.",
    guild_ids=guild_ids
)
async def command_mohaji(ctx):
    embed=discord.Embed(title="굴려굴려 모하지 룰-렛", description="오늘도 무얼 해야할지 고민인 당신을 위해 제가 골라왔어요!", color=0x38d7ff)
    embed.add_field(name=random.choice(list), value="Let's do it!")
    embed.set_footer(text="엥? 이미 해버린거라구요? 그럼 다시 `/모하지`")
    await ctx.send(embed=embed)

client.run(os.environ['token'])
