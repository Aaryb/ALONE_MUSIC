import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
     ("Sunday", 60 * 60 * 24 * 7),
     ("Day", 60 * 60 * 24),
     ("Hour", 60*60),
     ("Minute", 60),
     ("Second", 1),
 )


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)

@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.edit("Pinging...")
   delta_ping = time() - start
   await m_reply.edit("0% ▒▒▒▒▒▒▒▒▒▒")
   await m_reply.edit("20% ██▒▒▒▒▒▒▒▒")
   await m_reply.edit("40% ████▒▒▒▒▒▒")
   await m_reply.edit("60% ██████▒▒▒▒")
   await m_reply.edit("80% ████████▒▒")
   await m_reply.edit("100% ██████████")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"**┞◈𝗣𝗼𝗻𝗴!! Music Alone Userbot🏓**\n**┞◈Pinger**  - {delta_ping * 1000:.3f} ms \n**┞◈Uptime** - {uptime}")


@Client.on_message(filters.command(["pong"], prefixes=f"{HNDLR}"))
async def pong(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   pong = await m.edit("Pinging...")
   delta_ping = time() - start
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏===◈❏◈")
   await pong.edit("❏====❏◈◈")
   await pong.edit("**◈PINGGGG!**")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await pong.edit(
       f"**❏AloneMusicUserbot**\n**❏Pinging** : {delta_ping * 1000:.3f} ms\n**❏Bot Uptime** : {uptime}")

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Alone Music Userbot Restarted**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
 <b>👋 Hello {m.from_user.mention}!
 MUSIC PLAYER HELP MENU
 COMMANDS FOR EVERYONE
 • {HNDLR}play [song title |  youtube link |  reply audio file] - to play the song
 • {HNDLR}videoplay [video title |  youtube link |  reply video file] - to play video
 • {HNDLR}playlist to view playlist
 • {HNDLR}ping - to check status
 • {HNDLR}id - to view user id
 • {HNDLR}video - video title |  yt link to search video
 • {HNDLR}song - song title |  yt link to search for songs
 • {HNDLR}help - to see a list of commands
 • {HNDLR}join- to join |  to group
 COMMANDS FOR ALL ADMINS
 • {HNDLR}resume - to continue playing the song or video
 • {HNDLR}pause - to pause the playback of a song or video
 • {HNDLR}skip - to skip a song or video
 • {HNDLR}end - to end playback
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hello {m.from_user.mention}!
🗃️ Music And Video Player UserBot
🔰 Telegram UserBot To Play Songs And Videos In Telegram Voice Chat.
👩‍💻 Maintaned By 
• [Alone](https://t.me/i_am_pro_king)
📝 Persyaratan
• Python 3.8+
• FFMPEG
• Nodejs v16+
[Repo VC-Userbot](https://github.com/RioProjectX/VC-Userbot)
📝 Variabel Required
• `API_ID` - Get From [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Get From [my.telegram.org](https://my.telegram.org)
• `SESSION` - String session Pyrogram.
• `SUDO_USER` - Telegram Account ID Used As Admin 
• `HNDLR` - Handler to run your userbot
"""
    await m.reply(REPO, disable_web_page_preview=True)
