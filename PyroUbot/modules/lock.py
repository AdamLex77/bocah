from PyroUbot import *


__MODULE__ = "locks"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏᴄᴋꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}lock</code> [ᴛʏᴘᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴄɪ ɪᴢɪɴ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}unlock</code> [ᴛʏᴘᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ɪᴢɪɴ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}locks</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɪᴢɪɴ ꜱᴀᴀᴛ ɪɴɪ.

  <b>• ᴛʏᴘᴇ : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`
"""


@PY.UBOT("lock|unlock")
async def _(client, message):
    await locks_func(client, message)


@PY.UBOT("locks")
async def _(client, message):
    await locktypes(client, message)
