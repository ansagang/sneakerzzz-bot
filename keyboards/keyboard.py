from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnInformation = InlineKeyboardButton('Информация', callback_data='information')
btnMenu = InlineKeyboardButton('Каталог', callback_data='catalog')
btnHelp = InlineKeyboardButton('Возможности', callback_data='capability')
btnLoad = InlineKeyboardButton('Загрузить', callback_data='post')

btnBack = InlineKeyboardButton('« Назад', callback_data='back')
btnRemove = InlineKeyboardButton('🔻', callback_data='remove')
# btn3 = KeyboardButton('Поделиться номером', request_contact=True)
# btn4 = KeyboardButton('Поделиться локацией', request_location=True)

clientMenuKeyboard = InlineKeyboardMarkup(resize_keyboard=True)
clientMenuKeyboard.row(btnInformation, btnHelp, btnMenu)
clientAdminMenuKeyboard = InlineKeyboardMarkup(resize_keyboard=True)
clientAdminMenuKeyboard.row(btnInformation, btnHelp, btnMenu).add(btnLoad)

clientBackKeyboard = InlineKeyboardMarkup(resize_keyboard=True)
clientBackKeyboard.add(btnBack)

clientRemoveKeyboard = InlineKeyboardMarkup()
clientRemoveKeyboard.add(btnRemove)


