from discord.ext import commands
from discord import Embed
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import settings
import discord


class MyWelcomeMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def welcome_menu(self, ctx):
        embed = Embed(title = 'Welcome to Minto Discord! :worried:', 
                      description=settings.WELCOME_MENU_DESCRIPTION)
        components = [[
                Button(style = ButtonStyle.URL, url = 'https://t.me/btcmtofficial', label='Telegram', emoji="😕"),
                Button(style = ButtonStyle.URL, url = 'https://twitter.com/BTCMTOfficial', label='Twitter', emoji="👀"),
                Button(style = ButtonStyle.URL, url = 'https://minto.finance/', label='Website', emoji="🕸️"),
        ]]
        await ctx.send(embed=  embed, components = components)

class MyInfoMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    def roles_info_menu(self):
        embed = discord.Embed(title=":scroll: Special roles", 
                      description=settings.CONTENT_ROLES, 
                      color=0x5bf1b9)
        embed.add_field(name="1 level — <@MiTrainee>", value=settings.FIRST_LVL, inline=True)
        embed.add_field(name="5 level — <@MiJunior>", value=settings.FIFTH_LVL, inline=True)
        embed.add_field(name="10 level — <@MiMiddle>", value=settings.TENTH_LVL, inline=True)
        embed.add_field(name="25 level — <@MiSenior>", value=settings.TWENTY_FIFTH_LVL, inline=True)
        embed.add_field(name="55 level — <@MiLead>", value=settings.FIFTY_FIFTH_LVL, inline=True)
        return embed
    
    def chats_info_menu(self):
        embed = discord.Embed(title=":scroll: Chats", 
                      description=settings.CONTENT_CHATS, 
                      color=0x5bf1b9)
        embed.add_field(name="Community", value=settings.COMMUNITY_CHATS, inline=True)
        embed.add_field(name="Information", value=settings.INFORMATION_CHATS, inline=True)
        return embed

    def rules_info_menu(self):
        embed = discord.Embed(title=":gift: RULES", 
                      description=settings.RULES_INFO, 
                      color=0x5bf1b9)
        return embed
        

    @commands.command()
    async def info_menu(self, ctx):
        embed = Embed(title = '', 
                      url='https://minto.finance/about', 
                      description=settings.INFO_MENU_DESCRIPTION, color=0x5bf1b9)
        embed.add_field(name="Quick Links", value=settings.INFO_MENU_LINKS, inline=True)
        embed.add_field(name="Information", value=settings.INFO_MENU_INFORMATION, inline=True)
        embed.add_field(name="Vote on Top.gg!", value="Use the dropdown one category at a time to avoid rate limits!", inline=False,)
        components = [[
                Button(style = ButtonStyle.grey, label = 'Roles info', custom_id="bth_roles_info"),
                Button(style = ButtonStyle.grey, label = 'Chats', custom_id="chats"),
                Button(style = ButtonStyle.grey, label = 'Server rules', custom_id="bth_server_rules"),
        ]]
        await ctx.send(embed = embed, components = components)
        while True:
            response = await self.client.wait_for('button_click', check = lambda message: message.author == ctx.author)
            if response.component.custom_id == 'bth_roles_info':
                await response.respond(embed=self.roles_info_menu(), ephemeral=True)
            elif response.component.custom_id == 'chats':
                await response.respond(embed=self.chats_info_menu(), ephemeral=True)
            elif response.component.custom_id == 'bth_server_rules':
                await response.respond(embed=self.rules_info_menu(), ephemeral=True)


class MySelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def select_menu(self, ctx):
        embed = Embed(title = 'Frequently Asked Questions', description="Select your question from the dropdown below to get an answer to! If your question isn't listed here, feel free to ask @minto_support ")
        components = [
            Select(
                placeholder = "Select something!",
                options = [
                    SelectOption(label = "When will BTCMT be listed on CEX?", value = "A", description="FAQ 1"),
                    SelectOption(label = "How many tokens were sold?", value = "B", description="FAQ 2"),
                    SelectOption(label = "What's new this week?", value = "C", description="FAQ 3"),
                    SelectOption(label = "What is Minto Finance?", value = "D", description="FAQ 4"),
                    SelectOption(label = "How are you different from other projects?", value = "E", description="FAQ 5"),
                ]
            )
        ]
        await ctx.send(embed=embed, components=components)
        while True:
            response = await self.client.wait_for("select_option")
            if response.message.id == 891587821368905728: #Message id(not obligatory)
                await response.respond(type=6)
            if response.values[0] == "A":
                await response.respond(content = """When will BTCMT be listed on CEX?\nWe are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet.""")
            elif response.values[0] == "B":
                await response.respond(content = "How many tokens were sold?\nYou can find out how many tokens have been sold on our website or using our smart contract.")
            elif response.values[0] == "C":
                await response.respond(content = "What's new this week?\nYou can find all the updates and news on our Telegram or Twitter pages.")
            elif response.values[0] == "D":
                await response.respond(content = "What is Minto Finance?\nThe Minto token is backed by actively operating Bitcoin mining hardware. There are no high entry barriers, risks, or maintenance issues for the end user. You can buy tokens to receive rewards in the same way a miner does, or you can buy and sell mining power to make money, but you don't have to deal with the hassles of traditional mining.")
            elif response.values[0] == "E":
                await response.respond(content = "How are you different from other projects?\nWe are very proud that our crypto project is eco-friendly. As you probably know, bitcoin mining consumes a lot of energy. Various other mining operations use electricity generated by burning coal, which is sourced from the power grid. We don't. Minto DeFi project uses only eco-friendly mining.")


def setup(client):
    DiscordComponents(client)
    client.add_cog(MyInfoMenu(client))
    client.add_cog(MyWelcomeMenu(client))
    client.add_cog(MySelectMenu(client))
