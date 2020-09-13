import telebot
import random



bot = telebot.TeleBot('1138493895:AAHT3-TJ8I3ypcNwqm2ug3fN56hcZ46bHZQ')

stickers = ['🎁', '💳', '💰', '💎', '👨🏻‍🔬', '👨🏻‍🌾', ' 💴', '⬆️']
money = [500]
btk = [0]
click_one = [1]



@bot.message_handler(commands=['start', 'menu'])
def main(message):
    keyboard_main = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_main.row('/баланс💳', '/казино💎', '/бонус🎁', '/фермаБТК👨🏻‍🌾')

    bot.send_message(message.chat.id, f'Хэй это 💎<b>Diamond casino</b>💎\nхочешь испытать удачу?💰\nтогда тебе к нам!', parse_mode='html', reply_markup=keyboard_main)
    bot.send_message(message.chat.id, f'Что бы вернутся в главное меню напиши <b>/menu</b>', parse_mode='html')

@bot.message_handler(commands=['баланс💳'])
def balance(message):


    bot.send_message(message.chat.id, '💳Ваш баланс - ' + str(money[0]) + 'Руб 💳\n💳Ваш баланс - ' + str(btk[0]) + 'БТК 💳')


@bot.message_handler(commands=['казино💎'])
def casino(message):
    keyboard_casino = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_casino.row('/Крутить', '/menu')
    x = random.randint(50, 500)

    bot.send_message(message.chat.id, 'Прокрутка будет стоить 50Руб\nу вас ' + str(money[0]) + 'Руб', reply_markup=keyboard_casino, parse_mode='html' )




@bot.message_handler(commands=['Крутить'])
def casino_logic(message):
    keyboard_casino = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_casino.row('/Крутить', '/menu')


    x = random.randint(10, 150)
    if money[0] >= 50:
        money[0] -= 50
        bot.send_message(message.chat.id, f'💳' + '<b>Ваш выйграш! - </b>' + str(x) + 'Руб', reply_markup=keyboard_casino, parse_mode='html')
        money[0] += x
        bot.send_message(message.chat.id, f'💳Ваш баланс ' + str(money[0]) )
    else:
        bot.send_message(message.chat.id, 'У вас недостаточно средств')


@bot.message_handler(commands=['бонус'])
def bonus(message):
    bot.send_message(message.chat.id, f'<b>В разработке!👨🏻‍🔬</b>', parse_mode='html')


@bot.message_handler(commands=['фермаБТК👨🏻‍🌾'])
def ferm(message):
    keyboard_ferma = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_ferma.row('/кликать💰', '/улучшить', '/menu')

    bot.send_message(message.chat.id, f'💰<b>Ферма биткоина</b>💰\nкликай и зарабатывай биткоин💰 потом обменяй в <b>рубли</b> 💴', reply_markup=keyboard_ferma, parse_mode='html')


@bot.message_handler(commands=['кликать💰'])
def click(message):
    keyboard_click = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_click.row('/клик💰')

    bot.send_message(message.chat.id, '<b>Баланс </b>' + str(btk[0]), parse_mode='html', reply_markup=keyboard_click)


@bot.message_handler(commands=['клик💰'])
def clickk(message):
    keyboard_click = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_click.row('/клик💰', '/menu')

    btk[0] += click_one[0]

    bot.send_message(message.chat.id, '<b>💳Баланс </b>' + '<b>' + str(btk[0]) + ' БТК</b>' + '\nБТК в клик ' + str(click_one[0]), parse_mode='html', reply_markup=keyboard_click)


@bot.message_handler(commands=['улучшить'])
def custom(message):
    keyboard_custum = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_custum.row('/Клик⬆️', '/menu')

    bot.send_message(message.chat.id, 'Повысить уровень клика\nваш уровень клика ' + str(click_one[0]) + '\nповышение уровня клика стоит 10 БТК', reply_markup=keyboard_custum)


@bot.message_handler(commands=['Клик⬆️'])
def click_castom(message):
    keyboard_custum = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard_custum.row('/Клик⬆️', '/menu')

    if click_one[0] == 1:
        if btk[0] >= 10:
            click_one.remove(1)
            level_2 = 2
            click_one.append(level_2)
            btk[0] -= 10
            bot.send_message(message.chat.id, 'Ваш уровень повышен')
        else:
            bot.send_message(message.chat.id, 'У вас не хватает БТК')
    elif click_one[0] == 2:
        if btk[0] >= 20:
            click_one.remove(2)
            level_3 = 3
            click_one.append(level_3)
            btk[0] -= 20
            bot.send_message(message.chat.id, 'Ваш уровень повышен')
        else:
            bot.send_message(message.chat.id, 'У вас не хватает БТК')
    elif click_one[0] == 3:
        if btk[0] >= 30:
            click_one.remove(3)
            level_4 = 4
            click_one.append(level_4)
            btk[0] -= 30
            bot.send_message(message.chat.id, 'Ваш уровень повышен')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    elif click_one[0] == 4:
        if btk[0] >= 40:
            click_one.remove(4)
            level_5 = 5
            click_one.append(level_5)
            btk[0] -= 40
            bot.send_message(message.chat.id, 'Уровень повышен')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    elif click_one[0] == 5:
        if btk[0] >= 50:
            click_one.remove(5)
            level_6 = 6
            click_one.append(level_6)
            btk[0] -= 50
            bot.send_message(message.chat.id, 'Уровень повышен')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    elif click_one[0] == 6:
        if btk[0] >= 60:
            click_one.remove(6)
            level_7 = 7
            click_one.append(level_7)
            btk[0] -= 60
            bot.send_message(message.chat.id, 'Уровень повышен')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    elif click_one[0] == 7:
        if btk[0] >= 70:
            click_one.remove(7)
            level_8 = 8
            click_one.append(level_8)
            btk[0] -= 70
            bot.send_message(message.chat.id, 'Уроовень повышен')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    elif click_one[0] == 8:
        if btk[0] >= 80:
            click_one.remove(8)
            level_9 = 9
            click_one.append(level_9)
            btk[0] -= 80
            bot.send_message(message.chat.id, 'Ваш уровень повышен')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    elif click_one[0] == 9:
        if btk[0] >= 90:
            click_one.remove(9)
            level_10 = 10
            click_one.append(level_10)
            btk[0] -= 90
            bot.send_message(message.chat.id, 'Вы повысели уровень')
        else:
            bot.send_message(message.chat.id, 'Не хватает БТК!')
    else:
        bot.send_message(message.chat.id, 'Вы достигли максимум уровня\n<b>10</b>', parse_mode='html')







bot.polling()
