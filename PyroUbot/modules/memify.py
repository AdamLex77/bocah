from PyroUbot import *

__MODULE__ = "memify"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍɪꜰʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}mmf</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ʙᴀʟᴀs ᴋᴇ sᴛɪᴄᴋᴇʀ ᴀᴛᴀᴜ ꜰᴏᴛᴏ ᴀᴋᴀɴ ᴅɪ ᴜʙᴀʜ ᴍᴇɴᴊᴀᴅɪ sᴛɪᴄᴋᴇʀ ᴛᴇᴋs ᴍᴇᴍᴇ ʏᴀɴɢ ᴅɪ ᴛᴇɴᴛᴜᴋᴀɴ
"""


@PY.UBOT("mmf|memify")
async def _(client, message):
    await memify_cmd(client, message)
