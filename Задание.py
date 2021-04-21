name = ['Хлебников Глеб','Почапская Евгения','Новиков Максим','Пыльнева Елена','Золотарёв Константин','Крылова Дарья']
a = [[3,4,4,5],[5,5,5,5],[4,4,4,5],[4,4,4,5],[5,4,4,5],[2,3,4,4]]
p = ['Алгебра и аналитическая геометрия','Информатика','Физика','История']
b = 0
#1-2)СПИСОК ГРУППЫ С ОЦЕНКАМИ И СРЕД.БАЛЛ
for i in range(len(name)):
    summ = 0
    for j in range(len(a[i])):
        summ += a[i][j]
        sred = summ/4
    print(name[i],':', a[i],'Средняя оценка: ',sred)
#3)СРЕДНЯЯ ОЦЕНКА ПО ПРЕДМЕТУ
for q in range(len(a[i])):
    sr=0
    for u in range(len(a)):
        sr+=a[u][q]
    print(p[q],':',round(sr/6,2))
#4)СПИСОК НАЗНАЧЕННЫХ НА ПОВЫШЕННУЮ СТИПЕНДИЮ
print('Получают повышенную стипендию: ')
for i in range(len(name)):
    k = 0
    for j in range(len(a[i])):
        if a[i][j] == 5:
            k+=1
    if k == 4:
        print(name[i])
#5)СПИСОК НАЗНАЧЕННЫХ НА  СТИПЕНДИЮ
print('Получают стипендию:')
for i in range(len(name)):
    k = 0
    for j in range(len(a[i])):
        if (a[i][j] == 5) or (a[i][j] == 4):
            k+=1
    if k == 4:
        b+=1
print(b, 'человек(а)')
#6)СПИСОК НЕ УСПЕВАЮЩИХ
print('Не успевают по заданной дисциплине:')
for i in range(len(name)):
    k = 0
    for j in range(len(a[i])):
        if a[i][j] == 2:
            k+=1
    if k >= 1:
        print(name[i])

