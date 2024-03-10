from aiogram import Router, F, types
from aiogram.filters import Command
import logging


start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Здравствуйте!, вы на канале по поиску фильмов, сериалов, аниме, мультиков. Полезные команды в нашем боте -\n"
                            "/films - фильмы\n"
                            "/cartoons - мультики\n"
                            "/anime - аниме\n"
                            "/serials - сериалы\n"
                            "/help - для жалобы либо для связи с нами")
