#Импорт
from Task_1 import *
from Task_2 import *

#Реализация
if __name__ == "__main__":

    def exit(a):
        if a == "-1":
            return False
        else: 
            return True  
        
    def num1(t):
        
        def printPukts():
            print("\n1)Вывод на экран исходного массива\n"+
              "2)Вывод на экран интервального статистического ряда\n"+ 
              "3)Вычисление и вывод на экран числовых характеристик выборки и формул для их вычисления\n"+ 
              "4)Вывод на экран точечных оценок параметров предполагаемого нормального закона распределения а* и σ*;\n"+
              "5)Вывод на экран формулы плотности предполагаемого закона распределения (нормального) с найденными а* и σ*\n"+
              "6)Ломаная гистограммы относительных частот эмпирического интервального ряда распределения\n"+
              "7)График плотности нормального распределения с найденными а* и σ*\n"+ 
              "8)Вычисление и вывод на экран теоретических вероятностей Pi попадания значений предполагаемой нормально распределенной случайной величины в соответствующие интервалы значений X\n"+
              "9)Вычисление χ2 наблюдаемого и вывод на экран формулы для χ2набл найденное значение χ2набл\n"+
              "10)Задание уровня значимости α и вычисление числа степеней свободы с выводом на экран соответствующей формулы и полученного результата\n"+
              "11)Вывод на экран значения χ2крит, найденного по соответствующим параметрам\n"+
              "12)Сравнение χ2набл с χ2крит и вывод на экран результата проверки\n"+
              "Введите -1, если хотите выйти\n")
        
        print("\nЗАДАНИЕ 1:")
        if(t):    
            massiveX, N, W = prepareData()
            del(W)
            intervals, Ninter, Winter = prepareIntervals(massiveX, N)
        else:
            intervals, Ninter, Winter = inputIntervals()
            
        aver = averIntervals(intervals)
        a = XB(aver, Ninter)
        ob = oB(DB(aver, Ninter, a))
        Xnab = Pirson(intervals, Ninter)
        az = 0.05  #Уровень значимости
        Xkrit = getValueKritic(findFreedom(Ninter), az) #X Критическое
        printPukts()
        
        b = input("Введите номер: ")
        print()
        while(b != "-1"):
            
            printPukts()
            
            if(b == "1"):
                print(f'{massiveX = }\n{N = }')
            elif(b == "2"):
                outputTableInter(intervals, Ninter)
            elif(b == "3"):
                calcFormules(aver, Ninter)
            elif(b == "4"):
                print(f'a = {a}\nσ = {ob}')
            elif(b == "5"):
                calcFormulesNormDistrib(aver, Ninter)
            elif(b == "6"):
                drawGistagramWithLine(intervals, Winter, "Гистограмма относительных частот")
            elif(b == "7"):
                drawPlotnost(aver, Ninter)
            elif(b == "8"):
                p = P(intervals, a, ob)
                print(f'{p = }')
            elif(b == "9"):
                drawFormulPirson()
                print(f'{Xnab = }')
            elif(b == "10"):
                az = float(input("Введите уровень значимости: "))
                print(f'Степень свободы {findFreedom(Ninter)}')
            elif(b == "11"):
                print("χ2крит = ", getValueKritic(findFreedom(Ninter), az))
            elif(b == "12"):
                if(Xkrit < Xnab):
                    print("Гипотеза неверна.")
                else:
                    print("Гипотеза верна.")
                    
            b = input("Введите номер: ")
        
        print()    
        cases()
    
    def num2():
     
        def printPukts():
            print("\n1)Ввод соответствующего группированного ряда частот\n"+
              "2)Вывод на экран формул для точечных оценок неизвестных параметров распределения λ*, их вычисление и вывод их на экран\n"+ 
              "3)Вывод на экран формулы, определяющей вероятность события Р(Х = хi) в общем виде и для найденных точечных оценок и вычисление теоретических вероятностей Pi=P(X=Xi) с параметрами, равными найденным точечным оценкам\n"+ 
              "4)Многоугольник предполагаемого теоретического распределения\n"+
              "5)Полигон относительных частот\n"+
              "6)Вычисление и вывод на экран в виде продолжения исходной таблицы значений N'i = PiN, (N'i - Ni)^2, ((N'i - Ni)^2)/N'i\n"+
              "7)Вычисление χ2 наблюдаемого и вывод на экран формулы для χ2набл найденное значение χ2набл\n"+ 
              "8)Задание уровня значимости α и вычисление числа степеней свободы с выводом на экран соответствующей формулы и полученного результата\n"+
              "9)Вывод на экран значения χ2крит, найденного по соответствующим параметрам\n"+
              "Введите -1, если хотите выйти\n")
        
        print("\nЗАДАНИЕ 2:")  
        massiveX, N, W = prepareData()
        az = 0.05  #Уровень значимости
        p = calcProbability(massiveX, N)
        Xnab = Pirson2(massiveX, N)
        Xkrit = getValueKritic(findFreedom(N), az) #X Критическое
        printPukts()
        
        b = input("Введите номер: ")
        print()
        while(b != "-1"):
            
            printPukts()
            
            if(b == "1"):
                outputTable(massiveX, N)
            elif(b == "2"):
                calcFormules2(massiveX, N)
            elif(b == "3"):
                drawFormulesProbability()
                print(f'{p = }')
            elif(b == "4"):
                drawPoligonWP(massiveX, p, "Многоугольник распределения Пуассона", False)
            elif(b == "5"):
                drawPoligonWP(massiveX, W, "Полигон относительных частот")
            elif(b == "6"):
                newN(massiveX, N)
            elif(b == "7"):
                az = float(input("Введите уровень значимости: "))
                print(f'Степень свободы {findFreedom(N)}')
            elif(b == "8"):
                print("χ2крит = ", getValueKritic(findFreedom(N), az))
            elif(b == "9"):
                if(Xkrit < Xnab):
                    print("Гипотеза неверна.")
                else:
                    print("Гипотеза верна.")
                                  
            b = input("Введите номер: ")
        
        print()    
        cases()
               
    def cases():

        print("6 ЛАБОРАТОРНАЯ\n"+
              "1)Задание 1\n"+
              "2)Задание 2\n"+
              "Введите -1, если хотите выйти")

        num = input("Введите номер пункта: ")
        
        if exit(num):
            if num == "1":
                t = input("Ручной ввод 1)интервального ряда или 2)вариационного ряда: ")
                if(t == '1'):
                    num1(False)
                elif(t == '2'):
                    num1(True)
               
            elif num == "2":
                num2()
                    
    cases()
        
    
