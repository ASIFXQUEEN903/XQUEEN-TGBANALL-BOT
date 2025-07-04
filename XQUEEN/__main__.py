import os
import logging
from config import BOT_USERNAME
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)

@app.on_message(
    filters.command("start")
    & filters.private
)
async def start_command(client, message: Message):
    user = message.from_user
    await message.reply_photo(
        photo=f"https://files.catbox.moe/a0l6kq.jpg",
        caption=f"**✦ » ʜᴇʏ {user.mention}**\n**✦ » ᴛʜɪs ɪs ᴀ sɪᴍᴘʟᴇ ʙᴀɴ ᴀʟʟ ʙᴏᴛ ᴡʜɪᴄʜ ɪs ʙᴀsᴇᴅ ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙʀᴀʀʏ.**\n\n**✦ » 𝗝𝗢 𝗞𝗔𝗥𝗡𝗔 𝗛𝗔𝗜 𝗞𝗔𝗥𝗢 𝗕𝗔𝗦 𝗤𝗨𝗘𝗘𝗡 𝗞𝗢 𝗚𝗨𝗦𝗛𝗔 𝗠𝗔𝗧 𝗗𝗜𝗟𝗔𝗡𝗔 𝗢𝗥𝗥 𝗬𝗘 𝗠𝗔𝗧 𝗕𝗢𝗟𝗡𝗔 𝗞𝗜 𝗧𝗨𝗠 𝗦𝗥𝗜𝗙 𝗔𝗗𝗠𝗜𝗡 𝗞𝗘 𝗦𝗔𝗔𝗧𝗛 𝗛𝗜 𝗕𝗔𝗔𝗧 𝗞𝗔𝗥𝗧𝗘 𝗛𝗢.**\n\n**✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ ɢɪᴠᴇ ᴍᴇ ғᴜʟʟ ᴘᴏᴡᴇʀs ᴀɴᴅ ᴛʏᴘᴇ `/queenxxxxxx full comnd ke liye 👉@ASHlF903` ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.**\n\n**✦ » 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ »  <a href=t.me/ARAME9>❛꯭𓂀⎯⃟⃝ 𝐗⃪꯭𝐐⃪꯭𝐔⃪꯭𝐄⃪꯭𝐄⃪꯭𝐍 ⎯𓂀❜</a>**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜️ Aᴅᴅ ᴍᴇ Bᴀʙʏ ⚜️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton("🔸 ❍ᴡɴᴇʀ🔸", url="http://t.me/ASHLF903"),
                    InlineKeyboardButton("▫️ 𝗨ᴘᴅᴀᴛᴇs ▫️", url="http://t.me/BOT_HEART")
                ]                
            ]
        )
    )

@app.on_message(
filters.command("queenragigala") 
& filters.group
)
async def banall_command(client, message: Message):
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id = message.chat.id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kicked {} from {}".format(i.user.id, e))           
    print("process completed")
    

# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
