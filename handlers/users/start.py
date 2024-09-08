from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.weather_inl_b import weather_inl_button

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=""" 👋 Salom! Men sizga ob-havo ma'lumotlarini taqdim etaman.
        🔍 **Qanday ma'lumot olishni xohlaysiz?**
        1️⃣ **Joriy ob-havo**: Shahar nomini kiriting, men sizga joriy ob-havo ma'lumotlarini yuboraman.
        2️⃣ **Kunlik prognoz**: Shahar nomini kiriting va men sizga bugungi ob-havo prognozini taqdim etaman.
        🛠 **Qo'shimcha funksiyalar**:
        🌅 Tong, 🌞 Kun, 🌆 Oqshom uchun haroratni bilib oling.
        🌑 Oy bosqichini aniqlang.
        📍 **Misollar**:
        - `Toshkent`
        - `Navoiy`
        - `Buxoro`
        ❓ Savollar yoki yordam uchun /help komandasi orqali biz bilan bog'laning. """,parse_mode='Markdown', reply_markup=weather_inl_button)
    except:
        await message.answer(text="""👋 Salom! Men sizga ob-havo ma'lumotlarini taqdim etaman.
        🔍 **Qanday ma'lumot olishni xohlaysiz?**\n
        1️⃣ **Joriy ob-havo**: Shahar nomini kiriting, men sizga joriy ob-havo ma'lumotlarini yuboraman.
        2️⃣ **Kunlik prognoz**: Shahar nomini kiriting va men sizga bugungi ob-havo prognozini taqdim etaman.
        🛠 **Qo'shimcha funksiyalar**:
        🌅 Tong, 🌞 Kun, 🌆 Oqshom uchun haroratni bilib oling.
        🌑 Oy bosqichini aniqlang.
        📍 **Misollar**:
        - `Toshkent`
        - `Navoiy`
        - `Buxoro`
        ❓ Savollar yoki yordam uchun /help komandasi orqali biz bilan bog'laning. """,parse_mode='Markdown', reply_markup=weather_inl_button)
