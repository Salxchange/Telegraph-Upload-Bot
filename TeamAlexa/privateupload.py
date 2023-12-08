# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved Modified By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2023 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""

import os
import re
import asyncio
import traceback
from data import AlexaData
from pyrogram.errors import FloodWait
from telegraph import upload_file, Telegraph, exceptions
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


telegraph = Telegraph()
telegraph.create_account(short_name="The Team Alexa")


## UPLOAD PHOTOS

@Client.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(
        message=message, file_name="image/jetg"
    )
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "➜ ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ᴀʟsᴏ <a href=https://t.me/Team_Roku>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=AlexaData.ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⛅ 𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/Rokubotz"),
                InlineKeyboardButton("🌨️ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/Team_Roku")
            ],
            [
                InlineKeyboardButton("🌐 𝖶𝖾𝖻 𝖯𝗋𝖾𝗏𝗂𝖾𝗐 🌐", url=generated_link)
            ]
        ]
    )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n\n\n🔗 𝖫𝗂𝗇𝗄 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾𝖽 𝖡𝗒 ‣ <a href=https://t.me/RokuTelegraphUploaderRobot>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝗋 𝖡𝗈𝗍</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)
        
## UPLOAD VIDEOS

@Client.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(message=message, file_name="video/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "🌹 ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ᴀʟsᴏ  <a href=https://t.me/Team_Roku>LEARN HOW TO USE HERE!</a>",
            disable_web_page_preview=True, reply_markup=AlexaData.ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⛅ 𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/Rokubotz"),
                    InlineKeyboardButton("🌨️ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/Team_Roku")
                ],
                [
                    InlineKeyboardButton("🌐 𝖶𝖾𝖻 𝖯𝗋𝖾𝗏𝗂𝖾𝗐 🌐", url=generated_link)
                ]
            ]
        )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n\n\n🔗 𝖫𝗂𝗇𝗄 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾𝖽 𝖡𝗒 ‣ <a href=https://t.me/RokuTelegraphUploaderRobot>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝗋 𝖡𝗈𝗍</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)


        
## UPLOAD GIF

@Client.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply(AlexaData.UPLOAD_MSG, quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
    except:
        await msg.edit_text(
            "➜ ꜰɪʟᴇ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5ᴍʙ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɴᴏᴛʜᴇʀ ꜰɪʟᴇ ᴀʟsᴏ 👉 <a href=https://t.me/Team_Roku>❤️ ᴄᴏᴍᴇ ᴀɴᴅ ɪɴᴄʀᴇᴀsᴇ ʜᴇᴀʀᴛ ❤️</a>",
            reply_markup=AlexaData.INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        IN_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⛅ 𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/Rokubotz"),
                InlineKeyboardButton("🌨️ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/Team_Roku")
            ],
            [
                InlineKeyboardButton("🌐 𝖶𝖾𝖻 𝖯𝗋𝖾𝗏𝗂𝖾𝗐 🌐", url=generated_link)
            ]
        ]
        )
        await t.edit_text(
            f"🖇️ **ʟɪɴᴋ** - `{generated_link} `\n\n\n\n🔗 𝖫𝗂𝗇𝗄 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾𝖽 𝖡𝗒 ‣ <a href=https://t.me/RokuTelegraphUploaderRobot>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 𝖴𝗉𝗅𝗈𝖺𝖽𝖾𝗋 𝖡𝗈𝗍</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)
