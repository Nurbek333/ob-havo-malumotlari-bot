from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message: Message):
    await message.answer(
        """<b>ℹ️ Bot haqida</b>

<b>Salom!</b> Men [Bot nomi] - ob-havo ma'lumotlarini taqdim etuvchi botman. Quyidagi imkoniyatlarni taqdim etaman:

<b>🌤️ Joriy Ob-havo:</b>
- O'zingizga kerakli shaharda joriy ob-havo ma'lumotlarini tez va oson olish imkoniyatini beradi.

<b>📅 5 Kunlik Prognoz:</b>
- Har qanday shahar uchun 5 kunlik ob-havo prognozini ko'rsataman.

<b>🌕 Oy Bosqichi:</b>
- Bugungi oy bosqichini bilib olishingiz mumkin.

<b>🔧 Yordam:</b>
- Botni qanday ishlatishni bilishni xohlasangiz, yordam bo'limiga murojaat qilishingiz mumkin.

<b>Botning afzalliklari:</b>
- Foydalanuvchilarga qulay interfeys
- Aniq va dolzarb ob-havo ma'lumotlari
- Har qanday shahar uchun moslashuvchan prognozlar

<b>📌 Yaratuvchi:</b> Nurbek Uktamov

<b>📩 Aloqa:</b>
- Agar sizda savollar bo'lsa yoki bot haqida fikrlaringiz bo'lsa, biz bilan bog'laning: /xabar

Sizning ob-havo ehtiyojlaringizni qondirish uchun shu yerda bo'laman! 😊""",
        parse_mode='HTML'
    )


