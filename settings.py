import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")

WELCOME_MENU_DESCRIPTION = """
Hey! We are Minto — a Bitcoin mining platform.

*Mining is simple. Don't you believe it? Try to mine with us!*

We've removed all the unnecessary steps. To mine BTC, all you need is to buy and stake our BTCMT token, that equals a unit of Bitcoin mining power. 
Our token is secured by actively operating equipment. To make it work **we use renewable energy sources with a neutral carbon footprint**. 

Visit our [website](https://minto.finance/) and learn more about our project!
"""

INFO_MENU_DESCRIPTION = """
For additional questions or to contact us please write to @minto_support and we'll get back to you as soon as we can.
"""

INFO_MENU_LINKS = """
:globe_with_meridians: [Website](https://minto.finance/)
:placard: [Telegram](https://t.me/btcmtofficial)
:fingers_crossed: [Twitter](https://twitter.com/BTCMTOfficial)
"""

INFO_MENU_INFORMATION = """
Founded: 15 декабря 2020 г.
Owner: @gniro#0069
Invite: https://discord.gg/minto
"""

FIRST_LVL = """
• Welcome! 
• Access to Discord
"""

FIFTH_LVL = """
• Change nickname 
• Add reactions 
• Custom emojis
"""

TENTH_LVL = """
• Special posting
"""

TWENTY_FIFTH_LVL = """
• Access to closed chat rooms 
• Access to voice chats
"""

FIFTY_FIFTH_LVL = """
• Token rewards 
• Custom roles and emojis
• Our adoration♥️
"""

CONTENT_ROLES = """
For participating in games and events you will get XP. The more points — the higher your level. With every level you will achieve a new role on this server, which will open up new possibilities. 
"""

INFORMATION_CHATS = """
#minto_updates — news about Minto
#minto_faq — product faq 
#minto_eco — environmental of Minto
#minto_ed — educational publications
"""

COMMUNITY_CHATS = """
#chat — for communication in general
#offtop — for roles and bots
#events-activities — announces and contests
#memes — fun
#minto_arena — for streams
#sum_up — sample discussions from other channels in Discord
#news — analysis of current news and events in the world of blockchain
"""

CONTENT_CHATS = """
Two chat categories: community and information.
"""

RULES_INFO = """
1. Be respectful to each other's opinions. NO insults, racism or harassment please. 
2. No one should ask you to send money to the account. Please contact our moderator immediately if this happens to you.
3. Do not post any NSFW content and limit the use of offensive language across all channels and nicknames.
4. We are free from all forms of advertising. Do not post referral links, discord invitations or any other invitations.
5. Impersonating members of the moderator team is a crime. Anyone caught doing this will be banned immediately.
"""