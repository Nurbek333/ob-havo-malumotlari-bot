from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Weather options with emojis
weather_inl_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌇 Tashkent", callback_data="Tashkent"), InlineKeyboardButton(text="🏰 Buxoro", callback_data="Bukhara")],
        [InlineKeyboardButton(text="🏜️ Navoi", callback_data="Navoi"), InlineKeyboardButton(text="🌾 Sirdaryo", callback_data="Sirdaryo")],
        [InlineKeyboardButton(text="🏛️ Samarqand", callback_data="Samarkand"), InlineKeyboardButton(text="🌻 Farg'ona", callback_data="Fergana")],
        [InlineKeyboardButton(text="🏞️ Namangan", callback_data="Namangan"), InlineKeyboardButton(text="🌳 Andijon", callback_data="Andijan")],
        [InlineKeyboardButton(text="🌿 Jizzah", callback_data="Jizzakh"), InlineKeyboardButton(text="🏙️ Urganch", callback_data="Urgench")],
        [InlineKeyboardButton(text="🏜️ Nukus", callback_data="Nukus"), InlineKeyboardButton(text="🌄 Termiz", callback_data="Termiz")],
        [InlineKeyboardButton(text="🏙️ Zarafshon", callback_data="Zarafshan"), InlineKeyboardButton(text="🏰 Hiva", callback_data="Khiva")]
    ]
)

# Settings with emojis
sozlamalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📆 1 kunlik ma'lumot", callback_data="kun")],
        [InlineKeyboardButton(text="📆 Haftalik ma'lumot", callback_data="kunlik")],
        [InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="sozlamalar")],
    ]
)

# Settings options with emojis
sozlamalarni_ichi = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📍 Shaharni o'zgartirish", callback_data="shahar")],
        [InlineKeyboardButton(text="🔙 Ortga qaytish", callback_data="ortga")],
    ]
)
