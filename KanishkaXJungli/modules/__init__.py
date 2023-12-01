from KanishkaXJungli.config import *
from KanishkaXJungli.core.version import __version__
from KanishkaXJungli import sudoser, RiZoeL 
from Krishna import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "KanishkaXJungli"
pic = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/aa599d1a0e8afd6202c89.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "KanishkaXJungli - by Krishna"

try:
   sah = Krishna.get_users(1195997736)
   owner_mention = sah.mention
except:
   owner_mention = f"[{1195997736}](tg://user?id={1195997736})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **Master:** {owner_mention}
➠ **Python Version:** `{platform.python_version()}`
➠ **KanishkaXJungli Version:** `{__version__}`
➠ **Pyrogram Version:** `{pyro_vr}`
➠ **pyKrishna Version:** `{pip_vr}`
➠ **Channel:** @Krishna
━───────╮•╭───────━
➠ **Source Code:** [•Repo•](https://github.com/CoderXKrishna/KanishkaXJungli)
     """

handler = HNDLR
Owner = int(1195997736)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from KanishkaXJungli.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
