import asyncio
from gc import get_objects

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from PyroUbot import *


async def copy_bot_msg(client, message):
    if message.from_user.id not in ubot._get_my_id:
        return
    Tm = await message.reply("ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id)
            await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        await Tm.edit("ᴍᴀsᴜᴋᴋɪɴ ʟɪɴᴋ ʏᴀɴɢ ᴠᴀʟɪᴅ")


async def copy_ubot_msg(client, message):
    msg = message.reply_to_message or message
    Tm = await message.reply("ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ")
    link = get_arg(message)
    if not link:
        return await Tm.edit(
            f"<b><code>{message.text}</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]</b>"
        )
    if link.startswith(("https", "t.me")):
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            chat = int("-100" + str(link.split("/")[-2]))
        else:
            chat = str(link.split("/")[-2])
        try:
            get = await client.get_messages(chat, msg_id)
            await get.copy(message.chat.id, reply_to_message_id=msg.id)
            await Tm.delete()
        except Exception:
            try:
                text = f"get_msg {id(message)}"
                x = await client.get_inline_bot_results(bot.me.username, text)
                await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=msg.id,
                )
            except Exception:
                await client.send_message(
                    message.chat.id,
                    f"<b>🔒 ᴋᴏɴᴛᴇɴ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴀᴍʙɪʟ ʙᴇʀsɪꜰᴀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅd\n\n👉🏻 <a href=https://t.me/{bot.me.username}?start=copyMsg_{id(message)}>ᴋʟɪᴋ ᴅɪsɪɴɪ</a> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ</b>",
                    reply_to_message_id=msg.id,
                )
            await Tm.delete()
    else:
        await Tm.edit("ᴍᴀsᴜᴋᴋɪɴ ʟɪɴᴋ ʏᴀɴɢ ᴠᴀʟɪᴅ")


async def copy_inline_msg(client, inline_query):
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get message!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="🔐 ʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ 🔐",
                                    callback_data=f"copymsg_{int(inline_query.query.split()[1])}",
                                )
                            ],
                        ]
                    ),
                    input_message_content=InputTextMessageContent(
                        "<b>🔒 ᴋᴏɴᴛᴇɴ ʏᴀɴɢ ᴍᴀᴜ ᴅɪᴀᴍʙɪʟ ʙᴇʀsɪꜰᴀᴛ ʀᴇsᴛʀɪᴄᴛᴇᴅ\n\n✅ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ᴋᴏɴᴛᴇɴ ʀᴇsᴛʀɪᴄᴛᴇᴅ</b>"
                    ),
                )
            )
        ],
    )


async def copy_callback_msg(client, callback_query):
    try:
        q = int(callback_query.data.split("_", 1)[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        if not callback_query.from_user.id == m.from_user.id:
            return await callback_query.answer(
                f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
                True,
            )
        else:
            await m._client.unblock_user(bot.me.username)
            await callback_query.edit_message_text("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
            copy = await m._client.send_message(
                bot.me.username, f"/copy {m.text.split()[1]}"
            )
            await asyncio.sleep(1.5)
            await copy.delete()
            async for get in m._client.search_messages(bot.me.username, limit=1):
                await m._client.copy_message(m.chat.id, bot.me.username, get.id)
                await callback_query.edit_message_text(
                    "<b>✅ ᴄᴏᴘʏ ᴍᴇssᴀɢᴇ ʙᴇʀʜᴀsɪʟ ᴅɪʟᴀᴋᴜᴋᴀɴ"
                )
                await get.delete()
    except Exception as error:
        await callback_query.edit_message_text(f"<code>{error}</code>")
