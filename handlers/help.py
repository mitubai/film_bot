from aiogram import Router, F, types
from aiogram.filters import Command
import logging

help_router = Router()


@help_router.message(Command("help"))
async def show_anime(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Контакты", callback_data="contacts")
            ]
        ]
    )
    logging.info(message.from_user)
    await message.answer("Наша поддержка!", reply_markup=kb)


@help_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("О нас:\n"
                                  "Мы компания которая старается помогать\n"
                                  "людам находить фильмы, сериалы, аниме, мультики")


@help_router.callback_query(F.data == "contacts")
async def about(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Ватсапп", url="https://Wa.me/996755044489")
            ],
            [
                types.InlineKeyboardButton(text="Телеграмм", url="https://t.me/Timurskii_M"),
                types.InlineKeyboardButton(text="Жалоба", url="https://Wa.me")
            ]
        ]
    )
    logging.info(callback.from_user)
    await callback.message.answer("Наши контакты:", reply_markup=kb)
