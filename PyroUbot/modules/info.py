from PyroUbot import *

__MODULE__ = "info"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴꜰᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}info</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀs]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ᴘᴇɴɢɢᴜɴᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴇɴɢᴀɴ ᴅᴇsᴋʀɪᴘsɪ ʟᴇɴɢᴋᴀᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}cinfo</code> [ᴄʜᴀᴛ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴄʜᴀᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴅᴇɴɢᴀɴ ᴅᴇsᴋʀɪᴘsɪ ʟᴇɴɢᴋᴀᴘ
"""


@PY.UBOT("whois|info")
async def _(client, message):
    await info_cmd(client, message)


@PY.UBOT("cwhois|cinfo")
async def _(client, message):
    await cinfo_cmd(client, message)
