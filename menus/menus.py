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
        Hey! We are Minto — a Bitcoin mining platform.

        *Mining is simple. Don't you believe it? Try to mine with us!*

        We've removed all the unnecessary steps. To mine BTC, all you need is to buy and stake our BTCMT token, that equals a unit of Bitcoin mining power. 
        Our token is secured by actively operating equipment. To make it work **we use renewable energy sources with a neutral carbon footprint**. 

        Visit our [website](https://minto.finance/) and learn more about our project!
        """
        embed = Embed(title = 'Welcome to Minto Discord! :worried:', 
                      description=description)
        components = [[
                Button(style = ButtonStyle.URL, url = 'https://t.me/btcmtofficial', label='Telegram', emoji="😕"),
                Button(style = ButtonStyle.URL, url = 'https://twitter.com/BTCMTOfficial', label='Twitter', emoji="👀"),
                Button(style = ButtonStyle.URL, url = 'https://minto.finance/', label='Website', emoji="🕸️"),
        ]]
        await ctx.send(embed=  embed, components = components)

class MyInfoMenu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info_menu(self, ctx):
        description = """
        For additional questions or to contact us please write to @minto_support and we'll get back to you as soon as we can.
        """
        links = """
        :globe_with_meridians: [Website](https://minto.finance/)
        :placard: [Telegram](https://t.me/btcmtofficial)
        :fingers_crossed: [Twitter](https://twitter.com/BTCMTOfficial)
        """
        information = """
        Founded: 15 декабря 2020 г.
        Owner: @gniro#0069
        Invite: https://discord.gg/minto
        """
        embed = Embed(title = '', 
                      url='https://minto.finance/about', 
                      description=description, color=0x5bf1b9)
        embed.add_field(name="Quick Links", value=links, inline=True)
        embed.add_field(name="Information", value=information, inline=True)
        embed.add_field(name="Vote on Top.gg!", value="Use the dropdown one category at a time to avoid rate limits!", inline=False,)
        components = [[
                Button(style = ButtonStyle.grey, label = 'Roles info', custom_id="bth_roles_info"),
                Button(style = ButtonStyle.grey, label = 'Chats', custom_id="chats"),
                Button(style = ButtonStyle.grey, label = 'Server rules', custom_id="bth_server_rules"),
        ]]
        await ctx.send(embed = embed, components = components)
        content_roles = """
        For participating in games and events you will get XP. The more points — the higher your level. .
        With every level you will achieve a new role on this server, which will open up new possibilities. 

        1 level — @MiTrainee 
        • Welcome! 
        • Access to Discord

        5 level — @MiJunior 
        • Change nickname 
        • Add reactions 
        • Custom emojis

        10 level — @MiMiddle
        • Special posting
        
        25 level — @MiSenior 
        • Access to closed chat rooms 
        • Access to voice chats

        55 level — @MiLead
        • Token rewards 
        • Custom roles and emojis
        • Our adoration♥️
        """
        content_chats = """
        CHATS
        Two chat categories: information and community.

        Information
        #minto_updates — news about Minto
        #minto_faq — product faq 
        #minto_eco — environmental of Minto
        #minto_ed — educational publications

        Community
        #chat — for communication in general
        #offtop — for roles and bots
        #events-activities — announces and contests
        #memes — fun
        #minto_arena — for streams
        #sum_up — sample discussions from other channels in Discord
        #news — analysis of current news and events in the world of blockchain
        """

        rules_info = """
        RULES
        1. Be respectful to each other's opinions. NO insults, racism or harassment please. 

        2. No one should ask you to send money to the account. Please contact our moderator immediately if this happens to you.

        3. Do not post any NSFW content and limit the use of offensive language across all channels and nicknames.

        4. We are free from all forms of advertising. Do not post referral links, discord invitations or any other invitations.

        5. Impersonating members of the moderator team is a crime. Anyone caught doing this will be banned immediately.
        """
        while True:
            response = await self.client.wait_for('button_click', check = lambda message: message.author == ctx.author)
            if response.component.custom_id == 'bth_roles_info':
                await response.respond(content = content_roles)
            elif response.component.custom_id == 'chats':
                await response.respond(content = content_chats)
            elif response.component.custom_id == 'bth_server_rules':
                await response.respond(content = rules_info)


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
