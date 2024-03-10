from aiogram import Router, F, types
from aiogram.filters import Command
import logging

anime_router = Router()

@anime_router.message(Command('anime'))
async def show_anime(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Ужас", callback_data="Horrors_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Боевики", callback_data="Thrillers_for_anime")
            ],
            [
                types.InlineKeyboardButton(text="Популярные за 2024-год", callback_data="Popular_for_2024")
            ],
        ]
    )
    logging.info(message.from_user)
    await message.answer("Какой жанр аниме вы хотите?", reply_markup=kb)

@anime_router.callback_query(F.data == "Comedian_for_anime")
async def show_comedian(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="One Punch Man", url="https://example.com/one_punch_man")
            ],
            [
                types.InlineKeyboardButton(text="Gintama", url="https://example.com/gintama")
            ],
            [
                types.InlineKeyboardButton(text="Daily Lives of High School Boys", url="https://example.com/daily_lives_of_high_school_boys")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=kb)

@anime_router.callback_query(F.data == "Horrors_for_anime")
async def show_horror(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Tokyo Ghoul", url="https://example.com/tokyo_ghoul")
            ],
            [
                types.InlineKeyboardButton(text="Another", url="https://example.com/another")
            ],
            [
                types.InlineKeyboardButton(text="Parasyte", url="https://example.com/parasyte")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=kb)

@anime_router.callback_query(F.data == "Fantastic_for_anime")
async def show_fantastic(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Attack on Titan", url="https://example.com/attack_on_titan")
            ],
            [
                types.InlineKeyboardButton(text="Fullmetal Alchemist: Brotherhood", url="https://example.com/fullmetal_alchemist")
            ],
            [
                types.InlineKeyboardButton(text="Hunter x Hunter", url="https://example.com/hunter_x_hunter")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=kb)

@anime_router.callback_query(F.data == "Thrillers_for_anime")
async def show_thrillers(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Death Note", url="https://example.com/death_note")
            ],
            [
                types.InlineKeyboardButton(text="Psycho-Pass", url="https://example.com/psycho_pass")
            ],
            [
                types.InlineKeyboardButton(text="Steins;Gate", url="https://example.com/steins_gate")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=kb)

@anime_router.callback_query(F.data == "Popular_for_2024")
async def show_populars(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Demon Slayer: Kimetsu no Yaiba", url="https://example.com/demon_slayer")
            ],
            [
                types.InlineKeyboardButton(text="My Hero Academia", url="https://example.com/my_hero_academia")
            ],
            [
                types.InlineKeyboardButton(text="Naruto", url="https://example.com/naruto")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите аниме:", reply_markup=kb)
