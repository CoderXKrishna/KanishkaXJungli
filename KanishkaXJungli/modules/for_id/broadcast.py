# Krishna X - Telegram Projects
# (c) 2022 - 2023 Krishna


import asyncio
from .. import Owner, handler
from KrishnaX import Devs
from KrishnaX.functions import broadcast_
from pyrogram import Client , filters
from pyrogram.types import Message


@Client.on_message(filters.user(Devs) & filters.command(["broadcast", "gcast"], prefixes=handler))
@Client.on_message(filters.user(Owner) & filters.command(["broadcast", "gcast"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["broadcast", "gcast"], prefixes=handler))
async def broadcast(KanishkaXJungli: Client, message: Message):
    await broadcast_(KanishkaXJungli, message)
