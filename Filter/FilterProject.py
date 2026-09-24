bannedWords = ['выиграли', 'скидка', 'ссылке', 'депозит', 'приза', 'бесплатная', 'обнаружили', 'бесплатного', 'бесплатных', 'оплатите', 'долларов', 'работать из дома', 'акція', 'скидкой', 'пароль', 'won',
               'распродажа', 'доход', 'приз', 'бесплатно', 'cvv',
               'бонус']

with open('emails.txt', 'r', encoding='utf-8') as file:
    allEmails = file.read().split('/')

with open('normal.txt', 'w', encoding='utf-8') as normal, \
     open('senders.txt', 'w', encoding='utf-8') as senders:

    for email in allEmails:
        if any(word in email.lower() for word in bannedWords):
            for line in email.split('\n'):
                if 'from:' in line.lower():
                    senders.write(line.split(':')[1].strip() + '\n')
        else:
            normal.write(email + '/')

with open ('BannedWords.txt', 'w', encoding='utf-8') as banned:
    for words in bannedWords:
        banned.write(words + '\n')