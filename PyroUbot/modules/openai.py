from PyroUbot import *

__MODULE__ = "openai"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴘᴇɴᴀɪ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}ai</code> ᴏʀ <code>{PREFIX[0]}ask</code>  [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴊᴜᴋᴀɴ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴇ ᴄʜᴀᴛɢᴘᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}dalle</code> ᴏʀ <code>{PREFIX[0]}photo</code> [ǫᴜᴇʀʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ᴘʜᴏᴛᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}stt</code> [ʀᴇᴘʟʏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘᴇsᴀɴ sᴜᴀʀᴀ ᴋᴇ ᴛᴇxᴛ
"""


@PY.UBOT("ai|ask")
async def _(client, message):
    await ai_cmd(client, message)


@PY.UBOT("dalle|photo")
async def _(client, message):
    await dalle_cmd(client, message)


@PY.UBOT("stt")
async def _(client, message):
    await stt_cmd(client, message)
