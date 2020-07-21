expression = input("Введите выражение: ")
def control_symbol_allowance(x):
    """Проверяем строку на допустимые символы чисел и знаков"""
    for i in x:
        allow_flag = True
        if i.isdigit() or i == "+" or i == "-" or i == "/" or i == "*" or i == "." or i == " " or i == "(" or i == ")": #пока не беру комплексные числа и допускаю только 4 действия и пробелы
            pass
        else:
            allow_flag = False
            print("Ошибка ввода! Введите только числа и знаки действий")
            break
    return allow_flag
def get_start_list(x):
    """Создаем список в котором сохраним последовательность знаков как в строке но разобьем числа и знаки действий отдельно"""
    if control_symbol_allowance(x):
        items = x
        element = ""
        items2 = [] # будующий готовый список с разбитыми числами и знаками в отдельные элементы списка
        for i in items:
            for j in i:
                if j.isdigit() or j == ".":
                    element += j
                elif j == "+" or j == "-" or j == "*" or j == "/" or j == "(" or j == ")":
                    items2.append(element)
                    items2.append(j)
                    element = ""
        items2.append(element)
    for i in items2:
        if i == "":
            items2.remove("")
    print(items2)
    return items2
def get_negative_numbers(x): #недопиленная фича, хуй пойми почему не работет, нужно пофиксить!
    for i in x:
        if i == "-":
            if x[x.index(i) + 1].isdigit():
                if "." in x[x.index(i) + 1]:
                    x[x.index(i) + 1] = str(float(x[x.index(i) + 1]) * (-1))
                    x[x.index(i)] = "+"
                    if x.index(i) != 0:
                        if x[x.index(i) - 1] == "(" and x[x.index(i) + 2] == ")":
                            x.pop(x.index(i) - 1)
                            x.pop(x.index(i) + 1)
                else:
                    x[x.index(i) + 1] = str(int(x[x.index(i) + 1]) * (-1))
                    x[x.index(i)] = "+"
                    if x.index(i) != 0:
                        if x[x.index(i) - 1] == "(" and x[x.index(i) + 2] == ")":
                            x.pop(x.index(i) - 1)
                            x.pop(x.index(i) + 1)
    return x # # #
def start_end_check(x):
    """Проверка списка на положение в начале и в конце знаков действий и точки"""
    allow_flag = True
    if x[0] != "+" and x[0] != "/" and x[0] != "*" and x[0] != "." and x[-1] != "+" and x[-1] != "/" and x[-1] != "*" and x[-1] != "." and x[-1] != "-":
        allow_flag = True
    else:
        allow_flag = False
        print("Ошибка ввода! Не используйте знаки действий в начале и конце выражения, в начале выражение может быть использован знак '-' ")
    return allow_flag
def using_0_check(x):
    """Проверка списка на неправильное употребление 0"""
    allow_flag == True
    for i in x:
        if len(i) > 1:
            if i[0] == "0":
                if i[1] == ".":
                    if len(i) > 2:
                        if i[2].isdigit:
                            allow_flag = True
                        else:
                            print("Ошибка ввода! Неправильно введена дробная часть!")
                            allow_flag = False
                            break
                    else:
                        print("Ошибка ввода! Не введена дробная чать!")
                        allow_flag = False
                        break
                else:
                    print("Ошибка ввода! Вводите 0 только в начало дробных чисел, где за одним нулем следует точка, а затем дробная часть")
                    allow_flag = False
                    break
    return allow_flag
def using_action_check(x):
    """Проверка на использование нескольких знаков действий подряд"""
    allow_flag = True
    for i in x:
        if i == "+" or i == "-" or i == "/" or i == "*" or i == ".":
            if x[x.index(i) + 1] == "+" or x[x.index(i) + 1] == "-" or x[x.index(i) + 1] == "/" or x[x.index(i) + 1] == "*" or x[x.index(i) + 1] == ".":
                print("Ошибка ввода! Не вводите несколько знаков подряд!")
                allow_flag = False
                break
    return allow_flag
def using_point_check(x):
    """Проверяем правильность использования точек"""
    allow_flag = True
    for i in x:
        if i[0] == "." or i[-1] -- ".":
            print("Ошибка ввода! Не используйте точки в начале и конце чисел!")
            allow_flag = False
            break
    return allow_flag
def control_logic_allowance(x):
    """Проверка на правильность употребления знаков в выражении"""
    flag1 = start_end_check(x)
    flag2 = using_0_check(x)
    flag3 = using_action_check(x)
    flag4 = using_point_check(x)
    return flag1 and flag2 and flag3 and flag4
def DoingMultiplicationAndDivision(list):
    """Выполняет умножение и деление"""
    while "*" in list or "/" in list:
        for i in list:
            c = list.index(i)
            if i == "*":
                if "." in list[c - 1] or list[c + 1]:
                    list[c] = str(float(list[c - 1]) * float(list[c + 1]))
                    list.pop(c - 1)
                    list.pop(c)
                else:
                    list[c] = str(int(list[c - 1]) * int(list[c + 1]))
                    list.pop(c - 1)
                    list.pop(c)
            if i == "/":
                if "." in list[c - 1] or list[c + 1]:
                    list[c] = str(float(list[c - 1]) / float(list[c + 1]))
                    list.pop(c - 1)
                    list.pop(c)
                else:
                    list[c] = str(int(list[c - 1]) / int(list[c + 1]))
                    list.pop(c - 1)
                    list.pop(c)
    return list
def DoingSumAndSubtraction(list):
    """Выполняет сложение и вычитание"""
    if "." in list[0]:
        d = float(list[0])
    else:
        d = int(list[0])
    for i in range(len(list) - 1):
        k = list[i + 1]
        if list[i] == "+":
            if "." in k:
                d += float(k)
            else:
                d += int(k)
        if list[i] == "-":
            if "." in k:
                d -= float(k)
            else:
                d -= int(k)
    return d
print(GetList(expression))
