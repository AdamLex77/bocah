from PyroUbot import *

__MODULE__ = "profiles"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜰɪʟᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setbio</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴀɴᴅᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setname</ᴄᴏᴅᴇ> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴀɴᴅᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}block</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}unblock</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ
"""


@PY.UBOT("setbio")
async def _(client, message):
    await set_bio(client, message)


@PY.UBOT("setname")
async def _(client, message):
    await setname(client, message)


@PY.UBOT("block")
async def _(client, message):
    await block_user_func(client, message)


@PY.UBOT("unblock")
async def _(client, message):
    await unblock_user_func(client, message)






