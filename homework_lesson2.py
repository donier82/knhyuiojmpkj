#Задача1. Строки в python обозначаются кавычками. Приведите все способы в виде комментарий.
# 1. Одинарная кавычка.
# text= 'Это одинарная кавычка'
# print(text)
# 2. Двойная кавычка.
# text= "Это двойная кавычка" # работает так же как и одинарная кавычка
# print(text)
# 3. Тройная кавычка.
# text='''это тройная кавычка''' # тройная кавычка используется для длинных текстов 
# print(text)

#Задача2. Как применяют операции умножения к строкам?
# text='Hello'*4 #здесь n=4, значить n раз повторяет
# print(text)

#Задача3. Какие типы данных можно преобразовать в строку?
# любые данные можно преобразовать на строк. число, список, обьект, функция.

#Задача4. Опишите синтаксис срезов строк при помощи квадратных скобок.
# text='это текст примера'
# print(text[4:9]) # учитывать счет с нуля, и конце -1  

#Задача5. 
# 1.Посчитайте количество букв s и t .
#text='''Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.
# '''
# count1=text.count('s')
# count2=text.count('t')
# print(count1, count2)
# 2.Найдите все слова, которые начинаются с корня advert (регистр не должен учитываться) и превратите их все в верхний регистр
#print(text.replace('advert', 'ADVERT'))

# Задача6. Дана строка нечетной длины больше 7 символов, вернуть строку, состоящую из трех средних символов данной строки
# text='adverts'
# print(text[2:5])

#Задача7. Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой.
#Результат: "AAiddialneat"
# name1='Aidana'
# name2='Adilet'
# print(*[i + j for i, j in zip(name1, name2)], sep='')

#Задача8.Написать программу, которая будет проверять пароль...
# password=input('введите свой пароль :')
# userpassword='Donier'
# if password==userpassword:
#     print('Password is correct. You are welcome')
# else:
#     print('Password is incorrect. Please, try again') 

#Задача9. рещаемые используя условных операторов.
# temp=int(input('Введите темпаратуру за окном :'))
# if temp<-30:
#     print('Там холодно, лучше сиди дома')
# elif temp==-30 or temp<0 :
#     print('{Холодновато.Оденься потеплее')
# elif temp==0 or temp<15:
#     print('Прохладно. Куртлу накинь')
# elif temp==15 or temp<30:
#     print('Тепло. Иди гуляй в парке!')
# elif temp==30 or temp<50:
#     print('Ого. как жарко!')
# elif temp<50:
#     print('Ошибка!')

#Задача9.
# time=int(input('Введите текущего время :')) # здесь только целые число использовал исходя из задачи
# if time<0 or time>23:
#     print('Неправильно указали время')
# elif time<7:
#     print('ночь')
# elif time<13:
#     print('утро')
# elif time<18:
#     print('день')
# else:
#     print('вечер')

#доп задача
#Задача1
# assessment=int(input('Введите оценку студента :'))
# if assessment<0 or assessment>100:
#     print('не ври ...')
# elif assessment>=80:
#     print('Хорошо')
# elif assessment>=70:
#     print('Удовлетворительно')
# elif assessment>=60:
#     print('Неудовлетворительно')
# else:
#     print('Студент должен пересдать экзамен')

#Задача2
# num=int(input('Введите одно число от 1 до 12 :'))
# if num<1 or num>12:
#     print('Вы ввели неправильное число')
# elif num==1 or num==2 or num==12:
#     print('Декабрь, январь, февраль-зима')
# elif num<6:
#     print('Март, апрель, май-весна')
# elif num<9:
#     print('Июнь, июль, август-лето')
# else:
#     print('Сентябрь, октябрь, ноябрь-осень')
