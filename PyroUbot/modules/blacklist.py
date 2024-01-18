from PyroUbot import *

__MODULE__ = "blacklist"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʟɪsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}addbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴀsᴜᴋᴋᴀɴ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʜɪᴛᴀᴍ sᴜᴘᴀʏᴀ ɢᴄᴀsᴛ ᴋᴀʟɪᴀɴ ᴛɪᴅᴀᴋ ᴍᴀsᴜᴋ ᴋᴇ ɢʀᴏᴜᴘ [ʟᴀᴋᴜᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ, sᴇʟᴀɪɴ ᴅɪ ɢʀᴏᴜᴘ ʙᴏᴛ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ʀᴇsᴘᴏɴ]

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}unbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ɢʀᴏᴜᴘ ᴅᴀʀɪ ᴅᴀꜰᴛᴀʀ ʜɪᴛᴀᴍ ᴀɢᴀʀ ɢᴄᴀsᴛ ʙɪsᴀ ᴍᴀsᴜᴋ ᴋᴇ ɢʀᴏᴜᴘ  [ʟᴀᴋᴜᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ, sᴇʟᴀɪɴ ᴅɪ ɢʀᴏᴜᴘ ʙᴏᴛ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ʀᴇsᴘᴏɴ]
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}rallbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ʙʟᴀᴄᴋʟɪsᴛ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}listbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪsᴛ ɢʀᴏᴜᴘ
"""


@PY.UBOT("addbl", FILTERS.ME_GROUP)
async def _(client, message):
    await add_blaclist(client, message)


@PY.UBOT("unbl", FILTERS.ME_GROUP)
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("rallbl")
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("listbl")
async def _(client, message):
    await get_blacklist(client, message)
