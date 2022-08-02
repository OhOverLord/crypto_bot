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
<#981116499152502825> — news about Minto
<#981116559743418368>  — product faq 
<#981116609160691712> — environmental of Minto
<#981116667683819520> — educational publications
"""

COMMUNITY_CHATS = """
<#981116965974315019> — for communication in general
<#981117018638016572> — for roles and bots
<#981117055082315777> — announces and contests
<#981117088095686686> — fun
`#minto_arena` — for streams
<#981118133202993152> — sample discussions from other channels in Discord#news — analysis of current news and events in the world of blockchain
<#981117432410279966> — analysis of current news and events in the world of blockchain
"""

CONTENT_CHATS = """
Two chat categories: community and information.
"""

RULES_INFO = """
``Rule 1`` **No disrespect**
Be respectful to each other's opinions. NO insults, racism or harassment please. 

``Rule 2`` **Scam**
No one should ask you to send money to the account. Please contact our moderator immediately if this happens to you. 

``Rule 3`` **No Inappropriate content**
Do not post any NSFW content and limit the use of offensive language across all channels and nicknames.

``Rule 4`` **No advertising**
We are free from all forms of advertising. Do not post referral links, discord invitations or any other invitations.

``Rule 5`` **Impersonating moderator team**
Impersonating members of the moderator team is a crime. Anyone caught doing this will be banned immediately.
"""

FAQ = {
  1: ["When will BTCMT be listed on CEX?", "FAQ 1", "When will BTCMT be listed on CEX?\nWe are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet."],
  2: ["When will BTCMT be listed on CEX?", "FAQ 1", "When will BTCMT be listed on CEX?\nWe are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet."],
  3: ["When will BTCMT be listed on CEX?", "FAQ 1", "When will BTCMT be listed on CEX?\nWe are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet."],
  4: ["When will BTCMT be listed on CEX?", "FAQ 1", "When will BTCMT be listed on CEX?\nWe are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet."],
  5: ["When will BTCMT be listed on CEX?", "FAQ 1", "When will BTCMT be listed on CEX?\nWe are currently working on listing. We plan to list before 3-4Q 2022, but we don't have an exact date yet."],
}