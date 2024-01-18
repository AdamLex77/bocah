from PyroUbot import *


@PY.CALLBACK("grts")
async def _(client, callback_query):
    await need_gratis(client, callback_query)


@PY.CALLBACK("gratis")
async def _(client, callback_query):
    await bikin_gratis(client, callback_query)


@PY.CALLBACK("pler")
async def _(client, callback_query):
    await ohaja(client, callback_query)


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("memek")
async def _(client, callback_query):
    await bikin_memek(client, callback_query)


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("memek")
async def _(client, callback_query):
    await bikin_memek(client, callback_query)


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    await payment_userbot(client, callback_query)


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)


@PY.CALLBACK("cek_ubot")
@PY.BOT("getubot", FILTERS.OWNER)
async def _(client, message):
    await cek_ubot(client, message)


@PY.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def _(client, callback_query):
    await tools_userbot(client, callback_query)


@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    await cek_userbot_expired(client, callback_query)


@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)

    
@PY.CALLBACK("^(prev_ub|next_ub)")
async def _(client, callback_query):
    await next_prev_ubot(client, callback_query)
