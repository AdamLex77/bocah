import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from PyroUbot import *



async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if not user_id:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ʙʟᴏᴋɪʀ.")
    if user_id == client.me.id:
        return await tex.edit("ᴏᴋ ᴅᴏɴᴇ.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>ʙᴇʀʜᴀꜱɪʟ ᴅɪʙᴇʙᴀꜱᴋᴀɴ</b> {umention}")


async def block_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if not user_id:
        return await tex.edit(f"ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜɴᴛᴜᴋ ᴅɪʙʟᴏᴋɪʀ.")
    if user_id == client.me.id:
        return await tex.edit("ᴏᴋ ᴅᴏɴᴇ.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>ʙᴇʀʜᴀꜱɪʟ ᴅɪʙʟᴏᴋɪʀ</b> {umention}")


async def setname(client: Client, message: Message):
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ.")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴍᴇɴᴊᴀᴅɪ</b> <code>{name}</code>"
            )
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ.")


async def set_bio(client: Client, message: Message):
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴍᴇɴᴊᴀᴅɪ</b> <code>{bio}</code>")
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ.")
