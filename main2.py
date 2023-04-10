#g = 4212, n = 22 =>
"""
 table_1 = 4 => j(i,x)
 table_2 =6 => x - y
 table_3 = 1 => 1ая форма(аналог СДНФ)
"""
import re

jFuncRegular = r"j\(\d,\w\)"
#j(i,x)
def firstTableFunc(i, xValues):
    i = int(i)
    res = [0]*len(xValues)
    for x in range(len(xValues)):
        if xValues[x] == i:
            res[x] = 1
        else:
            res[x] = 0
    return res
#вычитание по модулю k
def secondTableFucn(x,y,k,n):

    try:
        x = int(x)
        x = [x]*k
    except:
        pass
    try:
        y = int(y)
        y = [y] * k
    except:
        pass

    if type(x) == str:
        x = list(range(k))
    elif type(y) == str:
        y = list(range(k))
    xRange = k**2 if n==2 else k
    res = list(range(xRange))
    for i in range(len(x)):
        if x[i] >= y[i]:
            res[i] = x[i]-y[i]
        else:
            res[i] = x[i]-y[i]+k
    return res
#решаем чем является переменная и возвращаем ее значения
def decide(variable, n, k):
    try:
        variable = int(variable)
    except:
        pass

    res = None
    #xValues = list()
    if type(variable) == int:
        if n == 1:
            res = [variable] * k
        else:
            res = [variable] * (k**2)
    elif re.match(jFuncRegular, variable):
        if n == 2:

            if variable[-2] == 'y':
                xValues = list(range(k))*k
            else:
                xValues = list(range(k)) * k
                xValues.sort()
        else:
            xValues = list(range(k))
        res = firstTableFunc(variable[2], xValues)

    elif re.match(r"\w", variable):
        if n == 2:
            if 'y' in variable:
                xValues = list(range(k))*k
            else:
                xValues = list(range(k)) * k
                xValues.sort()
        else:
            xValues = list(range(k))
        res = xValues

    else:
        print("Dead inside xP")
        return
    return res
#СДНФ
def SDNF(funcVals, n, k):
    #значения функции закинуты списком
    out = ""
    if n ==1:
        for val in range(len(funcVals)):
            if funcVals[val] != 0:
                if funcVals[val] == (k-1):
                    out += "J({0},x) v ".format(val)
                else:
                    out += "{0}&J({1},x) v ".format(funcVals[val], val)
        out = out[:-3]
    else:
        k = int(len(funcVals)**0.5)
        yValues = list(range(k))*k
        for val in range(len(funcVals)):
            if funcVals[val] != 0:
                if funcVals[val] == (k-1):
                    out+="J({0},x)&J({1},y) v ".format(yValues[val//k], yValues[val])
                else:
                    out += "{0}&J({1},x)&J({2},y) v ".format(funcVals[val], yValues[val//k], yValues[val])
        out = out[:-3]
    print("Первая форма(аналог СДНФ):")
    print(out)
#вывод значений функции
def output(resultsList, k, n):
    if n==1:
        xValues = xValues = list(range(k))
        print("\tx\t\tf")
        for i in range(len(resultsList)):
            print("\t"+str(xValues[i])+"\t\t"+str(resultsList[i]))
            print("-"*14)
    else:
        xValues = list(range(k)) * k
        xValues.sort()

        yValues = list(range(k)) * k
        print("\tx\ty\t\tf")
        for i in range(len(resultsList)):
            print("\t"+str(xValues[i])+"\t"+str(yValues[i])+"\t\t"+str(resultsList[i]))
            print("-"*14)

def main():
    while 1:
        try:
            k = int(input('Введите значение k:\n'))
        except:
            print("Повторите ввод\n")
            continue
        else:
            break

    n = 0
    while n != 1 and n != 2:
        n = int(input('Введите количество переменных n(1 или 2)\n'))
        print(n)
    print('Введите функции, доступные в следующем списке:\n')

    print('Характеристическая фукция 1-ого рода:\t j(i,x)')
    print('Разность по модулю k:\t x-y')
    print('Константа:\t 1;2;3...;k-1')

    # исходная функция
    userFunction = input()
    userFunction = '(' + userFunction + ')'
    #список функций, входящий в исходную, разделенную знаками '-'
    userFunction = "".join(userFunction.split()).split("-")
    # print("userFunction")
    # print(userFunction)

    beginning = []
    end = 0
    subResultsList = []
    i = 0
    bracketsSubFunc = None
    #если 1 переменная
    if n == 1:
        while userFunction:
            #ищем открывающуюся скобку
            if re.match(r"\(\w", userFunction[i]) or re.match(r"\(\d", userFunction[i]):
                if len(userFunction) == 1:
                    userFunction[0] = userFunction[0][1:-1]
                    subResultsList.append(decide(userFunction[i], n, k))
                    # print("temporary subResultList is: ")
                    # print(subResultsList)
                    break
                beginning.append(i)
                #print(str(i) + " is the beginning")
            #ищем закрывающуюся скобку
            elif re.search(r"\w\)\)", userFunction[i]) or \
                    (re.match(r"\w\)", userFunction[i])) or \
                re.search(r"\d\)", userFunction[i]):
                end = i
                #(str(i) + " is the end")
                #вырезаем подфункцию
                subFunction = userFunction[beginning[-1]:end+1]
                # print("Subfunction", end = " ")
                # print(subFunction)
                #убираем скобки в начале первого аргумента и в конце последнего
                subFunction[0] = subFunction[0][1:]
                subFunction[-1] = subFunction[-1][:-1]
                # print("Subfunction without braces", end=" ")
                # print(subFunction)
                #берем первый элемент подфункции
                bracketsSubFunc = decide(subFunction[0], n, k)
                # print("Brackets subres", end=" ")
                # print(bracketsSubFunc)

                #считаем подфункцию
                for item in subFunction[1:]:
                    bracketsSubFunc = secondTableFucn(bracketsSubFunc, decide(item, n, k), k, n)
                    # print("Brackets subres", end = " ")
                    # print(bracketsSubFunc)
                #добавляем в список вычисленных подфункций
                subResultsList.append(bracketsSubFunc)
                #вырезаем подфункцию из исходной функции

                userFunction = userFunction[:beginning[-1]] + userFunction[end+1:]
                #проходим по функции снова
                beginning.pop()
                if len(userFunction) != 0:
                    if userFunction[-1][-1] != ")":
                        userFunction[-1] = userFunction[-1] + ")"
                i = 0

            i += 1

        # if len(subResultsList) == 1:
        #     print("subResultList: ")
        #     print(subResultsList)
        # else:
        finalResult = subResultsList.pop()
        for item in subResultsList:
            finalResult = secondTableFucn(finalResult, item, k, n)
        print("finalResult is: ")
        output(finalResult, k, n)
        print()
        SDNF(finalResult, n, k)
    #если 2 переменные
    elif n == 2:
        while userFunction:
            #ищем открывающуюся скобку
            if re.match(r"\(\w", userFunction[i]) or re.match(r"\(\d", userFunction[i]):
                if len(userFunction) == 1:
                    userFunction[0] = userFunction[0][1:-1]
                    subResultsList.append(decide(userFunction[i], n, k))
                    # print("temporary subResultList is: ")
                    # print(subResultsList)
                    break
                beginning.append(i)
            #ищем закрывающуюся скобку
            elif re.search(r"\w\)\)", userFunction[i]) or \
                    (re.match(r"\w\)", userFunction[i])) or \
                re.search(r"\d\)", userFunction[i]):
                end = i
                #вырезаем подфункцию
                subFunction = userFunction[beginning[-1]:end+1]
                # print("Subfunction", end = " ")
                # print(subFunction)
                #убираем скобки в начале первого аргумента и в конце последнего
                subFunction[0] = subFunction[0][1:]
                subFunction[-1] = subFunction[-1][:-1]
                # print("Subfunction without braces", end=" ")
                # print(subFunction)
                #берем первый элемент подфункции
                bracketsSubFunc = decide(subFunction[0], n, k)
                # print("Brackets subres", end=" ")
                # print(bracketsSubFunc)

                #считаем подфункцию
                for item in subFunction[1:]:
                    bracketsSubFunc = secondTableFucn(bracketsSubFunc, decide(item, n, k), k, n)
                    # print("Brackets subres", end = " ")
                    # print(bracketsSubFunc)
                #добавляем в список вычисленных подфункций
                subResultsList.append(bracketsSubFunc)
                #вырезаем подфункцию из исходной функции

                userFunction = userFunction[:beginning[-1]] + userFunction[end+1:]
                #проходим по функции снова
                beginning.pop()
                if len(userFunction) != 0:
                    if userFunction[-1][-1] != ")":
                        userFunction[-1] = userFunction[-1] + ")"
                i = 0

            i += 1

        # if len(subResultsList) == 1:
        #     print("subResultList: ")
        #     print(subResultsList)
        # else:
        finalResult = subResultsList.pop()
        for item in subResultsList:
            finalResult = secondTableFucn(finalResult, item, k, n)
        print("finalResult is: ")
        output(finalResult, k, n)
        print()
        SDNF(finalResult, n, k)

    print("Задайте множество E, для получения информации о принадлежности функции классу T(E).\nНапример: 0,1,3:")
    ESet = input()
    ESet = list(map(int, "".join(ESet.split()).split(',')))

    belongs = True
    if n == 2:
        xValues = list(range(k)) * k
        xValues.sort()

        yValues = list(range(k)) * k

        for i in range(len(xValues)):
            if xValues[i] in ESet and yValues[i] in ESet:
                if finalResult[i] not in ESet:
                    print(f'f({xValues[i]}, {yValues[i]}) = {finalResult[i]}')
                    belongs = False
                    break

    else:
        xValues = list(range(k))

        for i in range(len(xValues)):
            if xValues[i] in ESet:
                if finalResult[i] not in ESet:
                    print(f'f({xValues[i]}) = {finalResult[i]}')
                    belongs = False
                    break

    if belongs:
        print("Функция принадлежит классу функций T(E)")
    else:
        print("Функция НЕ принадлежит классу функций T(E)")

main()