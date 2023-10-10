from pyrogram.types import InlineKeyboardButton

import config
from AarohiX.utils import random 

## After Edits with Timer Bar


selections = [
     "▁▄▂▇▄▅▄▅▃", 
     "▁▃▇▂▅▇▄▅▃", 
     "▃▁▇▂▅▃▄▃▅", 
     "▃▄▂▄▇▅▃▅▁", 
     "▁▃▄▂▇▃▄▅▃", 
     "▃▁▄▂▅▃▇▃▅", 
     "▁▇▄▂▅▄▅▃▄", 
     "▁▃▅▇▂▅▄▃▇", 
     "▃▅▂▅▇▁▄▃▁", 
     "▇▅▂▅▃▄▃▁▃", 
     "▃▇▂▅▁▅▄▃▁", 
     "▅▄▇▂▅▂▄▇▁", 
     "▃▅▂▅▃▇▄▅▃",
]


## After Edits with Timer Bar


def stream_markup_timer(_, videoid, chat_id, played, dur):
    bar = random.choice(selections)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton( 
                text="💞", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="💖", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💝", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❣️𝐁ᴀᴅ𝗌ʜᴀʜ❣️",
                url=f"https://t.me/Shivans_Raj_BrockenHart",
            ),
            InlineKeyboardButton(
                text="❤️𝐁ᴇɢᴀᴍ❤️", url=f"https://t.me/Ziddi_Rani",
            ),
        ],
        [
           InlineKeyboardButton(
                text="💖𝐎ᴡɴᴇʀ💖", url=f"https://t.me/itz_Lucky_Raja",
            ),
           InlineKeyboardButton(
                text="💝𝐂ᴏ 𝐎ᴡɴᴇʀ💝", url=f"https://t.me/MR_RAJA_ROY",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌹𝐂ʟᴏ𝐬ᴇ🌹", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_sec(played)
    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "—"
    circle = "💖"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))
    
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💖", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💝", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
           InlineKeyboardButton(
                text="💖𝐎ᴡɴᴇʀ💖", url=f"https://t.me/itz_Lucky_Raja",
            ),
           InlineKeyboardButton(
                text="❣️𝐁ᴀᴅ𝗌ʜᴀʜ❣️", url=f"https://t.me/Shivans_Raj_BrockenHart",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️𝐁ᴇɢᴀᴍ❤️", url=f"https://t.me/Ziddi_Rani",
            ),
            InlineKeyboardButton(
                text="🌹𝐂ʟᴏ𝐬ᴇ🌹", callback_data="close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❣️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💖", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💝", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❣️𝐁ᴀᴅ𝗌ʜᴀʜ❣️",
                url=f"https://t.me/Shivans_Raj_BrockenHart",
            ),
            InlineKeyboardButton(
                text="❤️𝐁ᴇɢᴀᴍ❤️", url=f"https://t.me/Ziddi_Rani",
            ),
        ],
        [
           InlineKeyboardButton(
                text="💖𝐎ᴡɴᴇʀ💖", url=f"https://t.me/itz_Lucky_Raja",
            ),
           InlineKeyboardButton(
                text="💝𝐂ᴏ 𝐎ᴡɴᴇʀ💝", url=f"https://t.me/MR_RAJA_ROY",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌹𝐂ʟᴏ𝐬ᴇ🌹", callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❣️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💖", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💝", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
           InlineKeyboardButton(
                text="💖𝐎ᴡɴᴇʀ💖", url=f"https://t.me/itz_Lucky_Raja",
            ),
           InlineKeyboardButton(
                text="❣️𝐁ᴀᴅ𝗌ʜᴀʜ❣️", url=f"https://t.me/Shivans_Raj_BrockenHart",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️𝐁ᴇɢᴀᴍ❤️", url=f"https://t.me/Ziddi_Rani",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌹𝐂ʟᴏ𝐬ᴇ🌹", callback_data="close"
            )
        ],
    ]
    return buttons


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AarohiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AarohiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text="🖤 Lɪᴠᴇ 🖤",
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💓",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="💗",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


# Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="❣️",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton( 
                text="💞", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="💖", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="💝", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❣️𝐁ᴀᴅ𝗌ʜᴀʜ❣️",
                url=f"https://t.me/Shivans_Raj_BrockenHart",
            ),
            InlineKeyboardButton(
                text="❤️𝐁ᴇɢᴀᴍ❤️", url=f"https://t.me/Ziddi_Rani",
            ),
        ],
        [
           InlineKeyboardButton(
                text="💖𝐎ᴡɴᴇʀ💖", url=f"https://t.me/itz_Lucky_Raja",
            ),
           InlineKeyboardButton(
                text="💝𝐂ᴏ 𝐎ᴡɴᴇʀ💝", url=f"https://t.me/MR_RAJA_ROY",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌹𝐂ʟᴏ𝐬ᴇ🌹", callback_data="close"
            )
        ],
    ]
    return buttons
