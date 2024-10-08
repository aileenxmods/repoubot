from telegraph import Telegraph, exceptions, upload_file

from userbot import *


async def tg_cmd(client, message):
    XD = await message.reply("<code>sedang memproses . . .</code>")
    if not message.reply_to_message:
        return await XD.edit(
            "<b>mohon balas ke pesan, untuk mendapatkan link dari telegraph.</b>"
        )
    telegraph = Telegraph()
    if message.reply_to_message.media:
        m_d = await dl_pic(client, message.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        U_done = f"<b>berhasil diupload ke</b> <a href='https://telegra.ph/{media_url[0]}'>telegraph</a>"
        await XD.edit(U_done)
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        wow_graph = f"<b>berhasil diupload ke</b> <a href='https://telegra.ph/{response['path']}'>telegraph</a>"
        await XD.edit(wow_graph)
