import vk_api, random
from CoolProp.CoolProp import PropsSI
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# из лонг пулла импортируем нужные нам библиотеки.

token = "ваш токен"
vk = vk_api.VkApi(token=token)  # авторизация
vk._auth_token()  # в вк
longpoll = VkBotLongPoll(vk, 'ваш айди группы')  # подключение longpoll

print("Бот запущен")  # Пишем в консоль чтобы понять запущен ли бот.

while True:  # бесконечный цикл
    for event in longpoll.listen():  # прослушиваем все сообщения

        # Если пришло новое сообщение
        if event.type == VkBotEventType.MESSAGE_NEW:
            mess = event.obj['text']  # преобразуем текст сообщения в переменную
            peer_id = event.obj['peer_id']

            if mess == "Привет!":  # если текст сообщения = Привет!, отправляем сообщение.
                h_mess=PropsSI("H", "P", 101325, "T", 300, "HEOS::WATER")/1000
                vk.method("messages.send",
                          {"peer_id": peer_id, "message": f"Энтальпия = {h_mess} кДж/кг" , "random_id": random.randint(1, 2147483647)})
                # в строке выше из вк апи мы получаем метод отправки сообщения, а после указываем все нужные данные, такие как айди чата (лс/беседа), содержание отправленного ботом сообщения и рандомное айди для сообщения (а вообще я хз что это, никогда не обращал внимания).

                # Вообщем-то все. Бот готов