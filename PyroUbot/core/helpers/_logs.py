from pyrogram.enums import ChatType

from PyroUbot import *



from pyrogram.enums import ChatType

from PyroUbot import *


async def create_logs(client):
    logs = await client.create_channel(f"Logs Ubot: {bot.me.username}")
    await client.set_chat_photo(
        logs.id,
        video="storage/logs.mp4",
    )
    return logs.id


async def forward_logs(client, message):
    logs = await get_vars(client.me.id, "ID_LOGS")
    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if logs and on_logs:
        if message.chat.type == ChatType.PRIVATE:
            type = "ᴘʀɪᴠᴀᴛᴇ"
            from_user = message.chat
            id_link = f"tg://openmessage?user_id={from_user.id}&message_id={message.id}"
        elif message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            type = "ɢʀᴏᴜᴘ"
            from_user = message.from_user
            id_link = message.link
        rpk = f"{from_user.first_name} {from_user.last_name or ''}"
        link = f"[ᴋʟɪᴋ ᴅɪsɪɴɪ]({id_link})"
        psn = f"{message.text}"
        await client.send_message(
            int(logs),
            f"""
<b>📩 ᴀᴅᴀ ᴘᴇsᴀɴ ᴍᴀsᴜᴋ</b>
    <b>•> ᴛɪᴘᴇ :</b> {type}
    <b>•> ʟɪɴᴋ :</b> {link}
    
<b>⤵️ ᴘᴇsᴀɴ ᴛᴇʀᴜsᴀɴ 
    <b>•> ᴅᴀʀɪ :</b> {rpk}
    <b>•> ᴘᴇsᴀɴ : {psn}</b>
""",
        )
