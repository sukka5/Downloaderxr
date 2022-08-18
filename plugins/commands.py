from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.private & filters.command(['start']))
async def start(c:Client, m:Message):
    await m.reply_text(f"Welcome {m.from_user.mention} Boy!", quote=True)

