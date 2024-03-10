from aiogram import Router, F, types
from aiogram.filters import Command
import logging

film_router = Router()

@film_router.message(Command('films'))
async def show_films(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Ужасы", callback_data="Horrors_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Боевики", callback_data="Thrillers_for_film")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_for_film")
            ],
        ]
    )
    logging.info(message.from_user)
    await message.answer("Какой жанр фильмов вы хотите?", reply_markup=kb)

@film_router.callback_query(F.data == "Comedian_for_film")
async def show_comedian(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наполеон: динамит", url="https://example.com/napoleon_dynamite")
            ],
            [
                types.InlineKeyboardButton(text="Оффисное пространство", url="https://example.com/office_space")
            ],
            [
                types.InlineKeyboardButton(text="Поездка в америку", url="https://example.com/trip_to_america")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=kb)


@film_router.callback_query(F.data == "Horrors_for_film")
async def show_horror(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Прочь", url="https://example.com/get_out")
            ],
            [
                types.InlineKeyboardButton(text="Сияние", url="https://example.com/the_shining")
            ],
            [
                types.InlineKeyboardButton(text="Реинкарнация", url="https://example.com/reincarnation")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=kb)

@film_router.callback_query(F.data == "Fantastic_for_film")
async def show_fantastic(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Гарри Поттер и философский камень", url="https://example.com/harry_potter")
            ],
            [
                types.InlineKeyboardButton(text="Властелин колец: Братство кольца", url="https://example.com/lotr")
            ],
            [
                types.InlineKeyboardButton(text="Дева и дракон", url="https://example.com/dragonheart")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=kb)

@film_router.callback_query(F.data == "Thrillers_for_film")
async def show_thrillers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Безумный Макс: Дорога ярости", url="https://example.com/mad_max_fury_road")
            ],
            [
                types.InlineKeyboardButton(text="Бесславные ублюдки", url="https://example.com/inglourious_basterds")
            ],
            [
                types.InlineKeyboardButton(text="Kingsman: Секретная служба", url="https://example.com/kingsman")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=kb)

@film_router.callback_query(F.data == "Popular_for_film")
async def show_populars(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Дюна: Часть вторая", url="https://example.com/dune_2")
            ],
            [
                types.InlineKeyboardButton(text="Каскадёры", url="https://example.com/cascaders")
            ],
            [
                types.InlineKeyboardButton(text="Фуриоса: Хроники Безумного Макса", url="https://example.com/furiosa")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите фильм:", reply_markup=kb)

