from userbot import *


@CB.CALLBACK("^support")
async def _(client, callback_query):
    await support_callback(client, callback_query)


@CB.CALLBACK("^jawab_pesan")
async def _(client, callback_query):
    await jawab_pesan_callback(client, callback_query)


@CB.CALLBACK("^profil")
async def _(client, callback_query):
    await profil_callback(client, callback_query)


@CB.CALLBACK("^batal")
async def _(client, callback_query):
    await batal_callback(client, callback_query)
