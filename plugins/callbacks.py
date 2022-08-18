import os
from plugins.progress import progress_for_pyrogram, humanbytes

from Translation import Translation
from pyrogram import Client, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from plugins.downloader import youtube_dl_call_back

@Client.on_callback_query()
async def call_backs(bot:Client, update:CallbackQuery):
    if "|" in update.data:
        await update.message.edit(f"{update.data}")
        await youtube_dl_call_back(bot, update)