from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋! Saya dapat memutar musik dalam obrolan suara Grup Telegram.\n\n✣ Apakah Anda ingin saya memutar musik di obrolan suara grup Telegram Anda? Silakan klik \'📜 Panduan Menggunakan BOT 📜\' tombol di bawah untuk mengetahui bagaimana cara menggunakan saya.\n\n✣ Tambahkan [Bintang Musik Assistant](https://t.me/@bintankgede2) ke grup Anda untuk memutar musik di obrolan suara grup Anda.\n\n Managed With ☕️ By [Bintang](https://t.me/bintankgede)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Panduan Menggunakan BOT 📜", url="https://telegra.ph/CARA-PENGGUNAAN-BOT-04-28")
                  ],[
                    InlineKeyboardButton(
                        "Group Owner", url="https://t.me/maribicaraa"
                    ),
                    InlineKeyboardButton(
                        "Channel Owner", url="https://t.me/coverbuatsendiri"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✣ Pemutar Musik Sedang Online ✣**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Owner", url="https://t.me/maribicaraa"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/bintankgede"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Owner", url="https://t.me/maribicaraa"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/bintankgede"
                    )
                ]
            ]
        )
   )
