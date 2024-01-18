from pyrogram.enums import ChatType

from PyroUbot import *


async def id_cmd(client, message):
    if len(message.command) < 2:
        chat_type = message.chat.type
        if chat_type == ChatType.PRIVATE:
            user_id = message.chat.id
            await message.reply_text(
                f"<b>ɪᴅ</b> <code>{user_id}</code>",
            )
        elif chat_type == ChatType.CHANNEL:
            await message.reply(
                f"<b>ɪᴅ {message.sender_chat.title} ᴀᴅᴀʟᴀʜ:</b> <code>{message.sender_chat.id}</code>",
            )
        elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            _id = ""
            _id += f"\n\n<b>ɪᴅ {message.from_user.first_name} {message.from_user.last_name or ''} ᴀᴅᴀʟᴀʜ:</b> <code>{message.from_user.id}</code>\n\n<b>ɪᴅ {message.chat.title} ᴀᴅᴀʟᴀʜ:</b> <code>{message.chat.id}</code>\n"
            if message.reply_to_message:
                _id += f"\n\n<b>ɪᴅ {message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name or ''} ᴀᴅᴀʟᴀʜ:</b> <code>{message.reply_to_message.from_user.id}</code>\n"
                file_info = get_file_id(message.reply_to_message)
                if file_info:
                    _id += f"\n<b>ɪᴅ {file_info.message_type} ᴀᴅᴀʟᴀʜ:</b> <code>{file_info.file_id}</code>\n"
            m = message.reply_to_message or message
            return await m.reply_text(_id)
    try:
        chat_id = message.text.split()[1]
        get = await client.get_chat(chat_id)
        name = f"{get.title}"
        if name == "None":
            get = await client.get_users(chat_id)
            name = f"{get.first_name} {get.last_name or ''}"
        msg = f"<b>ɪᴅ {name} ᴀᴅᴀʟᴀʜ:</b> <code>{get.id}</code>"
        return await message.reply(msg)
    except Exception as why:
        return await message.reply(why)
