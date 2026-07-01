from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

signup_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Записаться на пробный урок", callback_data="signup_ru")]
    ]
)

signup_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📝 Sinov darsiga yozilish", callback_data="signup_uz")]
    ]
)

courses_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇬🇧 Английский")],
        [KeyboardButton(text="🇷🇺 Русский язык")],
        [KeyboardButton(text="🎯 IELTS / CEFR")],
        [KeyboardButton(text="💻 IT")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

courses_uz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇬🇧 Ingliz tili")],
        [KeyboardButton(text="🇷🇺 Rus tili")],
        [KeyboardButton(text="🎯 IELTS / CEFR")],
        [KeyboardButton(text="💻 IT")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

@router.message(F.text == "📚 Курсы")
async def courses_ru_menu(message: Message):
    await message.answer(
        "📚 Выберите курс:",
        reply_markup=courses_ru
    )

@router.message(F.text == "📚 Kurslar")
async def courses_uz_menu(message: Message):
    await message.answer(
        "📚 Kursni tanlang:",
        reply_markup=courses_uz
    )
@router.message(F.text == "🇬🇧 Английский")
async def english_ru(message: Message):
    await message.answer(
        "🇬🇧 Английский язык\n\n"
        "📅 Длительность: 3 месяца\n"
        "📚 Занятия: 3 раза в неделю\n"
        "💰 Цена: 700 000 сум/месяц\n"
        "🎯 Уровни: Beginner, Elementary, Intermediate\n\n"
        "🎁 Первый пробный урок бесплатно.",
        reply_markup=signup_ru
    )


@router.message(F.text == "🇬🇧 Ingliz tili")
async def english_uz(message: Message):
    await message.answer(
        "🇬🇧 Ingliz tili\n\n"
        "📅 Davomiyligi: 3 oy\n"
        "📚 Darslar: haftasiga 3 marta\n"
        "💰 Narxi: 700 000 so'm/oy\n"
        "🎯 Darajalar: Beginner, Elementary, Intermediate\n\n"
        "🎁 Birinchi sinov darsi bepul.",
        reply_markup=signup_uz
    )
@router.message(F.text == "🇷🇺 Русский язык")
async def russian_ru(message: Message):
    await message.answer(
        "🇷🇺 Русский язык\n\n"
        "📅 Длительность: 3 месяца\n"
        "📚 Занятия: 3 раза в неделю\n"
        "💰 Цена: 600 000 сум/месяц\n"
        "🎯 Направления: разговорный русский, грамматика, подготовка к экзаменам.\n\n"
        "🎁 Пробный урок доступен."
    )


@router.message(F.text == "🇷🇺 Rus tili")
async def russian_uz(message: Message):
    await message.answer(
        "🇷🇺 Rus tili\n\n"
        "📅 Davomiyligi: 3 oy\n"
        "📚 Darslar: haftasiga 3 marta\n"
        "💰 Narxi: 600 000 so'm/oy\n"
        "🎯 Yo'nalish: so'zlashuv, grammatika, imtihonga tayyorgarlik.\n\n"
        "🎁 Sinov darsi mavjud."
    )
@router.message(F.text == "🎯 IELTS / CEFR")
async def ielts_course(message: Message):
    await message.answer(
        "🎯 IELTS / CEFR\n\n"
        "📅 Длительность: 4 месяца\n"
        "📚 Занятия: 3–4 раза в неделю\n"
        "💰 Цена: 900 000 сум/месяц\n"
        "🎯 Цель: IELTS 6.5+ / CEFR B2–C1\n\n"
        "✅ Подготовка: Reading, Listening, Writing, Speaking."
    )


@router.message(F.text == "💻 IT")
async def it_course(message: Message):
    await message.answer(
        "💻 IT курс\n\n"
        "📚 Направления:\n"
        "• Компьютерная грамотность\n"
        "• Python для начинающих\n"
        "• SMM и дизайн\n\n"
        "💰 Цена: 800 000 сум/месяц\n"
        "🎁 Пробный урок доступен."
    )
