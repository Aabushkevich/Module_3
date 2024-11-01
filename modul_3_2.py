
def send_email(message,recipient, sender="university.help@gmail.com") :

    a = ['@', '.com','.ru','.net']

    for a in recipient, sender:
        if a not in recipient  or a not in sender :  # Не получается настроить первое условие,из-за чего не срабатывают  условия 3 и 4. Думаю, что цикл неправильно считывает значения из списка...или список был не лучшим решением)))
            print("Невозможно отправить письмо с адреса " + sender + " на адрес " +  recipient)
            break

        if recipient == sender :
            print("Нельзя отправить письмо самому себе!")
            break

        if sender  :
            print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient)
            break

        else :
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо  отправлено с адреса " + sender + " на адрес " + recipient)


send_email('Это сообщение для проверки связи','vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса','urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание','urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре','urban.teacher@mail.ru', sender='urban.teacher@mail.ru')