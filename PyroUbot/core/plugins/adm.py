import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from PyroUbot import *

BANNED_USERS = filters.user()


async def admin_bannen(client, message):
    if message.command[0] == "kick":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴛᴜ.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg = f"<b>👤 ᴅɪᴛᴇɴᴅᴀɴɢ:</b> {mention}\n<b>👑 ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
        if reason:
            msg += f"\n<b>💬 ᴀʟᴀsᴀɴ:</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg)
            await asyncio.sleep(1)
            await message.chat.unban_member(user_id)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "ban":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg = (
            f"<b>👤 ᴅɪʙᴀɴɴᴇᴅ:</b> {mention}\n<b>👑 ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
        )
        if reason:
            msg += f"\n<b>💬 ᴀʟᴀsᴀɴ:</b> {reason}"
        try:
            await message.chat.ban_member(user_id)
            await message.reply(msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "mute":
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        if user_id == (await client.get_me()).id:
            return await message.reply_text(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ."
            )
        if user_id == OWNER_ID:
            return await message.reply_text("ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
        if user_id in (await list_admins(message)):
            return await message.reply_text(
                "sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ."
            )
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        msg = f"<b>👤 ᴍᴇᴍʙɪsᴜᴋᴀɴ:</b> {mention}\n<b>👑 ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
        if reason:
            msg += f"\n<b>💬 ᴀʟᴀsᴀɴ:</b> {reason}"
        try:
            await message.chat.restrict_member(user_id, ChatPermissions())
            await message.reply(msg)
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unmute":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<b>✅ {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴄʜᴀᴛ ʟᴀɢɪ</b>")
        except Exception as error:
            await message.reply(error)
    elif message.command[0] == "unban":
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
        try:
            mention = (await client.get_users(user_id)).mention
        except Exception as error:
            await message.reply(error)
        try:
            await message.chat.unban_member(user_id)
            await message.reply(f"<b>✅ {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴊᴏɪɴ ʟᴀɢɪ</b>")
        except Exception as error:
            await message.reply(error)


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "<code>gban</code> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit("ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴜꜱᴇʀ ᴛᴇʀꜱᴇʙᴜᴛ.")
        return
    iso = 0
    gagal = 0
    prik = user.id
    prok = await get_seles()
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            
            if prik in DEVS:
                return await Tm.edit(
                    "ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ɢʙᴀɴ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ ꜱᴀʏᴀ."
                )
            elif prik in prok:
                return await Tm.edit(
                    "ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ɢʙᴀɴ ᴅɪᴀ, ᴋᴀʀɴᴀ ᴅɪᴀ ᴀᴅᴀʟᴀʜ ᴀᴅᴍɪɴ ᴜꜱᴇʀʙᴏᴛ ᴀɴᴅᴀ."
                )
            elif udah:
                return await Tm.edit(
                    "ᴘᴇɴɢɢᴜɴᴀ ɪɴɪ ꜱᴜᴅᴀʜ ᴅɪ ɢʙᴀɴ."
                )
            elif prik not in prok and prik not in DEVS:
                try:
                    await add_banned_user(gua, prik)
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)
    return await Tm.edit(
        f"""
<b>ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ</b>

<b>ʙᴇʀʜᴀꜱɪʟ ʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜꜱᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )

async def cung_ban(client, message):
    user_id = await extract_user(message)
    if message.from_user.id != client.me.id:
        Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ.....</code>")
    else:
        Tm = await message.reply("<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "<code>ungban</code> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit("<b>ᴛɪᴅᴀᴋ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴜꜱᴇʀ ᴛᴇʀꜱᴇʙᴜᴛ.</b>")
        return
    iso = 0
    gagal = 0
    prik = user.id
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            if prik in BANNED_USERS:
                BANNED_USERS.remove(prik) 
            try:
                await remove_banned_user(gua, prik)
                await client.unban_chat_member(chat, prik)
                iso = iso + 1
                await asyncio.sleep(0.1)
            except BaseException:
                gagal = gagal + 1
                await asyncio.sleep(0.1)

    return await Tm.edit(
        f"""
<b>ɢʟᴏʙᴀʟ ᴜɴʙᴀɴɴᴇᴅ</b>

<b>ʙᴇʀʜᴀꜱɪʟ ᴜɴʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ᴜɴʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜꜱᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )


async def gbanlist(client, message):
    gua = client.me.id
    total = await get_banned_count(gua)
    if total == 0:
        return await message.reply("<b>ʙᴇʟᴜᴍ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪɢʙᴀɴ.</b>")
    nyet = await message.reply("<b>ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    msg = "ᴛᴏᴛᴀʟ ɢʙᴀɴɴᴇᴅ:\n\n"
    tl = 0
    org = await get_banned_users(gua)
    for i in org:
        tl += 1
        try:
            user = await client.get_users(i)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{tl}• {user}\n"
        except Exception:
            msg += f"{tl}• {i}\n"
            continue
    if tl == 0:
        return await nyet.edit("<b>ʙᴇʟᴜᴍ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪɢʙᴀɴ.</b>")
    else:
        return await nyet.edit(msg)
