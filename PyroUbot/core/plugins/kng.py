import asyncio
import os
import random
from io import BytesIO

import cv2
from PIL import Image
from pyrogram import *
from pyrogram.enums import ParseMode
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import DeleteHistory, GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName
from pyrogram.types import *

nomber_stiker = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 28 27 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67".split()

from PyroUbot import *
from PyroUbot import ubot


async def kang(client, message):
    await client.unblock_user("stickers")
    user = message.from_user
    replied = message.reply_to_message
    Tm = await eor(message, "ᴍᴇᴍᴘʀᴏꜱᴇꜱ ꜱᴛɪᴄᴋᴇʀꜱ...")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await Tm.edit("ꜱᴛɪᴋᴇʀ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ ɴᴀᴍᴀ!")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (
                replied.sticker.file_name.endswith(".tgs")
                or replied.sticker.file_name.endswith(".webm")
            ):
                resize = True
                ff_vid = True
        else:
            await Tm.edit("ꜰɪʟᴇ ᴛɪᴅᴀᴋ ᴅɪᴅᴜᴋᴜɴɢ")
            return
        media_ = await client.download_media(replied, file_name="PyroUbot/plugins/")
    else:
        await Tm.edit("ꜱɪʟᴀʜᴋᴀɴ ʀᴇᴘʟʏ ᴋᴇ ᴍᴇᴅɪᴀ ꜰᴏᴛᴏ/ɢɪꜰ/ꜱᴛɪᴄᴋᴇʀ!")
        return
    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (
            getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")
        ):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = user.username
        u_name = "@" + u_name if u_name else user.first_name or user.id
        packname = f"Sticker_u{user.id}_v{pack}"
        custom_packnick = f"{u_name} ᴘᴀᴄᴋ"
        packnick = f"{custom_packnick} Vol.{pack}"
        cmd = "/newpack"
        if resize:
            media_ = await resize_media(media_, is_video, ff_vid)
        if is_anim:
            packname += "_animated"
            packnick += " (Animated)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (Video)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await client.invoke(
                    GetStickerSet(
                        stickerset=InputStickerSetShortName(short_name=packname), hash=0
                    )
                )
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"a{user.id}_by_userge_{pack}"
                packnick = f"{custom_packnick} Vol.{pack}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (Animated){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (Video){pack}"
                await Tm.edit(
                    f"ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ {pack} ᴋᴀʀᴇɴᴀ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ꜱᴜᴅᴀʜ ᴘᴇɴᴜʜ"
                )
                continue
            break
        if exist is not False:
            try:
                await client.send_message("stickers", "/addsticker")
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            except Exception as e:
                return await Tm.edit(f"**ERROR:** `{e}`")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, client):
                pack += 1
                packname = f"_{user.id}_by_{user.username}_{pack}"
                packnick = f"{custom_packnick} vol.{pack}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (Animated)"
                if is_video:
                    packname += "_video"
                    packnick += " (Video)"
                await Tm.edit(
                    "ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ"
                    + str(pack)
                    + "ᴋᴀʀᴇɴᴀ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ꜱᴜᴅᴀʜ ᴘᴇɴᴜʜ"
                )
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, client) == "Invalid pack selected.":
                    await client.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await client.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await client.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await client.send_message(
                            "Stickers", f"<{packnick}>", parse_mode=ParseMode.MARKDOWN
                        )
                        await asyncio.sleep(2)
                    await client.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    await Tm.edit(
                        f"ꜱᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!\n         <a href=https://t.me/addstickers/{packname}>KLIK DISINI</a>\nᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴛɪᴄᴋᴇʀꜱ"
                    )
                    return
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await Tm.edit(
                    "ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ, ɢᴜɴᴀᴋᴀɴ @ꜱᴛɪᴄᴋᴇʀꜱ ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ ᴀɴᴅᴀ."
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/done")
        else:
            await Tm.edit("ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ")
            try:
                await client.send_message("Stickers", cmd)
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if (
                await get_response(message, client)
                == "Sorry, the file type is invalid."
            ):
                await Tm.edit(
                    "ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ, ɢᴜɴᴀᴋᴀɴ @ꜱᴛɪᴄᴋᴇʀꜱ ʙᴏᴛ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ ᴀɴᴅᴀ."
                )
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await client.send_message("Stickers", f"<{packnick}>")
                await asyncio.sleep(2)
            await client.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await Tm.edit(
            f"ꜱᴛɪᴄᴋᴇʀ ʙᴇʀʜᴀꜱɪʟ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ!\n         <a href=https://t.me/addstickers/{packname}>KLIK DISINI</a>\nᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ꜱᴛɪᴄᴋᴇʀꜱ"
        )
        if os.path.exists(str(media_)):
            os.remove(media_)
        user_info = "@stickers"
        await client.delete_messages(user_info, client.me.id)


async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text
