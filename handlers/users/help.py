from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message: Message):
    await message.answer(
        """<b>🆘 Yordam</b>

Assalomu alaykum! Men sizga ob-havo ma'lumotlarini taqdim etaman. Quyida mavjud bo'lgan komandalar haqida ma'lumotni topishingiz mumkin:

<b>1️⃣ /start</b> - Botni ishga tushiring va sizga qanday yordam bera olishim haqida ma'lumot oling.

<b>2️⃣ /current_weather [shahar nomi]</b> - Kiritingan shahar uchun joriy ob-havo ma'lumotlarini olish.
   Masalan: <code>/current_weather Toshkent</code>

<b>3️⃣ /forecast [shahar nomi]</b> - Kiritingan shahar uchun 5 kunlik ob-havo prognozini olish.
   Masalan: <code>/forecast Tashkent</code>

<b>4️⃣ /moon_phase</b> - Bugungi oy bosqichini bilib oling.

<b>5️⃣ /help</b> - Ushbu yordam xabarini ko'rsatadi.

<b>🌟 Qo'shimcha Ma'lumotlar:</b>
   - <b>Tong</b>: Tonggi haroratni bilib oling (06:00 - 12:00).
   - <b>Kun</b>: Kunduzgi haroratni bilib oling (12:00 - 18:00).
   - <b>Oqshom</b>: Oqshomgi haroratni bilib oling (18:00 - 24:00).

<b>📍 Misollar:</b>
- <code>Toshkent</code> shahrining joriy ob-havosi: <code>/current_weather Toshkent</code>
- <code>London</code> shahrining 5 kunlik ob-havo prognozi: <code>/forecast London</code>

<b>📨 Savollar yoki muammolar</b> uchun biz bilan bog'laning: /xabar

Yordam uchun doimo shu yerda bo'laman! 😊""",
        parse_mode='HTML'
    )

