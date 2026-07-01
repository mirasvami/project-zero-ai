from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio
from handlers.courses import router as courses_router
from handlers.courses import signup_ru, signup_uz
TOKEN = "8690521717:AAF53_5bDx3qu9Bnw6eLC_QHsInNPsYD2Cc"
ADMIN_ID = 7903745315

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(courses_router)

user_data = {}

languages = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺 Русский"), KeyboardButton(text="🇺🇿 O'zbekcha")]
    ],
    resize_keyboard=True
)

menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Курсы"), KeyboardButton(text="💰 Цены")],
        [KeyboardButton(text="👩‍🏫 Преподаватели"), KeyboardButton(text="🕒 Время работы")],
        [KeyboardButton(text="📍 Локация"), KeyboardButton(text="🎁 Пробный урок")],
        [KeyboardButton(text="☎️ Связаться")]
    ],
    resize_keyboard=True
)

menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Kurslar"), KeyboardButton(text="💰 Narxlar")],
        [KeyboardButton(text="👩‍🏫 O'qituvchilar"), KeyboardButton(text="🕒 Ish vaqti")],
        [KeyboardButton(text="📍 Manzil"), KeyboardButton(text="🎁 Sinov darsi")],
        [KeyboardButton(text="☎️ Bog'lanish")]
    ],
    resize_keyboard=True
)

courses_ru_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇬🇧 Английский"), KeyboardButton(text="🇷🇺 Русский язык")],
        [KeyboardButton(text="🎯 IELTS / CEFR"), KeyboardButton(text="💻 IT курс")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

courses_uz_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇬🇧 Ingliz tili"), KeyboardButton(text="🇷🇺 Rus tili")],
        [KeyboardButton(text="🎯 IELTS / CEFR uz"), KeyboardButton(text="💻 IT kurs")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

teachers_ru_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👩‍🏫 Malika Karimova"), KeyboardButton(text="👩‍🏫 Aziza Rasulova")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

teachers_uz_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👩‍🏫 Malika Karimova uz"), KeyboardButton(text="👩‍🏫 Aziza Rasulova uz")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌍 Выберите язык / Tilni tanlang:",
        reply_markup=languages
    )


@dp.message(F.text == "🇷🇺 Русский")
async def russian(message: Message):
    await message.answer(
        "🏫 Добро пожаловать!\n\nВыберите раздел 👇",
        reply_markup=menu_ru
    )


@dp.message(F.text == "🇺🇿 O'zbekcha")
async def uzbek(message: Message):
    await message.answer(
        "🏫 Xush kelibsiz!\n\nKerakli bo'limni tanlang 👇",
        reply_markup=menu_uz
    )


@dp.message(F.text == "📚 Курсы")
async def courses_ru(message: Message):
    await message.answer(
        "📚 Выберите курс:",
        reply_markup=courses_ru_menu
    )


@dp.message(F.text == "📚 Kurslar")
async def courses_uz(message: Message):
    await message.answer(
        "📚 Qaysi kurs sizni qiziqtiradi?",
        reply_markup=courses_uz_menu
    )


@dp.message(F.text == "👩‍🏫 Преподаватели")
async def teachers_ru(message: Message):
    await message.answer(
        "👩‍🏫 Выберите преподавателя:",
        reply_markup=teachers_ru_menu
    )


@dp.message(F.text == "👩‍🏫 O'qituvchilar")
async def teachers_uz(message: Message):
    await message.answer(
        "👩‍🏫 O'qituvchini tanlang:",
        reply_markup=teachers_uz_menu
    )


@dp.message(F.text == "⬅️ Назад")
async def back_ru(message: Message):
    await message.answer(
        "🏫 Главное меню",
        reply_markup=menu_ru
    )


@dp.message(F.text == "⬅️ Orqaga")
async def back_uz(message: Message):
    await message.answer(
        "🏫 Asosiy menyu",
        reply_markup=menu_uz
    )
@dp.message(F.text == "🇬🇧 Английский")
async def english_ru(message: Message):
    await message.answer(
        "🇬🇧 Английский язык\n\n"
        "Длительность: 3 месяца\n"
        "Занятия: 3 раза в неделю\n"
        "Цена: 700 000 сум/месяц\n"
        "Уровни: Beginner, Elementary, Intermediate\n\n"
        "🎁 Первый пробный урок бесплатно.",
        reply_markup=signup_ru
    )


@dp.message(F.text == "🇬🇧 Ingliz tili")
async def english_uz(message: Message):
    await message.answer(
        "🇬🇧 Ingliz tili\n\n"
        "Davomiyligi: 3 oy\n"
        "Darslar: haftasiga 3 marta\n"
        "Narx: 700 000 so'm/oy\n"
        "Darajalar: Beginner, Elementary, Intermediate\n\n"
        "🎁 Birinchi sinov darsi bepul.",
        reply_markup=signup_uz
    )


@dp.message(F.text == "🇷🇺 Русский язык")
async def russian_course_ru(message: Message):
    await message.answer(
        "🇷🇺 Русский язык\n\n"
        "Длительность: 3 месяца\n"
        "Занятия: 3 раза в неделю\n"
        "Цена: 600 000 сум/месяц\n"
        "Направление: разговорный русский, грамматика, подготовка к экзаменам.\n\n"
        "🎁 Пробный урок доступен.",
        reply_markup=signup_ru
    )


@dp.message(F.text == "🇷🇺 Rus tili")
async def russian_course_uz(message: Message):
    await message.answer(
        "🇷🇺 Rus tili\n\n"
        "Davomiyligi: 3 oy\n"
        "Darslar: haftasiga 3 marta\n"
        "Narx: 600 000 so'm/oy\n"
        "Yo'nalish: so'zlashuv, grammatika, imtihonga tayyorgarlik.\n\n"
        "🎁 Sinov darsi mavjud.",
        reply_markup=signup_uz
    )


@dp.message(F.text == "🎯 IELTS / CEFR")
async def ielts_ru(message: Message):
    await message.answer(
        "🎯 IELTS / CEFR\n\n"
        "Длительность: 4 месяца\n"
        "Занятия: 3–4 раза в неделю\n"
        "Цена: 900 000 сум/месяц\n"
        "Цель: IELTS 6.5+ / CEFR B2–C1\n\n"
        "✅ Подготовка по Reading, Listening, Writing, Speaking.",
        reply_markup=signup_ru
    )


@dp.message(F.text == "🎯 IELTS / CEFR uz")
async def ielts_uz(message: Message):
    await message.answer(
        "🎯 IELTS / CEFR\n\n"
        "Davomiyligi: 4 oy\n"
        "Darslar: haftasiga 3–4 marta\n"
        "Narx: 900 000 so'm/oy\n"
        "Maqsad: IELTS 6.5+ / CEFR B2–C1\n\n"
        "✅ Reading, Listening, Writing, Speaking bo'yicha tayyorgarlik.",
        reply_markup=signup_uz
    )


@dp.message(F.text == "💻 IT курс")
async def it_ru(message: Message):
    await message.answer(
        "💻 IT курс\n\n"
        "Направления:\n"
        "• Компьютерная грамотность\n"
        "• Python для начинающих\n"
        "• SMM и дизайн\n\n"
        "Цена: 800 000 сум/месяц\n"
        "🎁 Пробный урок доступен.",
        reply_markup=signup_ru
    )


@dp.message(F.text == "💻 IT kurs")
async def it_uz(message: Message):
    await message.answer(
        "💻 IT kurs\n\n"
        "Yo'nalishlar:\n"
        "• Kompyuter savodxonligi\n"
        "• Python boshlang'ich\n"
        "• SMM va dizayn\n\n"
        "Narx: 800 000 so'm/oy\n"
        "🎁 Sinov darsi mavjud.",
        reply_markup=signup_uz
    )
@dp.message(F.text == "👩‍🏫 Malika Karimova")
async def malika_ru(message: Message):
    await message.answer(
        "👩‍🏫 Malika Karimova\n\n"
        "Курс: Английский / IELTS\n"
        "Опыт: 6 лет\n"
        "Результаты учеников: IELTS 6.5–7.5\n"
        "Языки: русский, узбекский"
    )


@dp.message(F.text == "👩‍🏫 Malika Karimova uz")
async def malika_uz(message: Message):
    await message.answer(
        "👩‍🏫 Malika Karimova\n\n"
        "Kurs: Ingliz tili / IELTS\n"
        "Tajriba: 6 yil\n"
        "O'quvchilar natijasi: IELTS 6.5–7.5\n"
        "Tillar: rus, o'zbek"
    )


@dp.message(F.text == "👩‍🏫 Aziza Rasulova")
async def aziza_ru(message: Message):
    await message.answer(
        "👩‍🏫 Aziza Rasulova\n\n"
        "Курс: Русский язык\n"
        "Опыт: 5 лет\n"
        "Результаты: подготовка к C1 и школьным экзаменам"
    )


@dp.message(F.text == "👩‍🏫 Aziza Rasulova uz")
async def aziza_uz(message: Message):
    await message.answer(
        "👩‍🏫 Aziza Rasulova\n\n"
        "Kurs: Rus tili\n"
        "Tajriba: 5 yil\n"
        "Natijalar: C1 va maktab imtihonlariga tayyorlov"
    )


@dp.message(F.text == "💰 Цены")
async def price_ru(message: Message):
    await message.answer(
        "💰 Стоимость обучения:\n\n"
        "🇬🇧 Английский — 700 000 сум/месяц\n"
        "🇷🇺 Русский язык — 600 000 сум/месяц\n"
        "🎯 IELTS / CEFR — 900 000 сум/месяц\n"
        "💻 IT курс — 800 000 сум/месяц"
    )


@dp.message(F.text == "💰 Narxlar")
async def price_uz(message: Message):
    await message.answer(
        "💰 Kurs narxlari:\n\n"
        "🇬🇧 Ingliz tili — 700 000 so'm/oy\n"
        "🇷🇺 Rus tili — 600 000 so'm/oy\n"
        "🎯 IELTS / CEFR — 900 000 so'm/oy\n"
        "💻 IT kurs — 800 000 so'm/oy"
    )


@dp.message(F.text == "🕒 Время работы")
async def time_ru(message: Message):
    await message.answer(
        "🕒 Время работы:\n\n"
        "Пн–Пт: 09:00–21:00\n"
        "Сб: 10:00–18:00\n"
        "Вс: выходной"
    )


@dp.message(F.text == "🕒 Ish vaqti")
async def time_uz(message: Message):
    await message.answer(
        "🕒 Ish vaqti:\n\n"
        "Dushanba–Juma: 09:00–21:00\n"
        "Shanba: 10:00–18:00\n"
        "Yakshanba: dam olish kuni"
    )


@dp.message(F.text == "📍 Локация")
async def location_ru(message: Message):
    await message.answer(
        "📍 Наш адрес:\n\n"
        "Ташкент, центр города\n"
        "Карта: https://maps.google.com"
    )


@dp.message(F.text == "📍 Manzil")
async def location_uz(message: Message):
    await message.answer(
        "📍 Bizning manzil:\n\n"
        "Toshkent shahri, shahar markazi\n"
        "Xarita: https://maps.google.com"
    )


@dp.message(F.text == "☎️ Связаться")
async def contact_ru(message: Message):
    await message.answer(
        "☎️ Связаться с нами:\n\n"
        "Телефон: +998 90 000 00 00\n"
        "Telegram: @projectzero\n"
        "Instagram: @projectzero.ai"
    )


@dp.message(F.text == "☎️ Bog'lanish")
async def contact_uz(message: Message):
    await message.answer(
        "☎️ Bog'lanish:\n\n"
        "Telefon: +998 90 000 00 00\n"
        "Telegram: @projectzero\n"
        "Instagram: @projectzero.ai"
    )
@dp.message(F.text == "🎁 Пробный урок")
async def trial_ru(message: Message):
    user_data[message.from_user.id] = {"step": "name_ru"}
    await message.answer("🎁 Запись на пробный урок\n\nКак вас зовут?")


@dp.message(F.text == "🎁 Sinov darsi")
async def trial_uz(message: Message):
    user_data[message.from_user.id] = {"step": "name_uz"}
    await message.answer("🎁 Sinov darsiga yozilish\n\nIsmingiz nima?")


@dp.message()
async def collect_trial(message: Message):
    user_id = message.from_user.id

    if user_id not in user_data:
        await message.answer("Пожалуйста, выберите раздел из меню.\nIltimos, menyudan bo'lim tanlang.")
        return

    step = user_data[user_id]["step"]

    if step == "name_ru":
        user_data[user_id]["name"] = message.text
        user_data[user_id]["step"] = "phone_ru"
        await message.answer("Отправьте номер телефона.")
    elif step == "phone_ru":
        user_data[user_id]["phone"] = message.text
        user_data[user_id]["step"] = "course_ru"
        await message.answer("Какой курс вас интересует?")
    elif step == "course_ru":
        user_data[user_id]["course"] = message.text
        data = user_data.pop(user_id)
        await bot.send_message(
    ADMIN_ID,
    f"🟢 Новая заявка!\n\n"
    f"👤 Имя: {data['name']}\n"
    f"📞 Телефон: {data['phone']}\n"
    f"📚 Курс: {data['course']}"
)
        await message.answer(
            f"✅ Заявка принята!\n\nИмя: {data['name']}\nТелефон: {data['phone']}\nКурс: {data['course']}\n\nАдминистратор скоро свяжется с вами."
        )

    elif step == "name_uz":
        user_data[user_id]["name"] = message.text
        user_data[user_id]["step"] = "phone_uz"
        await message.answer("Telefon raqamingizni yuboring.")
    elif step == "phone_uz":
        user_data[user_id]["phone"] = message.text
        user_data[user_id]["step"] = "course_uz"
        await message.answer("Qaysi kurs sizni qiziqtiradi?")
    elif step == "course_uz":
        user_data[user_id]["course"] = message.text
        data = user_data.pop(user_id)
        await bot.send_message(
    ADMIN_ID,
    f"🟢 Yangi ariza!\n\n"
    f"👤 Ism: {data['name']}\n"
    f"📞 Telefon: {data['phone']}\n"
    f"📚 Kurs: {data['course']}"
)
        await message.answer(
            f"✅ Arizangiz qabul qilindi!\n\nIsm: {data['name']}\nTelefon: {data['phone']}\nKurs: {data['course']}\n\nAdministrator tez orada siz bilan bog'lanadi."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())