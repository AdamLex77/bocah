from PyroUbot import *

__MODULE__ = "efect"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇғᴇᴄᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}efect</code> [ᴇꜰᴇᴋ_ᴄᴏᴅᴇ - ʀᴇᴘʟʏ ᴛᴏ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ sᴜᴀʀᴀ ᴠᴏɪᴄᴇ ɴᴏᴛᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}listefect</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴀғᴛᴀʀ ᴇғᴇᴄᴛ

"""


@PY.UBOT("efect")
async def _(client, message):
    await convert_efek(client, message)


@PY.UBOT("listefect")
async def _(client, message):
    await list_cmd_efek(client, message)


