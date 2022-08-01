from http import client
from discord.ext import commands
from discord.utils import get
from discord import Embed
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import discord


class MyWelcomeMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def welcome_menu(self, ctx):
        description = """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.
        """
        embed = Embed(title = 'Welcome to minto! :worried:', 
                      url='https://minto.finance/', 
                      description=description, color=discord.Color.blue())
        embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
        components = [[
                Button(style = ButtonStyle.URL, url = 'https://bitcoin.org/ru/', label='YouTube', emoji="😕"),
                Button(style = ButtonStyle.URL, url = 'https://bitcoin.org/ru/', label='Twitter', emoji="👀"),
                Button(style = ButtonStyle.URL, url = 'https://bitcoin.org/ru/', label='Website', emoji="🕸️"),
        ]]
        await ctx.send(embed=  embed, components = components)

class MyInfoMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info_menu(self, ctx):
        description = """
        It is a long established fact that a reader will be distracted by 
        the readable content of a page when looking at its layout.
        """
        links = """
        [Website](https://minto.finance/)
        [Telegram](https://web.telegram.org/k/)
        [Inst](https://minto.finance/)
        """
        information = """
        Founded: 15 декабря 2020 г.
        Owner: OhOverLord
        Interesting link: https://slovnik.seznam.cz/
        """
        embed = Embed(title = 'Info', 
                      url='https://minto.finance/about', 
                      description=description, color=discord.Color.blue())
        embed.add_field(name="Quick Links", value=links, inline=True)
        embed.add_field(name="Information", value=information, inline=True)
        embed.add_field(name="Vote on Top.gg!", value="Use the dropdown one category at a time to avoid rate limits!", inline=False,)
        components = [[
                Button(style = ButtonStyle.blue, label = 'Roles info', custom_id="bth_roles_info"),
                Button(style = ButtonStyle.blue, label = 'Booster Perks', custom_id="bth_booster_perks"),
                Button(style = ButtonStyle.blue, label = 'Server rules', custom_id="bth_server_rules"),
        ]]
        await ctx.send(embed = embed, components = components)
        while True:
            response = await self.client.wait_for('button_click', check = lambda message: message.author == ctx.author)
            if response.component.custom_id == 'bth_roles_info':
                await ctx.send('ok', hidden=True)
            elif response.component.custom_id == 'bth_booster_perks':
                await response.respond(content = 'Деньги успешно !')
            elif response.component.custom_id == 'bth_server_rules':
                await response.respond(content = 'Деньги !')


class MySelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def select_menu(self, ctx):
        embed = Embed(title = 'Frequently Asked Questions', description="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humou")
        components = [
            Select(
                placeholder = "Select something!",
                options = [
                    SelectOption(label = "When will BTCMT be listed on CEX?", value = "A"),
                    SelectOption(label = "How many tokens were sold?", value = "B"),
                    SelectOption(label = "What's new this week?", value = "C"),
                    SelectOption(label = "What is Minto Finance?", value = "D"),
                    SelectOption(label = "How are you different from other projects?", value = "E"),
                ]
            )
        ]
        await ctx.send(embed=embed, components=components)
        while True:
            response = await self.client.wait_for("select_option")
            if response.message.id == 891587821368905728: #Message id(not obligatory)
                await response.respond(type=6)
            if response.values[0] == "A":
                await response.respond(content = "We are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet.")
            elif response.values[0] == "B":
                await response.respond(content = "You can find out how many tokens have been sold on our website or using our smart contract.")
            elif response.values[0] == "C":
                await response.respond(content = "You can find all the updates and news on our Telegram or Twitter pages.")
            elif response.values[0] == "D":
                await response.respond(content = "The Minto token is backed by actively operating Bitcoin mining hardware. There are no high entry barriers, risks, or maintenance issues for the end user. You can buy tokens to receive rewards in the same way a miner does, or you can buy and sell mining power to make money, but you don't have to deal with the hassles of traditional mining.")
            elif response.values[0] == "E":
                await response.respond(content = "We are very proud that our crypto project is eco-friendly. As you probably know, bitcoin mining consumes a lot of energy. Various other mining operations use electricity generated by burning coal, which is sourced from the power grid. We don't. Minto DeFi project uses only eco-friendly mining.")


def setup(client):
    DiscordComponents(client)
    client.add_cog(MyInfoMenu(client))
    client.add_cog(MyWelcomeMenu(client))
    client.add_cog(MySelectMenu(client))
