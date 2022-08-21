import copy
from datetime import datetime
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import zz_zayav, kb_contact, kb_client_menu, kb_client_sochy, kb_client_abhaz, kb_client_voda
from keyboards import kb_client_vozduh, kb_client_menu2, open_menu_file  #kb_client_proch,
from excel_loader import edit2

from kbs import menu

from client_commands import get_commands_client

# список кому доступна кнопка вывод excel file
excel_files = ['489322950', '1189955796', '631293008', '5295520075']
msg_id_bot = []
msg_id_user = []
# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    global msgBot
    msg_id_user.clear()
    msgUser = message  # берем id msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)
    try:
        # кнопка вывести файл будет доступна только определенным людям
        if str(message.from_user.id) in excel_files:
            msgBot = await message.answer("Вас приветствует\nЧат-бот \"Сочифорния\"\n\nЕсли вы зашли не в тот пункт меню,\n и нужно вернуться назад,\nнапишите: /start\n\n"
                             "Если уже начали оформлять заявку\n и что-то ввели не верно,\nнапишите слово: *отмена*", parse_mode= "Markdown", reply_markup=open_menu_file)
            msg_id_bot.append(msgBot)
        else:
            msgBot = await message.answer("Вас приветствует\nЧат-бот \"Сочифорния\"\n\nЕсли вы зашли не в тот пункт меню,\n и нужно вернуться назад,\nнапишите: /start\n\n"
                "Если уже начали оформлять заявку\n и что-то ввели не верно,\nнапишите слово: *отмена*",
                parse_mode="Markdown", reply_markup=zz_zayav)
            msg_id_bot.append(msgBot)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/continent_test_bot')


# @dp.message_handler(commands=[''Вывести_файл''])
async def file_excel_loader(message : types.Message):
    global msgBot
    'для отправки файла excel'
    if str(message.from_user.id) in excel_files:  # файл могут получить только определенные люди
        await message.reply_document(open('my_book.xlsx', 'rb'), reply_markup=open_menu_file)
    if msgBot is not None:
        await msgBot.delete()
        msgBot = None  # чтобы не вызывалось ошибка если он нажмет дважды на кнопку, так как первый раз смс удалено, и её нельзя удалить ещё раз

    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)

    try:
        for i in msg_id_user:  # удаляем все сообщения от бота
            await i.delete()
        msg_id_user.clear()  # очищаем словарь, чтобы не возникали ошибки, ли не перебрасывало в except, когда это не нужно
    except:
        await msgUser.delete()

    # for i in msg_id_bot:  # очищаем список
    #     msg_id_user.remove(i)

    # for i in msg_id:
    #     await i.delete()  # удаляем смс бота
    # await msgs.delete()  # удаляем смс бота

new_data = []
# @dp.message_handler(commands=['Заполнить_заявку'])
async def otkr_menu(message : types.Message):
    from lists_news import old_data, greeting
    data = datetime.now().strftime("%d_%m_%Y").split("_")[1]
    # print(data, "data")
    new_data.clear()
    new_data.append(data)
    if old_data != new_data:
        # если даты не совпадают, значит другой день, и создаем новый лист в файле
        # если даты не совпадают, значит другой день, и создаем новый лист в файле
        greeting()

     # если совпали, значит тот же день, и нет нужды в создании нового листа
    name_sud_vrem.clear() # чистим список, чтобы при повторном зявке не было так как будно он выбрал море
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)
    msgBot = await message.answer("Поделитесь номером телефона", reply_markup=kb_contact)
    msg_id_bot.append(msgBot)


sp_phone = {}
# перехватываем номер телефона
# @dp.message_handler(content_types=['contact'])
async def contact(message):
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)
    global phonenumber
    if message.contact is not None:
        if edit2['is'] == 0:
            msgBot = await bot.send_message(message.chat.id, 'Меню', reply_markup=kb_client_menu)
            msg_id_bot.append(msgBot)
            # print(msg_id)
        else:
            msgBot = await bot.send_message(message.chat.id, 'Меню', reply_markup=kb_client_menu2)
            msg_id_bot.append(msgBot)
            # print(msg_id)
        phonenumber= str(message.contact.phone_number)
        # для вывода в тг создаем список
        sp_phone[message.chat.id] = phonenumber


"""обработчики хендлеров главного меню"""
@dp.message_handler(lambda message: 'Где найти нужный тур?' in message.text)
async def maps(message : types.Message):
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)

    await bot.send_message(message.chat.id, paps)
    for i in msg_id_bot:  # удаляем все сообщения от бота
        await i.delete()
    msg_id_bot.clear()

    for i in msg_id_user:
        await i.delete()
    msg_id_user.clear()



# путеводитель по боту
paps = ('CОЧИ:\n----------\nКрасная поляна\nОбзорная Сочи\n33 Водопада\nЭпоха времени\nВоронцовские пещеры\nКаньоны Псахо (джип-тур)\nМамонтово Ущелье (джип-тур)\nСолохаул (джип-тур)\nИНДИВИДУАЛЬНЫЙ ТУР\n\n'
        'АБХАЗИЯ:\n----------------\nЗолотое Кольцо\nАбхазское застолье\nТермальные Источники\nГорода Призраки\nАльпийские Луга (джип-тур)\nАбхазский драйв (джип-тур)\nИНДИВИДУАЛЬНЫЙ ТУР\n\n'
        'МОРЕ:\n-----------\nМорская прогулка\nРыбалка в море\nАРЕНДА ЯХТ\n\n'
        'АКТИВ:\n------------\nРафтинг\nДайвинг\nКонные Прогулки\nКвадроциклы и Багги\nПараплан\nВоздушный Шар\nВертолёт\nПарашют\nСолохаул Парк\n\n'
        'Прочее:\n-------------\nШашлыки (индивидуальный)\nВечеринка в лесу\nАквапарк\nСафари Парк\nФорт Боярд\nКвесты\nБилеты на мероприятия\nДРУГОЕ')

# @dp.message_handler(commands="Сочи")
async def sochy(message : types.Message):
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)
    msgBot = await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_sochy)
    msg_id_bot.append(msgBot)

    # for i in msg_id: # удаляем сообщение от бота
    #     # print(i)
    #     await i.delete()
    # for i in msg_id_user: # удаляем сообщения от пользователя
    #     await i.delete()
    #     print(i)


# @dp.message_handler(commands="Абхазия")
async def abhaz(message : types.Message):
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)

    msgBot = await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_abhaz)
    msg_id_bot.append(msgBot)

name_sud_vrem = []
# @dp.message_handler(commands="Вода")
async def voda(message : types.Message):
    name_sud_vrem.append(1)
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)
    msgBot = await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_voda)
    msg_id_bot.append(msgBot)

# @dp.message_handler(commands="Воздух")
async def vozduh(message : types.Message):
    msgUser = message  # берем msg пользователя, чтобы потом удалить его
    msg_id_user.append(msgUser)
    msgBot = await bot.send_message(message.chat.id, "Ваш выбор!", reply_markup=kb_client_vozduh)
    msg_id_bot.append(msgBot)


async def all_handler(message : types.Message):

    # print(message)

    for option in menu:

        _name = option['name']

        if _name != 'menu1':

            for keyboard in option['keyboards']:

                _handler = keyboard['handler']

                if _handler != 'dat_ukaz':

                    for button in keyboard['buttons']:

                        text = button['text']
                        status = button['status']

                        if status == 1 and text == message.text:  # status 1 команда активна
                            await eval(_handler)(message)  # eval(_handler) перевод str в функцию и (message) запуск


cmnds = get_commands_client(menu)  # определяет команду клиента используя словарь из client_commands.py
def regiter_handlers_client(dp : Dispatcher):

    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(contact, content_types=['contact'])

    dp.register_message_handler(all_handler, lambda message: message.text in cmnds)  # определяет нужную функцию используя словарь из kbs.py


    # dp.register_message_handler(otkr_menu, lambda message: 'Открыть меню' in message.text)
    dp.register_message_handler(contact, content_types=['contact'])
    # dp.register_message_handler(sochy, lambda message: 'СOЧИ' in message.text) # сочи о на анг, чтобы не среагировал на обзор на сочи кнопку
    # dp.register_message_handler(abhaz, lambda message: 'АБХАЗИЯ' in message.text)
    # dp.register_message_handler(voda, lambda message: 'МОРЕ' in message.text)
    # dp.register_message_handler(vozduh, lambda message: 'АКТИВ' in message.text)
    # dp.register_message_handler(file_excel_loader, lambda message: 'Вывести файл' in message.text)