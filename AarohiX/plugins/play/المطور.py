from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["المطور", "السورس", "المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_video(
        video="https://telegra.ph/file/9ccdf1b81efa30d2adb53.mp4",
        caption="• Dev Bot ↦ تيتو\n━━━━━━━━━━━━\n• Dev ↦  AhmedTeto . \n• Bio ↦ ضع القياده لنا وتمتع بالطريق @T_S_T4",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة البوت . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )
    
