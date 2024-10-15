# Task  "Рассылка писем"

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    variants = ('.com', '.ru', '.net')
    if '@' not in recipient or '@' not in sender or not recipient.endswith(variants) or not sender.endswith(variants):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('lksdfjlksdfjlksdf', 'На деревню дедушке')
send_email('lksdfjlksdfjlksdf', 'Дедушке@mail.деревня')
send_email('lsdkfjslkdfjlksdjf', 'university.help@gmail.com')
send_email('lsdkfjslkdfjlksdjf', 'poluchatel.help@gmail.com')
send_email('lsdkfjslkdfjlksdjf', 'poluchatel.help@gmail.com', sender = 'Otpravitel.help@gmail.ru')
send_email('lsdkfjslkdfjlksdjf', 'poluchatel.help@gmail.com', sender = 'Otpravitel.help@gmail.gnu')