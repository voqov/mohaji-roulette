import discord
import os
from discord_slash import SlashCommand
import random

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)
list = ["<무작위> 숙련자","<무작위> 레벨링","<무작위> 506070", "<무작위> 토벌전",
        "<고대 무기: 제타> 한 단계 완성",
        "<고대 무기: 아니마> 한 단계 완성",
        "<고대 무기: 에우레카> 한 단계 완성",
        "<고대 무기: 레지스탕스> 한 단계 완성",
        "<디아뎀> 500개 채집",
        "<쿠로의 공상 수첩> 4개 완료",
        "<총당님> 1클",
        "<탈 것: 용> 2클",
        "<트리플 트라이어드> 승부해서 1장 얻기",
        "<공략 수첩: 골드 소서> 2개 완료",
        "인벤토리 정리",
        "<군힐드의 사원> 1클",
        "<남부 보즈야 전선> 돌발 교전 3클",
        "<에덴의 낙원: 재생> 일반 파밍",
        "<고대 도구> 한 직업 완성",
        "<청마도사> 레벨 1 올리기",
        "<청마도사> 가면 무투대회 2회 승리하기",
        "골드소서 패션 체크 80점 이상 받기"
    ]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@slash.slash(
    name="모하지",
    description="무얼할지 못 정한 당신을 위해 룰-렛을 굴려드립니다."
)
async def command_mohaji(ctx):
    embed=discord.Embed(title=random.choice(list), description="자, 어서 하러 갑시다!", color=0x38d7ff)
    embed.set_author(name=ctx.author.name + "님이 해야할 일은", icon_url=ctx.author.avatar_url)
    embed.set_footer(text="엥? 이미 해버린거라구요? 그럼 다시 `/모하지`")
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.send(embed=embed)

client.run(os.environ['token'])
