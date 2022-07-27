from discord.ext import commands
from discord import Embed
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import discord

from dpymenus import Page, TextMenu, Page


class MyButtonMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def buttons(self, ctx):
        msg = await ctx.send(
            embed = Embed(title = 'Вы точно хотите перевевсти деньги?', timestamp = ctx.message.created_at),
            components = [
                Button(style = ButtonStyle.green, label = 'Да'),
                Button(style = ButtonStyle.URL, url = 'https://bitcoin.org/ru/', label='Нащ сайт')
            ])
        responce = await self.client.wait_for('button_click', check = lambda message: message.author == ctx.author)
        if responce.component.label == 'Да':
            await responce.respond(content = 'Деньги успешно переведены!')

class MyTextMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def menu(self, ctx):

        page1 = Page(
            title='Something about bitcoin',
            description="""
            About us: https://www.bitcoin.com/
            Something new: https://en.wikipedia.org/wiki/Bitcoin
            """,
        )
        page1.set_footer(text='You can trust')

        menu = TextMenu(ctx)
        menu.add_pages([page1, ])
        await menu.open()


class MySelectMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def select(self, ctx):
        await ctx.send(
        embed = Embed(title = 'Что вы хотите выбрать?', timestamp = ctx.message.created_at),
        components = [
            Select(
                placeholder = "Select something!",
                options = [
                    SelectOption(label = "A", value = "A"),
                    SelectOption(label = "B", value = "B")
                ]
            )
        ]
    )


def setup(client):
    DiscordComponents(client)
    client.add_cog(MyTextMenu(client))
    client.add_cog(MyButtonMenu(client))
    client.add_cog(MySelectMenu(client))
