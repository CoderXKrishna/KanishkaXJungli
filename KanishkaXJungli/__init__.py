""" © Krishna """

from .config import *
from .database import *
from .core import *
from pyrogram import Client 
from Krishna.functions import * # make_list
import time, os, sys


print("""
     ╒══════════════════════╕
        Starting Your KanishkaXJungli 
     ╘══════════════════════╛
""")

#__version__ = "v0.5"
"""start time"""
start_time  = time.time()

try:
   OWNER_ID = int(OWNER_ID)
except ValueError:
   raise Exception("Your OWNER_ID variable is not a valid integer.")

"""Sudo Users"""
sudoser = []
if SUDO_USERS:
  sudoser = make_list(OWNER_ID, SUDO_USERS)
else:
  sudoser.append(OWNER_ID)

AUTO_REACT = []
if auto_re:
   AUTO_REACT = make_list(-1001790499664, auto_re)
else:
   AUTO_REACT.append(-1001790499664)

EMOJI_LIST = ['❤️', '✨', '🔥', '🥰', '💫', '💯', '🌟', '😁', '💥']
