count = 0
def check_email(email):
    required_values = ("@", ".com", ".ru", ".net")
    list_email = list(email)
    check = None
    for i in range(len(list_email)):
        if list_email[i] == required_values[0]:
            list_email.reverse()
            count_recipient = 0
            for j in range(len(list_email)):
                if list_email[j] == '.':
                    if count_recipient == 3:
                        check = list_email[j] + list_email[j - 1] + list_email[j - 2] + list_email[j - 3]
                    elif count_recipient == 2:
                        check = list_email[j] + list_email[j - 1] + list_email[j - 2]
                    break
                elif count_recipient > 3:
                    break
                else:
                    count_recipient += 1
                    continue
    if check in required_values:
        global count
        count += 1


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    global count
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        check_email(recipient)
        if count == 0:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        else:
            count = 0
        check_email(sender)
        if count == 0:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        else:
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    count = 0



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
