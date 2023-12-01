# Krishna X - Telegram Projects
# (c) 2022 - 2023 Krishna
# Don't Kang Bitch -!



import os
import sys
from random import choice
from .. import Owner, handler
from pyrogram import Client, filters
from pyrogram.types import Message


Media = "resources/Profile.jpg"

@Client.on_message(filters.user(Owner) & filters.command(["setpic"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setpic"], prefixes=handler))
async def setpic(KanishkaXJungli: Client, e: Message):
     replied = e.reply_to_message
     if (replied and replied.media and (replied.photo or (replied.document and "image" in replied.document.mime_type))):
            await KanishkaXJungli.download_media(message=replied, file_name=Media)
            await KanishkaXJungli.set_profile_photo(photo=Media)
            await e.reply_text(f"**Changed profile picture successfully** ✅")
            if os.path.exists(Media):
               os.remove(Media)
     else:
         await e.reply_text("Reply To any Photo To Change Profile pic")
      
etc_bio = "ᴜsᴇʀ ᴏғ ʀɪᴢᴏᴇʟ x"

@Client.on_message(filters.user(Owner) & filters.command(["setname"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setname"], prefixes=handler))
async def setname(KanishkaXJungli: Client, e: Message): 
     Krishna = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
     if e.reply_to_message:
        name = e.reply_to_message.text.markdown
     elif Krishna:
        name = str(Krishna[0])
     else:
        await e.reply_text(f"Wrong usage! \n syntax: {handler}setname (name)")
        return
     try:
        await KanishkaXJungli.update_profile(first_name=name, bio=etc_bio)
        await e.reply_text(f"**Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
     except Exception as ex:
        await e.reply_text(f"**Error !!** \n\n {ex}")
        print(ex)
     
@Client.on_message(filters.user(Owner) & filters.command(["setbio"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["setbio"], prefixes=handler))
async def setbio(KanishkaXJungli: Client, e: Message):
      Krishna = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
      if e.reply_to_message:
        xd = e.reply_to_message.text.markdown
      elif Krishna:
        xd = str(Krishna[0])
      else:
        await e.reply_text(f"Wrong usage! \n syntax: {handler}setbio (bio)")
        return
      ok = await KanishkaXJungli.get_me()
      nam = ok.first_name
      nam2 = ok.last_name
      try:
         await KanishkaXJungli.update_profile(first_name=nam, last_name=nam2, bio=xd)
         await e.reply_text(f"**Profile Bio Changed Successfully !** \n\n **New Bio**: {xd}")
      except Exception as ex:
         await e.reply_text(f"**Error !!** \n\n {ex}")
         print(ex)
      
