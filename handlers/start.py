from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Devil Music Bot, an open-source bot that lets you play music in your Telegram groups voice chat.
This bot is based on su music project and hamkers vc bot. 

To add in your group contact us at @abhinasroy

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒𝗙𝗔𝗧𝗛𝗘𝗥", url="https://t.me/abhinasroy"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 𝗚𝗥𝗢𝗨𝗣", url="https://t.me/DOSTI_GROUP_1234"
                    ),
                    InlineKeyboardButton(
                        "𝗩𝗖 𝗣𝗟𝗔𝗬𝗘𝗥 🔈", url="https://t.me/roy_music1"
                    ),
                    InlineKeyboardButton(
                        "𝗕𝗢𝗧 😈", url="https://t.me/MOVIE_CHANNEL_1234" )
                ],
                [
                    InlineKeyboardButton(
                        "𝗔𝗕𝗛𝗜𝗡𝗔𝗦", url="https://t.me/abhinasroy"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
