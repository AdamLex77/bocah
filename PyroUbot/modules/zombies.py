from PyroUbot import *

__MODULE__ = "zombies"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴢᴏᴍʙɪᴇs 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}zombies</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇʟᴜᴀʀᴋᴀɴ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜs ᴅɪɢʀᴜᴘ ᴀɴᴅᴀ.
"""


@PY.UBOT("zombies")
async def _(client, message):
    await zombies_cmd(client, message)
