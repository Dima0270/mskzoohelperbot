import telebot
from telebot import types
from atribute import TOKEN, questions, info_opeck, resultat, email, number_phone, admin_id
from animals import lst, list

step = 0
a, b, c, d = 0, 0, 0, 0
res_vict = None


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn_help = types.KeyboardButton('Узнать больше')
    btn_list = types.KeyboardButton('Список животных')
    btn_victorina = types.KeyboardButton('Пройти викторину')
    btn_info_opeck = types.KeyboardButton('Программа опеки')
    btn_contact = types.KeyboardButton('Контактная информация')
    markup.row(btn_victorina)
    markup.row(btn_info_opeck, btn_list)
    markup.row(btn_help,btn_contact)
    bot.send_message(message.chat.id,f'Привет, {message.chat.first_name} \nЯ bot Московского Zooпарка \nСкорее начни проходить викторину состоящую из {len(questions)} вопросов на определение твоего тотемного животного нажав на кнопку - "Пройти викторину" \nЕсли хочешь узнать что я умею нажми на кнопку - "Узнать больше"', reply_markup=markup)


@bot.message_handler(commands=['victorina'])
def victorina_srart(message):
    global step, a, b, c, d, res_vict
    step = 0
    a, b, c, d, res_vict = 0, 0, 0, 0, None
    ask_question(message, step)

@bot.message_handler(commands=['Contact'])
def сontact(message):
    bot.send_message(admin_id, f"Пользователь @{message.chat.username} \n\nРезультат викторины: \n\n{res_vict if res_vict != None else res_vict}")
    bot.send_message(message.chat.id, "Отправлен запрос на связь с сотрудником. \nВы и дальше можете пользоваться нашим ботом, пока ожидаете ответ от сотрудника")





# List animals
@bot.message_handler(commands=[f'Giraffe'])
def get_Giraffe(message):
    i = lst[0]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Northern_fur_seal'])
def get_Northern_fur_seal(message):
    i = lst[1]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Humboldti_penguin'])
def get_Humboldti_penguin(message):
    i = lst[2]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Snow_leopard'])
def get_Snow_leopard(message):
    i = lst[3]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Ratel'])
def get_Ratel(message):
    i = lst[4]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Capybara'])
def get_Capybara(message):
    i = lst[5]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Asian_rock_python'])
def get_Asian_rock_python(message):
    i = lst[6]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Odobenus_rosmarus'])
def get_Odobenus_rosmarus(message):
    i = lst[7]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Cougar'])
def get_Cougar(message):
    i = lst[8]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Domestic_bactrian_camel'])
def get_Domestic_bactrian_camel(message):
    i = lst[9]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Egyptian_rousette'])
def get_Egyptian_rousette(message):
    i = lst[10]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Boreal_owl'])
def get_Boreal_owl(message):
    i = lst[11]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Elephant'])
def get_Elephant(message):
    i = lst[12]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Lion'])
def get_Lion(message):
    i = lst[13]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Red_panda'])
def get_Red_panda(message):
    i = lst[14]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Eastern_hedgehog'])
def get_Eastern_hedgehog(message):
    i = lst[15]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Fennec_Fox'])
def get_Fennec_Fox(message):
    i = lst[16]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Dikdik'])
def get_Dikdik(message):
    i = lst[17]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Meerkat'])
def get_Dikdik(message):
    i = lst[18]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])


@bot.message_handler(commands=[f'Alpaca'])
def get_Alpaca(message):
    i = lst[19]
    bot.send_photo(message.chat.id, photo=i[1])
    bot.send_message(message.chat.id, i[0])



def ask_question(message, step):
    if step == len(questions):
        result(message)
    else:
        question = questions[step][0]
        markup = types.InlineKeyboardMarkup()
        btn_1 = types.InlineKeyboardButton(f"a", callback_data='option1')
        btn_2 = types.InlineKeyboardButton(f"b", callback_data='option2')
        btn_3 = types.InlineKeyboardButton(f"c", callback_data='option3')
        btn_4 = types.InlineKeyboardButton(f"d", callback_data='option4')
        markup.row(btn_1, btn_2)
        markup.row(btn_3, btn_4)
        bot.send_message(message.chat.id, f"Вопрос №{step + 1} \n{question}", reply_markup=markup)

def result(message):
    global a, b, c, d, res_vict
    markup = types.ReplyKeyboardMarkup()
    btn_list = types.KeyboardButton('Список животных')
    btn_info_opeck = types.KeyboardButton('Программа опеки')
    btn_victorina = types.KeyboardButton('Пройти викторину заново')
    btn_menu = types.KeyboardButton('Главное меню')
    btn_contact = types.KeyboardButton('Контактная информация')
    btn_rep = types.KeyboardButton('Поделиться результатом викторины')
    markup.row(btn_list)
    markup.row(btn_info_opeck)
    markup.row(btn_rep)
    markup.row(btn_contact)
    markup.row(btn_victorina, btn_menu)
    maximum = max(a, b, c, d)
    bot.send_message(message.chat.id, "Результат викторины")
    if a == maximum:
        bot.send_message(message.chat.id, resultat[0][0])
        bot.send_message(message.chat.id, resultat[0][1])
        res_vict = f"{resultat[0][0]} \n{resultat[0][1]}"
    elif b == maximum:
        bot.send_message(message.chat.id, resultat[1][0])
        bot.send_message(message.chat.id, resultat[1][1])
        res_vict = f"{resultat[1][0]} \n{resultat[1][1]}"
    elif c == maximum:
        bot.send_message(message.chat.id, resultat[2][0])
        bot.send_message(message.chat.id, resultat[2][1])
        res_vict = f"{resultat[2][0]} \n{resultat[2][1]}"
    elif d == maximum:
        bot.send_message(message.chat.id, resultat[3][0])
        bot.send_message(message.chat.id, resultat[3][1])
        res_vict = f"{resultat[3][0]} \n{resultat[3][1]}"
    bot.send_message(message.chat.id, 'В нашем Zooпарке действует программа опеки, благодоря ей вы можете стаст опекуном любого животного который входит в программу опеки.\n Посмотреть список животных можно нажав на кнопку "Список животных", а узнать больше о программе опекунства можно нажав на кнопку - "Программа опеки"', reply_markup=markup)

# Option
@bot.callback_query_handler(func=lambda callback: callback.data == "option1")
def get_option1(callback):
    global step, a
    a += 1
    step += 1
    ask_question(callback.message, step)
    bot.answer_callback_query(callback.id, "Ответ обрабатывается. Пожалуйста подождите")


@bot.callback_query_handler(func=lambda callback: callback.data == "option2")
def get_option2(callback):
    global step, b
    b += 1
    step += 1
    ask_question(callback.message, step)
    bot.answer_callback_query(callback.id, "Ответ обрабатывается. Пожалуйста подождите")


@bot.callback_query_handler(func=lambda callback: callback.data == "option3")
def get_option3(callback):
    global step, c
    c += 1
    step += 1
    ask_question(callback.message, step)
    bot.answer_callback_query(callback.id, "Ответ обрабатывается. Пожалуйста подождите")


@bot.callback_query_handler(func=lambda callback: callback.data == "option4")
def get_option4(callback):
    global step, d
    d += 1
    step += 1
    ask_question(callback.message, step)
    bot.answer_callback_query(callback.id, "Ответ обрабатывается. Пожалуйста подождите")





@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == "Пройти викторину" or message.text == "Пройти викторину заново":
        markup = types.ReplyKeyboardMarkup()
        btn_victorina = types.KeyboardButton('Пройти викторину заново')
        btn_menu = types.KeyboardButton('Главное меню')
        markup.row(btn_victorina)
        markup.row(btn_menu)
        bot.send_message(message.chat.id,"Викторина начинается", reply_markup=markup)
        victorina_srart(message)
    elif message.text == 'Программа опеки':
        bot.send_message(message.chat.id, info_opeck)
    elif message.text == 'Главное меню':
        print(message.chat.id)
        markup = types.ReplyKeyboardMarkup()
        btn_help = types.KeyboardButton('Узнать больше')
        btn_list = types.KeyboardButton('Список животных')
        btn_victorina = types.KeyboardButton('Пройти викторину')
        btn_info_opeck = types.KeyboardButton('Программа опеки')
        btn_contact = types.KeyboardButton('Контактная информация')
        markup.row(btn_victorina)
        markup.row(btn_info_opeck, btn_list)
        markup.row(btn_help, btn_contact)
        if res_vict != None:
            btn_res_vic = types.KeyboardButton("Поделиться результатом викторины")
            markup.row(btn_res_vic)
        bot.send_message(message.chat.id,f'"Пройти викторину" - Если хочешь пройти викторину \n\n"Программа опеки" - Подробнее узнать о программе опеки \n\n"Список животных" - Увидеть список животных входящие в программу опеки \n\n"Контактная информация" - Так можно связаться с нами если возникли вопросы  \n\nХочешь отправить обратную связь то смело можешь писать в сообщение"', reply_markup=markup)
    elif message.text == 'Узнать больше':
        bot.send_message(message.chat.id,f'"Пройти викторину" - Если хочешь пройти викторину \n"Программа опеки" - Подробнее узнать о программе опеки \n"Список животных" - Увидеть список животных входящие в программу опеки \n"Контактная информация" - Так можно связаться с нами если возникли вопросы  \nХочешь отправить обратную связь то смело можешь писать в сообщение"')
    elif message.text == 'Список животных':
        markup = types.ReplyKeyboardMarkup()
        btn_list = types.KeyboardButton('Список животных')
        btn_menu = types.KeyboardButton('Главное меню')
        markup.row(btn_list)
        markup.row(btn_menu)
        bot.send_message(message.chat.id,"Список животных которых можно взять под опеку",reply_markup=markup)
        for i in list:
            bot.send_message(message.chat.id, f"{i[0]} - /{i[1]}")
    elif message.text == 'Контактная информация':
        bot.send_message(message.chat.id,f"Наши контактные данные \nЭлектронная почта {email}, \nНомер телефона {number_phone} \nСвязь с сотрудником /Contact")
    elif message.text == 'Поделиться результатом викторины':
        text = f"Привет, приглашаю тебя пройти викторину на определение тотемного животного.\nВот мой результат: \n{res_vict.split("\n")[0]}, тебе подходят такие животные как..."#res_vict.split("\n")[0]
        markup = types.InlineKeyboardMarkup()
        btn_link = types.InlineKeyboardButton("Поделиться в Telegram", url=f"https://t.me/share/url?url=https%3A%2F%2Ft.me%2Fmskzoohelperbot%2F \n{text}")
        markup.row(btn_link)
        bot.send_message(message.chat.id,"Поделиться в Telegram ", reply_markup=markup )
    else:
        bot.send_message(admin_id,f"Пользователь @{message.chat.username} \n\nОставил обратную связь: \n\n{message.text}")
        bot.send_message(message.chat.id,"Спасибо за обратную связь, она уже отправлена сотруднику")


bot.polling()
