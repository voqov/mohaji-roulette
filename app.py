import discord
import os
from discord_slash import SlashCommand

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

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
    embed.add_field(name="청마도사 1렙업하기", value="가 나왔어요!")
    embed.set_footer(text="엥? 이미 해버린거라구요? 그럼 다시 굴려굴려 모하지 룰-렛")
    await ctx.send(embed=embed)

client.run(os.environ['token'])
