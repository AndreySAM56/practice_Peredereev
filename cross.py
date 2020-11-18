import random
print("""Игра 'КРЕСТИКИ-НОЛИКИ'""")
print("""Правила: Перед Вами поле, для игры "Крестики-Нолики". Вы играете крестиками (Х), компьютер ноликами (0). 
Что бы разместить крестик, вы указываете координаты, в формате "А1", т.е. сначала русскую букву обозначающую колонку,
 затем цифру обозночающую строку. Ходим по очереди. Первоочерёдность хода определяется случайным образом.  """)
pillar = ['А', 'Б', 'В', 'а', 'б', 'в']  # спсиок возможных введённых букв
lines = ['1', '2', '3']  # Список возможных введённых цифр
victory = 0;  # переменная, победы нет.
field = [[' ' for m in range(3)] for n in range(3)]  # Обозночаем пустое игровое поле
analiz = [[' ' for m in range(3)] for n in range(8)]  # Обозначаем список для анализа возможных вариантов
i, j = None, None  # обозначаем переменные для кординат столбцов и строк
StepUser = None  # Обозначаем переменную для обозначения хода игрока True или False
print(" ")
def show():
    print('      A     Б     В')
    print('   -------------------')
    for i in range(len(field)) :
        print(i+1,' | ',field[i][0],' | ',field[i][1],' | ',field[i][2],' | ')
        print('   -------------------')
        analiz[i]=field[i] # переносим первые три строки
        analiz[3][i] = field[i][0]  # из столбцов получаем списки для анализа
        analiz[4][i] = field[i][1]
        analiz[5][i] = field[i][2]
        analiz[6][i] = field[i][i]  # первая диагональ в список для анализа
        analiz[7][i] = field[2-i][i]  # вторая диагональ в список для анализа
#    print(analiz)
def InputStep(): # Функция ввода кординат
    global StepUser
    MoveCorrect = False
    while MoveCorrect == False:
        step=input('Укажите координаты Вашего хода:') # Проверяет на правильность ввода данных
        if len(step)!=2 :
            print('Количество символов должно быть два, без пробелов и знаков припинания!')
        elif step[0] not in pillar :
            print('Первый символов должно быть руской буквой А или Б или В')
        elif step[1] not in lines :
            print('Второй символов должен быть цифрой 1 или 2 или 3')
        else: MoveCorrect = True
    if step[0]=='А' or step[0]=='а': j=0  # В зависимости от введённой информации, присваивает значения индексам
    elif step[0]=='Б' or step[0]=='б': j=1
    elif step[0]=='В' or step[0]=='в': j=2
    else:
        print("какая-то ошибка. Попробуем ещё раз")
        InputStep()
    i=int(step[1])-1
    if field[i][j]==' ' :
        print("Ваш ход принят.")
        field[i][j]='X'
        StepUser=False     # Ход пользователя исчерпан
    else:
        print("Ячейка с такими координатами уже занята. Введите другие координаты")
        InputStep()
def StepComp(x,y):  # Компьютер делает ход, по координатам, которые ему передаются после анализа
    global StepUser
    if x is None and y is None:
        if field[1][1]==' ' : # В приоритете занять центральную клетку
            x,y=1,1
        else :
            x=random.randint(0,2)
            y=random.randint(0,2)
    if field[x][y]==' ': # На всякий случай проверяем не занята ли ячейка
        field[x][y]='O'
        StepUser = True
        return True  # возвращает + если всё прошло хорошо
    else: return False # возвращает - если по каким-то причинам прошло наложение.
def AnalizVictory(): # Функция проверяет, победил кто-то или нет.
    global victory
    victory=3
    for m in range(3):
        if ' ' in field[m]:
                victory=0
    for m in range(8):
        if 'O'==analiz[m][0] and analiz[m][0]==analiz[m][1] and analiz[m][1]==analiz[m][2]:
            victory=2
            print("Порадуйтесь за компьютер, он победил")
            break
        elif 'X'==analiz[m][0] and analiz[m][0]==analiz[m][1] and analiz[m][1]==analiz[m][2]:
            print("Поздравляю, Вы победили")
            victory=1
            break
    if victory==3: print("Ничья")
def Coordinates (m,n): # функция для получения координат на игровом поле
    if m in (0,1,2):
        i,j=m,n
    elif m in (3,4,5):
        j=m-3
        i=n
    elif m==6:
        i=n
        j=n
    elif m==7:
        i=2-n
        j=n
    else:
        # print('Компьютер не знает куда ему ходить')
        i,j=None,None
    return i,j
def WhereTwo(n,d,s): # функция проверки analiza на две пустые ячейки. и возврат положения O
    if analiz[n][0]==analiz[n][1] and analiz[n][0]==d and analiz[n][2]==s:
        return 2
    elif analiz[n][1]==analiz[n][2] and analiz[n][1]==d and analiz[n][0]==s:
        return 0
    elif analiz[n][0]==analiz[n][2] and analiz[n][0]==d and analiz[n][1]==s:
        return 1
    else: return 5

def Logics():
    global i, j
    m,n = None, None
    for k in range(len(analiz)) : # Перебераем analiz ищем где у компьютера стоят по два нолика
        if WhereTwo(k,'O',' ')!=5: # Функция проверяет анализ[k], есть ли два О, и где пусто
            m, n = k, WhereTwo(k,'O',' ')
            break
    if m==None : # Если не нашли два нолика, проверяем противника, т.е. ищем два крестика
        for k in range(len(analiz)):  # Перебераем analiz ищем где у соперника стоят по два крестика
            if WhereTwo(k, 'X', ' ') != 5:  # Функция проверяет анализ[k], есть ли два X, и где пусто
                m, n = k, WhereTwo(k, 'X', ' ')
                break
    if m==None and field[1][1]==' ':
        m,n=1,1
    if m==None : # Если до сих пор не определена m, значит не нашли парных крестиков или ноликов, пробуем подловить противника
        for k in range(len(analiz)): # перебираем анализ ищем где по два пустых и нолик
            if WhereTwo(k,' ','O')!=5: # если нашли такую строку,
                for t in range(len(analiz)-k-1):  # то проверям остальные и тоже ищем где две пустые и нолик
                    t=t+1 # проверка пошла со следующего после K элемента
                    if WhereTwo(t+k,' ','O')!=5:
                        for q in range(len(analiz[k])):
                            for w in range(len(analiz[t])):
                                if Coordinates(k,q)==Coordinates(t+k,w) and analiz[k][q]==' ':
                                    m,n=k,q
    if m==None : # Если до сих пор не определена m, значит не нашли парных крестиков или ноликов
        for k in range(len(analiz)-1,0,-1):  # Перебераем analiz ищем где пустые строки в обратном порядке
            # в обратном порядке для того, что бы занимать в первую очередь диагонали
            if analiz[k][0] == ' ' and analiz[k][1]==' ' and analiz[k][2] == ' ':
                m,n = k,0
                break
    if m==None : # если нет парных и пустых строк, то уже ходим в свободные пустые
        for k in range(len(analiz)):  # Перебераем analiz ищем в каких строках есть пустые ячейки
            for l in range(3):
                if analiz[k][l] == ' ':
                    m,n = k,l
                    break
    # Определились куда хотим ходить, теперь нужно m и n преобразовать в координаты игрового поля
    i,j=Coordinates(m,n)
# ИГРА
Game=True
while Game == True:
    field = [[' ' for m in range(3)] for n in range(3)]  # Обозночаем пустое игровое поле
    analiz = [[' ' for m in range(3)] for n in range(8)]  # Обозначаем список для анализа возможных вариантов
    i, j = None, None  # обозначаем переменные для кординат столбцов и строк
    StepUser = None  # Обозначаем переменную для обозначения хода игрока True или False
    show()
    print("      ЖЕЛАЕЮ УДАЧИ")
    print(" ")
    if random.random()>0.5 :  # определение первоочерёдности хода
        print("Первый ход выполняет компьютер")
        StepUser=False
    else:
        print("Первый ход выпал Вам.")
        StepUser=True
    while victory==0:
        if StepUser:
            InputStep()
        else:
            Logics()
            StepComp(i, j)
        show()
        AnalizVictory()
    str = input('Давайте сыграем ещё (Да/Любая клавиша): ').upper()
    if str != 'ДА':
        Game = False
    else: victory = 0
print("Конец игры")