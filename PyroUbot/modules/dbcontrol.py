from PyroUbot import *


@PY.BOT("prem")
async def _(client, message):
    await prem_user(client, message)


@PY.BOT("unprem", FILTERS.OWNER)
async def _(client, message):
    await unprem_user(client, message)


@PY.BOT("getprem", FILTERS.OWNER)
async def _(cliebt, message):
    await get_prem_user(client, message)


@PY.BOT("seles", FILTERS.OWNER)
async def _(client, message):
    await seles_user(client, message)


@PY.BOT("unseles", FILTERS.OWNER)
async def _(client, message):
    await unseles_user(client, message)


@PY.BOT("getseles", FILTERS.OWNER)
async def _(client, message):
    await get_seles_user(client, message)


@PY.BOT("time", FILTERS.OWNER)
async def _(client, message):
    await expired_add(client, message)


@PY.BOT("cek", FILTERS.OWNER)
async def _(client, message):
    await expired_cek(client, message)


@PY.BOT("untime", FILTERS.OWNER)
async def _(client, message):
    await un_expired(client, message)


@PY.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)


@PY.CALLBACK("gitpull")
async def _(client, callback_query):
    await cb_gitpull(client, callback_query)
