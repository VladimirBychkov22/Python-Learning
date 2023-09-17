# Объявите функцию здесь
#def print_friends_count(friends_count):
# Код, написанный ниже, переместите внутрь объявленной вами функции
    #if friends_count == 0:
        #print('У тебя нет друзей')
    #elif friends_count == 1:
        #print('У тебя', friends_count, 'друг')
    #elif friends_count >= 2 and friends_count <= 4:
        #print('У тебя', friends_count, 'друга')
    #elif friends_count >= 5 and friends_count < 20:
        #print('У тебя', friends_count, 'друзей')
    #else:
        #print('Ого, сколько у тебя друзей! Целых', friends_count)
#for friends_count in range(0, 22):
    #print_friends_count(friends_count)

#resorts = ['Сочи', 'курорты Краснодарского Края', 'Санкт-Петербург', 'Карелию']
#def choose_vacation_place(resorts):
    #for resort in resorts:
        #if resort == 'Сочи':
            #return resort
#resort = choose_vacation_place(resorts)
#print('Поехали в ' + resort)

#Програма показывающая уровни заряда.
def program_major(program):
    if program == 1:
        print('Критический уровень заряда.')
    elif program >= 2 and program <= 20:
        print("Уровень заряда низкий.")
    elif program >= 21 and program <= 49:
        print("Уровень заряда ниже среднего.")
    elif program == 50:
        print('Средний уровень заряда.')    
    elif program >= 51 and program <=  75:
        print('Уровень заряда выше среднего.')
    elif program >= 76 and program <= 99:
        print('Уровень заряда почти полный.')
    elif program == 100:
        print('Уровень заряда полный!')
    else:
        print('Erorr, tehnikal erorr.')
for program in range(0, 104):
    program_major(program)

print('Будь осторожен, ведь программа работает тогда, когда ты трудишься!')