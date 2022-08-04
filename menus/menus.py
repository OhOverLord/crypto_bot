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
        embed.add_field(name="\u200b", value=settings.FIRST_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.FIFTH_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.TENTH_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.TWENTY_FIFTH_LVL, inline=True)
        embed.add_field(name="\u200b", value=settings.FIFTY_FIFTH_LVL, inline=True)
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

    def select_info_menu(self, title, description):
        embed = discord.Embed(title=title, 
                      description=description, 
                      color=0x5bf1b9)
        return embed

    @commands.command()
    async def select_menu(self, ctx):
        embed = Embed(title = 'Frequently Asked Questions', description="Select your question from the dropdown below to get an answer to! If your question isn't listed here, feel free to ask @minto_support ")
        components = [
            Select(
                placeholder = "Select something!",
                options = [
                    SelectOption(label = "What is Minto Finance?", value = "What is Minto Finance?", description="FAQ 1"),
                    SelectOption(label = "How are you different from other projects?", value = "How are you different from other projects?", description="FAQ 2"),
                    SelectOption(label = "When will BTCMT be listed on CEX?", value = "When will BTCMT be listed on CEX?", description="FAQ 3"),
                    SelectOption(label = "How many tokens were sold?", value = "How many tokens were sold?", description="FAQ 4"),
                    SelectOption(label = "What's new this week?", value = "What's new this week?", description="FAQ 5"),
                    SelectOption(label = "What’s the total amount of tokens available for sale?", value = "What’s the total amount of tokens available for sale?", description="FAQ 6"),
                    SelectOption(label = "Are there any pictures of the Karelia hydro mining site and the data center?", value = "Are there any pictures of the Karelia hydro mining site and the data center?", description="FAQ 7"),
                    SelectOption(label = "Are there any plans to increase the hashrate per 100 tokens, like in other similar projects?", value = "Are there any plans to increase the hashrate per 100 tokens, like in other similar projects?", description="FAQ 8"),
                    SelectOption(label = "If bitcoin generates a fork when we are mining, could we also get the coin of the Bitcoin fork?", value = "If bitcoin generates a fork when we are mining, could we also get the coin of the Bitcoin fork?", description="FAQ 9"),
                    SelectOption(label = "Whom should I contact with marketing proposals?", value = "Whom should I contact with marketing proposals?", description="FAQ 10"),
                ]
            )
        ]
        await ctx.send(embed=embed, components=components)
        while True:
            response = await self.client.wait_for("select_option")
            if response.message.id == 891587821368905728: #Message id(not obligatory)
                await response.respond(type=6)
            try:
                await response.respond(embed=self.select_info_menu(title=response.values[0], description=settings.FAQ[response.values[0]]), ephemeral=True)
            except:
                print("this question doesn't exist")


def setup(client):
    DiscordComponents(client)
    client.add_cog(MyInfoMenu(client))
    client.add_cog(MyWelcomeMenu(client))
    client.add_cog(MySelectMenu(client))
