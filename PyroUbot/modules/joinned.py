from PyroUbot import *

__MODULE__ = "joinleave"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴʟᴇᴀᴠᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}kickme</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}join</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴋᴇ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallgc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leaveallch</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}leave</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ
"""


@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
async def _(client, message):
    await leave(client, message)


@PY.UBOT("join")
async def _(client, message):
    await join(client, message)


@PY.UBOT("leaveallgc")
async def _(client, message):
    await kickmeall(client, message)


@PY.UBOT("leaveallch")
async def _(client, message):
    await kickmeallch(client, message)


