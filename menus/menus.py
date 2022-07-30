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

    async def roles_info_menu(self):
        description = """
        These roles are usually harder to unlock and show some sign of authority/popularity 
        within Discord or the Community.
        """
        embed = Embed(title = 'Roles info', 
                      url='https://minto.finance/about', 
                      description=description, color=discord.Color.blue())
        return embed

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
        msg_with_buttons = await ctx.send(embed = embed, components = components)

        def check_button(i: discord.Interaction):
            return i.author == ctx.author and i.message == msg_with_buttons

        interaction = await self.client.wait_for('button_click', check=check_button)

        embed = discord.Embed(title='You pressed an Button',
        description=f'You pressed a button.',
        color=discord.Color.random())
        await interaction.respond(embed=embed)


class MySelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def select(self, ctx):
        embed = Embed(title = 'Frequently Asked Questions', description="There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humou")
        components = [
            Select(
                placeholder = "Select something!",
                options = [
                    SelectOption(label = "A", value = "A"),
                    SelectOption(label = "B", value = "B")
                ]
            )
        ]
        await ctx.send(embed=embed, components=components)


def setup(client):
    DiscordComponents(client)
    client.add_cog(MyInfoMenu(client))
    client.add_cog(MyWelcomeMenu(client))
    client.add_cog(MySelectMenu(client))
