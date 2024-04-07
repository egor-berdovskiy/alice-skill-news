from aiogram import Bot, F
from aiogram.types import Message

from typing import Optional, List

from helpers.keyboards import markups

from models.schemas.channel import ChannelSchema


async def render_channels(message: Message, channels: List[ChannelSchema], smooth: Optional[bool] = False):
    if smooth:
        if channels:
            await message.edit_text(f'<b>Ваши каналы</b> 🗂', reply_markup=markups.channels_list(channels))
        else:
            await message.edit_text('Вы не отслеживаете ни один канал 🕸', reply_markup=markups.channels())
    else:
        if channels:
            await message.answer(f'<b>Ваши каналы</b> 🗂', reply_markup=markups.channels_list(channels))
        else:
            await message.answer('Вы не отслеживаете ни один канал 🕸', reply_markup=markups.channels())
