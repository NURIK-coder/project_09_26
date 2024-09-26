from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

updt_dlt_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Изменить', callback_data='update')
    ],
    [
        InlineKeyboardButton(text='Удалить', callback_data='delete')
    ]
])
