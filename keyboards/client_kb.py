from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiogram.utils.markdown as fmt

# # открыть меню
# kb_menu0 = KeyboardButton('Где найти нужный тур?')
# kb_menu1 = KeyboardButton('СOЧИ') # сочи о на анг, чтобы не среагировал на обзор на сочи кнопку
# kb_menu2 = KeyboardButton('АБХАЗИЯ')
# kb_menu3 = KeyboardButton('МОРЕ')
# kb_menu4 = KeyboardButton('АКТИВ')
kb_button_individual = KeyboardButton('Индивид.')  # будут приниматься как тур, и после них сразу дата
kb_button_other = KeyboardButton('ДРУГОЕ')  # будут приниматься как тур, и после них сразу дата
# kb_menu6 = KeyboardButton('Корректировка заявки')
# kb_menu7 = KeyboardButton('Отмена заявки')
# kb_client_menu = ReplyKeyboardMarkup(resize_keyboard=True)

# kb_client_menu.row(kb_menu0)
# kb_client_menu.row(kb_menu1, kb_menu2)
# kb_client_menu.row(kb_menu3, kb_menu4)
# kb_client_menu.row(kb_menu6, kb_menu7)
# kb_client_menu.row(kb_button_individual, kb_button_other)


# # сочи
# kb_soch_var1 = KeyboardButton('Красная Поляна')
# kb_soch_var2 = KeyboardButton('Обзорная Сочи')
# kb_soch_var3 = KeyboardButton('33 Водопада')
# kb_soch_var4 = KeyboardButton('Воронцовские пещеры')
# kb_soch_var5 = KeyboardButton('Каньоны Псахо (джип-тур)')
# kb_soch_var6 = KeyboardButton('Мамонтово Ущелье (джип-тур)')
# kb_soch_var10 = KeyboardButton('Эпоха времени')
# kb_client_sochy = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client_sochy.row(kb_soch_var1, kb_soch_var2).row(kb_soch_var3, kb_soch_var10).row(kb_soch_var4).row(kb_soch_var5, kb_soch_var6)#.add(kb_soch_var9)


# # абхазия
# kb_abhaz_var1 = KeyboardButton('Золотое Кольцо')
# kb_abhaz_var2 = KeyboardButton('Абхазское застолье')
# kb_abhaz_var3 = KeyboardButton('Термальные Источники')
# kb_abhaz_var5 = KeyboardButton('Абхазский драйв (джип-тур)')
# kb_client_abhaz = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client_abhaz.row(kb_abhaz_var1).row(kb_abhaz_var2, kb_abhaz_var3).row(kb_abhaz_var5)


# # море
# kb_voda_var1 = KeyboardButton('Морская прогулка')
# kb_voda_var2 = KeyboardButton('Рыбалка в море')
# kb_voda_var7 = KeyboardButton('АРЕНДА ЯХТ')
# kb_client_voda = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client_voda.add(kb_voda_var1).add(kb_voda_var2).add(kb_voda_var7)


# # актив
# kb_vozduh_var5 = KeyboardButton('Рафтинг')
# kb_vozduh_var6 = KeyboardButton('Квадроциклы и Багги')
# kb_vozduh_var7 = KeyboardButton('Конные Прогулки')
# kb_vozduh_var8 = KeyboardButton('Солохаул Парк')
# kb_vozduh_var9 = KeyboardButton('Дайвинг')
# kb_vozduh_var1 = KeyboardButton('Параплан')

# kb_client_vozduh = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client_vozduh.row(kb_vozduh_var5, kb_vozduh_var9).row(kb_vozduh_var7, kb_vozduh_var6).row(kb_vozduh_var1).add(kb_vozduh_var8)




# --------------------

# Оставляем
# открыть меню
zz = KeyboardButton('Открыть меню')
zz_zayav = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
zz_zayav.add(zz)

# Оставляем
# поделиться контактом
b1 = KeyboardButton('Поделиться', request_contact=True)
kb_contact = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #resize_keyboard=True уменьшаем кнопки, one_time_keyboard=True одноразовая клавиатура
kb_contact.row(b1)

# сегодня зватра
kb_today = KeyboardButton('Сегодня')
kb_tomorrow = KeyboardButton('Завтра')
kb_today_tomorrow = ReplyKeyboardMarkup(resize_keyboard=True)
kb_today_tomorrow.row(kb_today, kb_tomorrow)


# сколько взрослых
sko_vz_button1 = KeyboardButton('1')
sko_vz_button2 = KeyboardButton('2')
sko_vz_button3 = KeyboardButton('3')
sko_vz_button4 = KeyboardButton('4')
sko_vz_button5 = KeyboardButton('5')

sko_vz_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sko_vz_markup.row(sko_vz_button1, sko_vz_button2, sko_vz_button3, sko_vz_button4, sko_vz_button5)


# Сколько детей с посадочным местом
pos_bes_button1 = KeyboardButton('1')
pos_bes_button2 = KeyboardButton('2')
pos_bes_button3 = KeyboardButton('3')
pos_bes_button4 = KeyboardButton('4')
pos_bes_button5 = KeyboardButton('5')
pos_bes_button0 = KeyboardButton('0')

pos_bes_markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pos_bes_markup.row(pos_bes_button0, pos_bes_button1, pos_bes_button2, pos_bes_button3, pos_bes_button4, pos_bes_button5)


# окно помощи
kb_tel = InlineKeyboardMarkup(row_width=1)
kb_t = InlineKeyboardButton(text='Если несколько, введите через пробел', callback_data='номер')
kb_tel.add(kb_t)


dop_in = InlineKeyboardMarkup(row_width=1)
kb_dop_in = InlineKeyboardButton(text='Время выезда, если есть выбор', callback_data='информация')
dop_in.add(kb_dop_in)


#подверждение
kb_ver = KeyboardButton('ВСЁ ВЕРНО')
kb_isp = KeyboardButton('ИСПРАВИТЬ')
kb_ver_isp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ver_isp.row(kb_ver, kb_isp)


# Да Нет
yes = KeyboardButton('Да')
now = KeyboardButton('Нет')
yes_now = ReplyKeyboardMarkup(resize_keyboard=True)
yes_now.row(yes, now)


# корректировать
kb_nazat = KeyboardButton('Отмена')
nazat_markup = ReplyKeyboardMarkup(resize_keyboard=True)
nazat_markup.add(kb_nazat)


# новое главное меню при корректировке
# открыть меню
kb_menu11 = KeyboardButton('СOЧИ') # сочи о на анг, чтобы не среагировал на обзор на сочи кнопку
kb_menu21 = KeyboardButton('АБХАЗИЯ')
kb_menu31 = KeyboardButton('МОРЕ')
kb_menu41 = KeyboardButton('АКТИВ')
kb_client_menu2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_menu2.row(kb_menu11, kb_menu21).row(kb_menu31, kb_menu41).row(kb_button_individual, kb_button_other)


net = KeyboardButton('Нет')
net_markup = ReplyKeyboardMarkup(resize_keyboard=True)
net_markup.add(net)