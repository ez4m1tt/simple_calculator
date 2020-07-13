expression = input("Введите выражение: ")
def GetWorkingData(a):
    """Подготовка списка для произведения вычислений"""
    a = a.split(" ")
    items2 = []
    element = ''
    mistake_flag = False
    for i in a:
        if mistake_flag:
            break
        else:
            for j in i:
                if j.isdigit() or j == ".":
                    element += j
                elif j == "+" or j == "-" or j == "*" or j == "/":
                    if element[0] != "0" or (element[1] == "." and element[0] == "0"):
                        items2.append(element)
                        items2.append(j)
                        element = ""
                    else:
                        print("Ошибка ввода. Не вводите нули в начало целых чисел и вводите только один ноль в начало дробных")
                        mistake_flag = True
                        break
                else:
                    print("Ошибка ввода. Введите только числа и знаки выражений!")
                    mistake_flag = True
                    break
    if element[0] != "0" or (element[1] == "." and element[0] == "0"):
        items2.append(element)
    else:
        if not mistake_flag:
            print("Ошибка ввода. Не вводите нули в начало целых чисел и вводите только один ноль в начало дробных")
    return items2
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
print(DoingSumAndSubtraction(DoingMultiplicationAndDivision(GetWorkingData(expression))))