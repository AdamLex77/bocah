from PyroUbot import *

__MODULE__ = "translate"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʀᴀɴsʟᴀᴛᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tr</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇʀᴊᴇᴍᴀʜᴋᴀɴ ᴛᴇxᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tts</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇᴄᴛ ᴍᴇɴᴊᴀᴅɪ ᴍᴇɴᴊᴀᴅɪ ᴘᴇsᴀɴ sᴜᴀʀᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setlang</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ʙᴀʜᴀsᴀ ᴛʀᴀɴsʟᴀᴛᴇ
"""


@PY.UBOT("tts")
async def _(client, message):
    await tts_cmd(client, message)


@PY.UBOT("tr|tl")
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("setlang")
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
