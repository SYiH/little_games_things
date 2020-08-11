import random, sys
while True: 
    while True:
        b=('камень','ножницы','бумага')
        usr=input('Камень, ножницы или бумага? Для выхода: "Выход" ')
        usr=usr.lower()
        if usr=='выход':
            sys.exit()
        elif usr.isalpha()==False:
            print('Неверное значение, попробуйте снова.')
        elif usr not in b:
            print('Неверное значение, попробуйте снова.')
        else:
            break

    pc=random.choice(b)
    usr=usr.capitalize()
    pc=pc.capitalize()

    if pc==usr:
        print('Ничья')

    elif usr=='Ножницы' and pc=='Бумага': #Ножницы и бумага
        print(
            'Ваш ответ: ',usr,',',
            'Ответ компьютера: ',pc,',',
            'Вы победили!'
            )
    elif usr=='Бумага' and pc=='Ножницы': #Ножницы и бумага
        print(
            'Ваш ответ: ',usr,',',
            'Ответ компьютера: ',pc,',',
            'Компьютер победил!'
            )

    elif usr=='Камень' and pc=='Ножницы': #Ножницы и камень
        print(
            'Ваш ответ: ',usr,',',
            'Ответ компьютера: ',pc,',',
            'Вы победили!'
            )
    elif usr=='Ножницы' and pc=='Камень': #Ножницы и камень
        print(
            'Ваш ответ: ',usr,',',
            'Ответ компьютера: ',pc,',',
            'Компьютер победил!'
            )

    elif usr=='Камень' and pc=='Бумага': #Камень и бумага
        print(
            'Ваш ответ: ',usr,',',
            'Ответ компьютера: ',pc,',',
            'Компьютер победил!'
            )
    elif usr=='Бумага' and pc=='Камень': #Камень и бумага
        print(
            'Ваш ответ: ',usr,',',
            'Ответ компьютера: ',pc,',',
            'Вы победили!'
            )
#else:
#    while True:
#        print('FATAL ERROR, DESTRUCTING PC')
