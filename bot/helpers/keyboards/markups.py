from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, InlineKeyboardBuilder, InlineKeyboardButton

from ..fabrics.fabric import MenuCallback, PopupCallback, ChannelsCallback, SessionCallback

from typing import Optional

from models.schemas.channel import ChannelSchema
from typing import List


btn_main_menu = KeyboardButton(text='Главное меню 🏠')
btn_back_button = KeyboardButton(text='Назад')

btn_main_menu_inline = InlineKeyboardButton(text='Меню 🕹', callback_data=MenuCallback(action='open_menu').pack())


def welcome():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Регистрация 👤'))

    return builder.as_markup(resize_keyboard=True)


def confirm():
    '''
    Reply markup with YES and NO buttons.
    '''
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Да'))
    builder.row(KeyboardButton(text='Нет'))

    return builder.as_markup(resize_keyboard=True)


def profile():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Профиль 👤'))

    return builder.as_markup(resize_keyboard=True)


def get_new_captcha():
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text='Другую капчу 🤬'))

    return builder.as_markup(resize_keyboard=True)


def profile_menu():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Редактировать ✏', callback_data=MenuCallback(action='edit_profile').pack()))
    builder.row(btn_main_menu_inline)

    return builder.as_markup(resize_keyboard=True)


def profile_menu_list():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Имя', callback_data=MenuCallback(action='edit_name').pack()))
    builder.row(InlineKeyboardButton(text='Удалить профиль 🗑', callback_data=MenuCallback(action='delete_profile').pack()))
    builder.row(InlineKeyboardButton(text='Назад', callback_data=MenuCallback(action='cancel').pack()))

    return builder.as_markup(resize_keyboard=True)


def cry():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='😭', callback_data='cry'))

    return builder.as_markup(resize_keyboard=True)


def popup(message_id: int):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Закрыть 🗑', callback_data=PopupCallback(action='close', message_id=message_id).pack()))

    return builder.as_markup(resize_keyboard=True)


def menu():
    builder = ReplyKeyboardBuilder()

    btn_subscriptions = KeyboardButton(text='Каналы 🗂')
    btn_profile = KeyboardButton(text='Профиль 👤')
    btn_help = KeyboardButton(text='Помощь 🔍')

    builder.row(btn_subscriptions, btn_profile)
    builder.row(KeyboardButton(text='Связать 🔗'))
    builder.row(btn_help)

    return builder.as_markup(resize_keyboard=True)


def channels_list(channels: List[ChannelSchema]):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Добавить ➕', callback_data=ChannelsCallback(action='new').pack()))

    for channel in channels:
        builder.row(
            InlineKeyboardButton(
                text=f"{channel.title}   {'🔳' if channel.active else '⬜️'}",
                callback_data=ChannelsCallback(
                    action='open',
                    channel_id=channel.id,
                    ).pack()
            ))
        
    builder.row(btn_main_menu_inline)

    return builder.as_markup(resize_keyboard=True)

def back_to_channels_list():
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Я передумал', callback_data=ChannelsCallback(action='cancel').pack()))

    return builder.as_markup(resize_keyboard=True)


def channels_end():
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='Назад к каналам 🗂', callback_data=ChannelsCallback(action='cancel').pack()))
    builder.row(InlineKeyboardButton(text='Добавить ещё ➕', callback_data=ChannelsCallback(action='new').pack()))

    return builder.as_markup(resize_keyboard=True)

def channels():
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='Добавить ➕', callback_data=ChannelsCallback(action='new').pack()))

    return builder.as_markup(resize_keyboard=True)

def channel_view(channel: ChannelSchema):
    builder = InlineKeyboardBuilder()

    channel_url = 'https://t.me/' + channel.channel_id[1:]

    STATUS = {
        True: '🔳',
        False: '⬜️',
    }

    builder.row(InlineKeyboardButton(text='Перейти 🔍', url=channel_url))
    builder.row(InlineKeyboardButton(text='Поменять название ✏️', callback_data=ChannelsCallback(action='edit', target='title', channel_id=channel.id).pack()))
    builder.row(InlineKeyboardButton(text=f'Видимость {STATUS[channel.active]}', callback_data=ChannelsCallback(action='toggle', channel_id=channel.id).pack()))
    builder.row(InlineKeyboardButton(text='Удалить 🗑', callback_data=ChannelsCallback(action='delete', channel_id=channel.id).pack()))
    builder.row(InlineKeyboardButton(text='Назад к каналам 🗂', callback_data=ChannelsCallback(action='back').pack()))

    return builder.as_markup(resize_keyboard=True)

# DEVICES

# def devices_list(devices: list):
#     builder = InlineKeyboardBuilder()
#     builder.row(InlineKeyboardButton(text='Связать 🔗', callback_data=DeviceCallback(action='new').pack()))

#     for device in devices:
#         builder.row(InlineKeyboardButton(text=device['title'], callback_data=DeviceCallback(action='open', device_id=device['id']).pack()))

#     builder.row(btn_main_menu_inline)

#     return builder.as_markup(resize_keyboard=True)

# def device_menu():
#     builder = InlineKeyboardBuilder()
#     builder.row(InlineKeyboardButton(text='Связать 🔗', callback_data=DeviceCallback(action='new').pack()))
#     builder.row(btn_main_menu_inline)
#     return builder.as_markup(resize_keyboard=True)

# def back_to_devices_list():
#     pass

# def devices_end():
#     pass

# def device_view():
#     pass

# SESSIONS

def cancel_all_sessions():
    '''
    Reply markup with one button - CLOSE ALL SESSIONS
    '''
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text='Закрыть все сессии ❌', callback_data=SessionCallback(action='close_all_sessions').pack()))
    return builder.as_markup(resize_keyboard=True)