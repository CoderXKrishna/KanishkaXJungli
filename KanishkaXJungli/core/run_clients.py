
# Versions

from .clients import *
from KanishkaXJungli.config import *

from .version import __version__
from KrishnaX import __version__ as Krishnax_vr
from pyrogram import __version__ as pyro_vr
import platform

from KrishnaX.functions import start_KanishkaXJungli
from pyrogram import idle

def Run_KanishkaXJungli():
    if CLIENT:
       if ":" in CLIENT:
         start_KanishkaXJungli(Krishna, "token")
       else:
         start_KanishkaXJungli(Krishna, "session")

    if CLIENT2:
       if ":" in CLIENT2:
         start_KanishkaXJungli(Krishna2, "token")
       else:
         start_KanishkaXJungli(Krishna2, "session")
         
    if CLIENT3:
       if ":" in CLIENT3:
         start_KanishkaXJungli(Krishna3, "token")
       else:
         start_KanishkaXJungli(Krishna3, "session")
         
    if CLIENT4:
       if ":" in CLIENT4:
         start_KanishkaXJungli(Krishna4, "token")
       else:
         start_KanishkaXJungli(Krishna4, "session")
         
    if CLIENT5:
       if ":" in CLIENT5:
         start_KanishkaXJungli(Krishna5, "token")
       else:
         start_KanishkaXJungli(Krishna5, "session")
         
    if CLIENT6:
       if ":" in CLIENT6:
         start_KanishkaXJungli(Krishna6, "token")
       else:
         start_KanishkaXJungli(Krishna6, "session")
         
    if CLIENT7:
       if ":" in CLIENT7:
         start_KanishkaXJungli(Krishna7, "token")
       else:
         start_KanishkaXJungli(Krishna7, "session")
         
    if CLIENT8:
       if ":" in CLIENT8:
         start_KanishkaXJungli(Krishna8, "token")
       else:
         start_KanishkaXJungli(Krishna8, "session")
         
    if CLIENT9:
       if ":" in CLIENT9:
         start_KanishkaXJungli(Krishna9, "token")
       else:
         start_KanishkaXJungli(Krishna9, "session")

    if CLIENT10:
       if ":" in CLIENT10:
         start_KanishkaXJungli(Krishna10, "token")
       else:
         start_KanishkaXJungli(Krishna10, "session")
         
    if CLIENT11:
       if ":" in CLIENT11:
         start_KanishkaXJungli(Krishna11, "token")
       else:
         start_KanishkaXJungli(Krishna11, "session")
         
    if CLIENT12:
       if ":" in CLIENT12:
         start_KanishkaXJungli(Krishna12, "token")
       else:
         start_KanishkaXJungli(Krishna12, "session")
         
    if CLIENT13:
       if ":" in CLIENT13:
         start_KanishkaXJungli(Krishna13, "token")
       else:
         start_KanishkaXJungli(Krishna13, "session")
         
    if CLIENT14:
       if ":" in CLIENT14:
         start_KanishkaXJungli(Krishna14, "token")
       else:
         start_KanishkaXJungli(Krishna14, "session")
         
    if CLIENT15:
       if ":" in CLIENT15:
         start_KanishkaXJungli(Krishna15, "token")
       else:
         start_KanishkaXJungli(Krishna15, "session")
         
    if CLIENT16:
       if ":" in CLIENT16:
         start_KanishkaXJungli(Krishna16, "token")
       else:
         start_KanishkaXJungli(Krishna16, "session")
         
    if CLIENT17:
       if ":" in CLIENT17:
         start_KanishkaXJungli(Krishna17, "token")
       else:
         start_KanishkaXJungli(Krishna17, "session")
         
    if CLIENT18:
       if ":" in CLIENT18:
         start_KanishkaXJungli(Krishna18, "token")
       else:
         start_KanishkaXJungli(Krishna18, "session")
         
    if CLIENT19:
       if ":" in CLIENT19:
         start_KanishkaXJungli(Krishna19, "token")
       else:
         start_KanishkaXJungli(Krishna19, "session")

    if CLIENT20:
       if ":" in CLIENT20:
         start_KanishkaXJungli(Krishna20, "token")
       else:
         start_KanishkaXJungli(Krishna20, "session")
    
    print(f"KanishkaXJungli - [INFO]: Python Version - {platform.python_version()}")
    print(f"KanishkaXJungli - [INFO]: KanishkaXJungli Version - {__version__}")
    print(f"KanishkaXJungli - [INFO]: pyKrishnaX Version - {Krishnax_vr}")
    print(f"KanishkaXJungli - [INFO]: Pyrogram Version - {pyro_vr}")
    print(""" \n\n
     ╒═══════════════════════════╕
      Your KanishkaXJungli has been Deployed!!
      Visit @Mrs_And_Mr_Hitler for updates!
     ╘═══════════════════════════╛
    """)
    idle()
