from PyroUbot import *

__MODULE__ = "carbon"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴏɴᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}carbon</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇᴋꜱ ᴄᴀʀʙᴏɴᴀʀᴀ
"""


@PY.UBOT("carbon")
async def _(client, message):
    await carbon_func(client, message)
