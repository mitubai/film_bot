from aiogram import Router, F, types
from aiogram.filters import Command
import logging

cartoons_router = Router()

@cartoons_router.message(Command('cartoons'))
async def show_cartoons(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Комедии", callback_data="Comedian_for_cartoon")
            ],
            [
                types.InlineKeyboardButton(text="Приключения", callback_data="Adventures_for_cartoon")
            ],
            [
                types.InlineKeyboardButton(text="Фантастика", callback_data="Fantastic_for_cartoon")
            ],
            [
                types.InlineKeyboardButton(text="Для детей", callback_data="ForKids")
            ],
            [
                types.InlineKeyboardButton(text="Популярные", callback_data="Popular_for_cartoon")
            ],
        ]
    )
    logging.info(message.from_user)
    await message.answer("Какой жанр мультфильмов вы хотите?", reply_markup=kb)

@cartoons_router.callback_query(F.data == "Comedian_for_cartoon")
async def show_comedian(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Семейка Симпсонов", url="https://example.com/simpsons")
            ],
            [
                types.InlineKeyboardButton(text="Футурама", url="https://example.com/futurama")
            ],
            [
                types.InlineKeyboardButton(text="Гравити Фолз", url="https://example.com/gravity_falls")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=kb)

@cartoons_router.callback_query(F.data == "Adventures_for_cartoon")
async def show_adventures(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Рик и Морти", url="https://example.com/rick_and_morty")
            ],
            [
                types.InlineKeyboardButton(text="Аватар: Легенда об Аанге", url="https://example.com/avatar")
            ],
            [
                types.InlineKeyboardButton(text="Наруто", url="https://example.com/naruto")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=kb)

@cartoons_router.callback_query(F.data == "Fantastic_for_cartoon")
async def show_fantastic(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Аладдин", url="https://example.com/aladdin")
            ],
            [
                types.InlineKeyboardButton(text="Холодное сердце", url="https://example.com/frozen")
            ],
            [
                types.InlineKeyboardButton(text="Тачки", url="https://example.com/cars")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=kb)

@cartoons_router.callback_query(F.data == "ForKids")
async def show_for_kids(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Пингвины из Мадагаскара", url="https://example.com/penguins_of_madagascar")
            ],
            [
                types.InlineKeyboardButton(text="Шрек", url="https://example.com/shrek")
            ],
            [
                types.InlineKeyboardButton(text="Маша и Медведь", url="https://example.com/masha_and_the_bear")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=kb)

@cartoons_router.callback_query(F.data == "Popular_for_cartoon")
async def show_populars(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Семейка Крудс", url="https://example.com/the_croods")
            ],
            [
                types.InlineKeyboardButton(text="Как приручить дракона", url="https://example.com/how_to_train_your_dragon")
            ],
            [
                types.InlineKeyboardButton(text="История игрушек", url="https://example.com/toy_story")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Выберите мультфильм:", reply_markup=kb)
