from aiogram import types, Router
from aiogram.filters import Command
from utils.custom_filters import AdminIdFilter
from typing import Union

start_router = Router()

@start_router.message(Command(commands=["start"]), AdminIdFilter())
async def start(message: Union[types.Message, types.CallbackQuery]):
  await message.reply(f"HEIL {message.from_user.username or "hitler"}")