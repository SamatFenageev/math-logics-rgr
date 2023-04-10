#g = 4212, n = 22 =>
"""
 table_1 = 4 => j(i,x)
 table_2 =6 => x - y
 table_3 = 1 => 1ая форма(аналог СДНФ)
"""
import re
def firstTableFunc(i, xValues):
    i = int(i)
    res = [0]*len(xValues)
    for x in range(len(xValues)):
        if xValues[x] == i:
            res[x] = 1
        else:
            res[x] = 0
    return res

def secondTableFucn(x,y,k,n):
    #если один из них инт -> передавай его в виде [x]*k
    xRange = k**2 if n==2 else k
    res = list(range(xRange))
    for i in range(len(x)):
        if x[i] >= y[i]:
            res[i] = x[i]-y[i]
        else:
            res[i] = x[i]-y[i]+k
    return res
def SDNF(funcVals):
    #значения функции закинуты списком
    out = ""
    for val in range(len(funcVals)):
        if funcVals[val] != 0:
            out += "{0}&J{1}(x)v".format(funcVals[val], val)
            out = out[:-1]
    print(out)
#(3x)-j2(x)
    ##p = 5
#(2x-j4(x))-j2(x)
def main():
    while 1:
        try:
            k = int(input('Введите значение k:\n'))
        except:
            print("Повторите ввод\n")
            continue
        else: break
    openBracketIndex = 0
    closedBracketIndex = 0
    n = 0
    while n != 1 and n != 2:
        n = int(input('Введите количество переменных n(1 или 2)\n'))
        print(n)
    print('Введите функции, доступные в следующем списке:\n')
    
    print('Характеристическая фукция 1-ого рода:\t j(i,x)')
    print('Разность по модулю k:\t x-y')
    print('Константа:\t 1;2;3...;k-1')

    #исходная функция
    userFunction = input()

    userFunction = "".join(userFunction.split())


    if n == 1:
        xValues = list(range(k))

        #регулярка для характеристической фукции 1-ого рода
        jFuncRegular = r'\d,(\w*|\d*)'

        #j(2,x) -> 2,x -> r'\d,\w' - subFunction
        #funcItself -> j(j(2,x)-x)
            # (2,x)
            # (j-x)
            # (j-x)
            #  ''
        #регулярка для разности по модулю к
        #subFuncRegular = r'(j\(\d,\w*\d*\)-j\(\d,\w*\d*\)|(j\(\d,\w*\d*\)-\w*\d*)|(\w*\d*-j\(\d,\w*\d*\))|(\w-\w))'
        #                                  две j              | j и пер/конст | пер/конст и j |   2 пер или 2 конст
        #subFuncRegular = r'(j\(\d,(\w*|\d*)\)-j\(\d,(\w*|\d*)\))|(j-(\w*|\d*))|((\w*|\d*)-j)|((\w*|\d*)-(\w*|\d*))'
        #subFuncRegular = r'(j-j\(\d,\w*\d*\))|(j-(\w*|\d*)\))|((\w*|\d*)\)-(\w*|\d*)\))|((\w*|\d*)\)-j)'
        subFuncRegular = r'(j-j)|(j-(\d|\w))|((\d|\w)-j)'


        """
        j = re.search(jFuncRegular, userFunction)
        sub = re.search(subFuncRegular, userFunction)
        for i in range(len(userFunction)):
            #есть разность
            if sub:
                #есть j
                if 'j' in sub.group():
                    if sub.group().count('j') == 2:
                        subjFunc1 = firstTableFunc(sub.group()[2], xValues)
                        subjFunc2 = firstTableFunc(sub.group()[-4], xValues)
                        subRes = secondTableFucn(subjFunc1, subjFunc2, k, n)
                    elif sub.group()[0] == 'j':
                        subjFunc1 = firstTableFunc(sub.group()[2], xValues)
                        contValues = [int(sub.group()[-1])]*k
                        subRes = secondTableFucn(subjFunc1, contValues, k, n)
                    else:
                        subjFunc1 = firstTableFunc(sub.group()[-4], xValues)
                        constValues = [int(sub.group()[0])]*k
                        subRes = secondTableFucn(constValues, subjFunc1, k, n)
                    print(subRes)
                    # subjFunc1 = firstTableFunc(sub.group()[sub.group().find('j')+2], xValues)
                    # print(subjFunc1)
                #есть переменная/ые нету j
                elif re.search(r'\w', sub.group()):
                    if sub.group()[0] == sub.group[-1]:
                        subRes = [0]*k
                    elif re.match(r'\w', sub.group()[0]):
                        constValues = [int(sub.group()[-1])]*k
                        subRes = secondTableFucn(xValues, constValues, k, n)
                    else:
                        constValues = [int(sub.group()[0])]*k
                        subRes = secondTableFucn(constValues, xValues, k, n)
                #только константы
                else:
                    constValues1 = [int(sub.group()[0])] * k
                    constValues2 = [int(sub.group()[-1])] * k
                    subRes = secondTableFucn(constValues1, constValues2, k, n)
            #есть j, нету разности
            elif j:
                subRes = firstTableFunc(j.group()[2], xValues)
        """
        i = 0
        #будем записывать текущее значение функции
        subRes = [item for item in xValues]
        while userFunction:
            #####################попробуй через re<---------------------
            if userFunction[i] == "(":
                openBracketIndex = i
            elif userFunction[i] == ")":
                closedBracketIndex = i

                #извлекаем подфункцию
                subFunc = userFunction[openBracketIndex+1:closedBracketIndex]

                j = re.search(jFuncRegular, subFunc)
                sub = re.search(subFuncRegular, subFunc)

                # есть разность
                if j:
                    subRes = firstTableFunc(j.group()[0], xValues)
                    openBracketIndex -= 1
                    print(subRes)

                elif sub:
                    # есть j
                    if 'j' in sub.group():
                        if sub.group().count('j') == 2:
                            subjFunc1 = firstTableFunc(sub.group()[2], xValues)
                            subjFunc2 = firstTableFunc(sub.group()[-4], xValues)
                            subRes = secondTableFucn(subjFunc1, subjFunc2, k, n)
                        elif sub.group()[0] == 'j':
                            subjFunc1 = firstTableFunc(sub.group()[2], xValues)
                            contValues = [int(sub.group()[-1])] * k
                            subRes = secondTableFucn(subjFunc1, contValues, k, n)
                        else:
                            subjFunc1 = firstTableFunc(sub.group()[-4], xValues)
                            constValues = [int(sub.group()[0])] * k
                            subRes = secondTableFucn(constValues, subjFunc1, k, n)
                        print(subRes)
                    elif re.search(r'\w', sub.group()):
                        if sub.group()[0] == sub.group[-1]:
                            subRes = [0] * k
                        elif re.match(r'\w', sub.group()[0]):
                            constValues = [int(sub.group()[-1])] * k
                            subRes = secondTableFucn(xValues, constValues, k, n)
                        else:
                            constValues = [int(sub.group()[0])] * k
                            subRes = secondTableFucn(constValues, xValues, k, n)
                        # только константы
                    else:
                        constValues1 = [int(sub.group()[0])] * k
                        constValues2 = [int(sub.group()[-1])] * k
                        subRes = secondTableFucn(constValues1, constValues2, k, n)
                #вырезаем подфункию из основной
                userFunction = userFunction[:openBracketIndex] + userFunction[closedBracketIndex+1:]

                print(subFunc)
                print(userFunction)
                i = 0
                continue
            i += 1
    else:
        pass
while 1:
    main()
