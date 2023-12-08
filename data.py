# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved Modified, Enhanced And Database Added By ©️ Team Alexa
""""
Alexa is a Telegram Audio and video streaming bot 
Copyright (c) 2022 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want.
"""
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class AlexaData(object):
    STATS = "➜ **ᴛᴏᴛᴀʟ ᴜsᴇʀs** : {}\n➜ **ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs** : {}\n\n**──────────────**\n➜ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{}`\n**──────────────**"
    BCAST_USG = "**💐 ᴜꜱᴀɢᴇ**:\n`/broadcast` [ᴍᴇꜱꜱᴀɢᴇ] ᴏʀ ʀᴇᴘʟᴀʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ɪɴᴛᴏ ᴄʜᴀᴛs ᴀɴᴅ ᴜsᴇʀs"
    BCAST_DN = "➜ **ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {} chat(s) and {} user(s).**"
    REPLAY_MSG = "➜ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɪɴᴄʟᴜᴅᴇ ᴛᴇxᴛ ᴀꜰᴛᴇʀ ᴛʜᴇ /upload ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ."
    UPLOAD_MSG = "⬆️ ʏᴏᴜʀ ꜰɪʟᴇ ɪs ʙᴇᴇɴ ᴜᴘʟᴏᴀᴅɪɴɢ..."
    UPLOAD_MSG2 = "➜ ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ / ᴛᴇxᴛ  / ᴀɴɪᴍᴀᴛɪᴏɴ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ . . ."
    HOLD_MSG = "⏳• ʜᴏʟᴅ ᴏɴ ɪ'ᴍ ᴜᴘʟᴏᴀᴅɪɴɢ . . ."
    ERROR_MSG = "➜ ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜰɪʟᴇ ꜰᴏʀᴍᴀᴛ ᴏʀ ꜰɪʟᴇ sɪᴢᴇ, ɪᴛ ᴍᴜsᴛ ʙᴇ ʟᴇss ᴛʜᴀɴ 5 ᴍʙ . . ."
    FILE_ERROR = "😢 sᴏʀʀʏ, ᴛʜᴇ ꜰɪʟᴇ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ !"
    INLINE_SELECT = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤩 ᴊᴏɪɴ ᴜs", url="https://t.me/Rokubotz"),
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs 🐲", url="https://t.me/Rokubotz")
            ],
            [
                InlineKeyboardButton("", url="https://youtube/jankarikiduniya")
            ]
        ]
    )
    ERROR_BUTTON = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌋 ʀᴇᴘᴏʀᴛ ᴇʀʀᴏʀ", url="https://t.me/Team_Roku"),
                InlineKeyboardButton("ᴊᴏɪɴ 🌋", url="https://t.me/Rokubotz")
            ]
        ]
    )    
    H_BUTTON = [
         [
              InlineKeyboardButton(text="๏ ᴀʙᴏᴜᴛ ๏", callback_data="ABOUT_CMD"),
         ],
         [
              InlineKeyboardButton(text="๏ ᴄᴍᴅs ๏", callback_data="CMDS_CMD"),
              InlineKeyboardButton(text="๏ ʀᴏᴋᴜʙᴏᴛᴢ ๏", callback_data="TEAM_CMD"),
         ],
    ]

    HELP_BACK = [
            [     
                  InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data="HELP_BACK"),
            ],
    ]

    HELP_STRING = f"""
**ɪᴛ ɪs ᴀ ʀᴏᴋᴜʙᴏᴛᴢ ᴘʀᴏᴊᴇᴄᴛ ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ʜᴇʟᴘ ᴀʟʟ ᴄᴍᴅ ᴀɴᴅ ᴅᴇᴛᴀɪʟs ᴀʀᴇ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ!**
**──────────────**
<b> @Rokubotz </b>
"""

    ABOUT_STRING = f"""
➛ ɪɴᴛʀᴏᴅᴜᴄɪɴɢ ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴘʀᴏᴊᴇᴄᴛ ꜰʀᴏᴍ ʀᴏᴋᴜʙᴏᴛᴢ - ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜᴘʟᴏᴀᴅ ʙᴏᴛ! ᴛʜɪs ɪɴᴄʀᴇᴅɪʙʟᴇ ʙᴏᴛ ᴄᴀɴ ᴇꜰꜰᴏʀᴛʟᴇssʟʏ ᴜᴘʟᴏᴀᴅ ᴘɪᴄᴛᴜʀᴇs, ᴠɪᴅᴇᴏs, ᴀɴɪᴍᴀᴛɪᴏɴs, ᴀɴᴅ ᴛᴇxᴛs ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ ᴀɴᴅ ɪɴsᴛᴀɴᴛʟʏ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ꜰɪʟᴇ. ᴊᴜsᴛ ʀᴇᴍᴇᴍʙᴇʀ, ꜰᴏʀ ᴛʜᴇ ʙᴇsᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ, ᴇɴsᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ꜰɪʟᴇ ɪs ᴜɴᴅᴇʀ 5ᴍʙ ɪɴ sɪᴢᴇ.
**───────────────**
<b> @Rokubotz </b>
"""

    CMDS_STRING = f"""
<u>**ʜᴇʀᴇ ɪs sᴏᴍᴇ ʙᴀsɪᴄ ᴄᴍᴅs**</u>
**➛ `/stats` ᴄᴏʟʟᴇᴄᴛ ᴄʜᴀᴛs ᴀɴᴅ ᴜsᴇʀ ᴡʜᴇʀᴇ ʙᴏᴛ ɪs ᴡᴏʀᴋɪɴɢ.**
**➛ `/help` ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴀʙᴏᴜᴛ ᴄᴍᴅ ɢɪᴠᴇɴ ɪɴ ᴛʜɪs ʙᴏᴛ.**
**➛ `/start` ᴜsᴇᴅ ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.**
**➛ `/upload` ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴘɪᴄs, ᴠᴅᴏ, ᴀɴɪᴍᴀᴛᴏɴ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.**
**➛ `/uploadtxt` ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴛᴇxᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ.**
**➛ `/broadcast` ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜsᴇʀs ᴀɴᴅ ᴄʜᴀᴛᴇs.**
**───────────────**
<b> @Rokubotz </b>
"""

    TEAM_STRING = f"""
<u>**ʀᴏᴋᴜʙᴏᴛᴢ:**</u>

ᴛᴏ ᴀʟʟ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴜᴘᴘᴏʀᴛᴇᴅ ʀᴏᴋᴜʙᴏᴛᴢ ᴀɴᴅ ᴜᴛɪʟɪᴢᴇᴅ ᴛʜᴇɪʀ ʙᴏᴛs, ᴡᴇ ᴇxᴛᴇɴᴅ ᴏᴜʀ ʜᴇᴀʀᴛꜰᴇʟᴛ ᴛʜᴀɴᴋs. ʏᴏᴜʀ ᴄᴏɴᴛɪɴᴜᴇᴅ sᴜᴘᴘᴏʀᴛ ʜᴀs ʙᴇᴇɴ ɪɴsᴛʀᴜᴍᴇɴᴛᴀʟ ɪɴ ᴅʀɪᴠɪɴɢ ʀᴏᴋᴜʙᴏᴛᴢ ᴛᴏ ɢʀᴇᴀᴛᴇʀ ʜᴇɪɢʜᴛs, ᴀɴᴅ ᴡᴇ ʟᴏᴏᴋ ꜰᴏʀᴡᴀʀᴅ ᴛᴏ ᴘʀᴏᴠɪᴅɪɴɢ ʏᴏᴜ ᴡɪᴛʜ ᴇᴠᴇɴ ᴍᴏʀᴇ ɪɴɴᴏᴠᴀᴛɪᴠᴇ sᴏʟᴜᴛɪᴏɴs ɪɴ ᴛʜᴇ ꜰᴜᴛᴜʀᴇ.
**──────────────**
<b> @Rokubotz </b>
"""    
