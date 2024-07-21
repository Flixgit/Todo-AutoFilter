class script(object):
    
    START_TXT = """<i>Hello {user} 👻.</i>

<blockquote><i>My Name Is {bot} 🎃.</i></blockquote>

<i>I Can Provide Movies For You, Just Add Me In Your Gorup Or Join Our Group Or Just Search In The PM 😁</i>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""

    MY_ABOUT_TXT = """<b><i>★ Server: <a href=https://www.heroku.com>Heroku</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>
★ Language: <a href=https://www.python.org>Python</a>
★ Library: <a href=https://pyrogram.org>Pyrogram</a></i></b>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""

    MY_OWNER_TXT = """
<b><i>★ Name: TODO
★ Username: <a href="https://t.me/TodoFactory">TodoFactory ✨</a>
★ Country: India 🇮🇳</i><b>"""

    STATUS_TXT = """<b><i>🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
🤑 Premium Users: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code></i></b>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""

    NEW_GROUP_TXT = """#NewGroup
★ Title - {}
★ ID - <code>{}</code>
★ Username - {}
★ Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NOT_FILE_TXT = """<i>👋🏻 Hello {},

I can't find the <b>{}</b> in my database! 🥲

👉🏻 Request here @Contact_Todobot with Year & seasons.
👉🏻 Google Search and check your spelling is correct.
👉🏻 Please read the Instructions to get better results.
👉🏻 Or not been released yet.</i>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""
    
    EARN_TXT = """<blockquote><b>How To Earn From This Bot 💸</b></blockquote>

<i>» Step 1:- First you have to this bot in your group with admin permission.

» Step 2:- Make an account on  shortner site.

» Step 3:- Click on the below given button to know how to connect your shortner with this bot.</i>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink mdisklink.link 5843c3cc645f5077b2200a2c77e0344879880b3e</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """<blockquote><b>Query: {query}</b></blockquote>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres} | 📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a>/10

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""

    FILE_CAPTION = """<b>{file_name}</b>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>

🚫 Click On The Close Button If You Forwarded The File 🚫"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""

    HELP_TXT = """<blockquote><b>NOTE 📝</b></blockquote>

<i><spoiler>Try each command without any argument to see more details 😹</spoiler></i>"""
    
    ADMIN_COMMAND_TXT = """<blockquote><b>BOT ADMIN COMMANDS 👇🏻</b></blockquote>

<i>/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/set_pm_search - to do pm search on/off
/index - to index bot accessible channels</i>"""
    
    USER_COMMAND_TXT = """<blockquote><b>BOT USER COMMANDS 👇🏻</b></blockquote>

<i>/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/set_fsub - to set force subscribe channels
/remove_fsub - to remove all force subscribe channel</i>"""
    
    SOURCE_TXT = """<i>
- Source - <a href=https://t.me/HA_Bots>Here</a>

- Developer - <a href="https://t.me/TodoFactory">Todo Factory ✨</a></i>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""

    PREMIUM_PLAN_TEXT = """<i>Every Here Has Premium Plan 🤍

• Still If You Guys Want To Donate, Scan The QR or Contact Me 💞</i>

<blockquote><b><a href="https://t.me/Todo_Archive">Todo Archive ⚡</a></b></blockquote>"""
