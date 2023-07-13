from config import *
from tabulate import tabulate
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import integrate

def prepareData() -> tuple:
    '''Сборка и подготовка данных'''

    def enterArrayN() -> tuple:
        '''Ввод массива'''
        inputArr = []
        N = []
        a = int(input("Введите длину ряда: "))
        
        for _ in range(a):
            inputArr.append(float(input("Введите элемент ряда: ")))
            N.append(float(input("Введите n: ")))
            
        for _ in range(len(inputArr)):
            
            for _2 in range(len(inputArr)):
                
                if(inputArr[_] < inputArr[_2]):
                    buf = inputArr[_]
                    inputArr[_] = inputArr[_2]
                    inputArr[_2] = buf

                    buf = N[_]
                    N[_] = N[_2]
                    N[_2] = buf

                    
            
        return (inputArr, N);    
            
    massive, N = enterArrayN() #Получаем данные
    countN = sum(N) #Количество чисел
    W = list(map(lambda x: x/countN, N))
    return (massive, N, W)

def outputTable(massiveX:list, NW:list, type:str = "Xi", type2:str = "Ni") -> None:
    '''Вывод вариционного ряда'''
    
    massiveXg = massiveX.copy()
    massiveXg.insert(0,type)
    NWg = NW.copy()
    NWg.insert(0, type2)
    unit = (massiveXg,NWg)
    
    print(tabulate(unit, tablefmt="rounded_grid", stralign='center'))
    
def outputTableInter(intervals:list, NWinter:list, type:str = "Ni") -> None:
    """Вывод таблицы интервалов"""
    stringer = []
    for s in intervals:
        stringer.append(str(s).replace('[', '').replace(']', '').replace(', ', ';'))
        
    outputTable(stringer, NWinter, "Xi;Xi+1", type)

def searchElInList(mass:list, el):
    """Поиск элемента в списке"""
    for _ in range(len(mass)):
        if mass[_] == el:
            return _
    return None

def prepareIntervals(massiveX:list, N:list) -> tuple:
    """Подготовка данных по интервалам"""
    
    outputTable(massiveX,N)
    
    def inputIntervals() -> list:
        """Ввод интервалов"""
        intervals = []
        num1 = massiveX[0]
        num2 = float(input("Введите правую границу: "))
        intervals.append([num1, num2])
        while num2 != massiveX[-1]:
            num1 = num2
            num2 = float(input("Введите правую границу: "))
            intervals.append([num1, num2])
        return intervals
    
    intervals = inputIntervals()
    Ninter = []
    start = 0
    end = searchElInList(massiveX,intervals[0][1])
    i = 1
    
    #Считает N по интервалам
    while i-1!=len(intervals):
        n = 0
        for _ in range(start, end):
            n += N[_]
        Ninter.append(n)
        if(i!=len(intervals)):
            start = end
            end = searchElInList(massiveX,intervals[i][1])
        i += 1
        
    Ninter[-1] += N[-1]
    countNinter = len(Ninter)
    Winter = list(map(lambda x: x/countNinter, Ninter))
    return intervals, Ninter, Winter

def inputIntervals() -> tuple:
    """Ввод интервалов"""
    Ninter = []
    intervals = []
    
    print("Ввод интервалов происходит, пока не будет введена -1")
    x1 = input("Введите X: ")
    x2 = input("Введите X + 1: ")
    n = input("Введите N: ")
    while(x1 != "-1" and x2 != "-1" and n != "-1"):
        
        if(x1.find(".") == -1):
            x1 = int(x1)
            x2 = int(x2)
        else:
            x1 = float(x1)
            x2 = float(x2)
        intervals.append([x1,x2])
        Ninter.append(int(n))
        
        x1 = input("Введите X: ")
        if x1 == "-1":
            break
        x2 = input("Введите X + 1: ")
        if x2 == "-1":
            break
        n = input("Введите N: ")
        if n == "-1":
            break
    
    Winter = list(map(lambda x: x/sum(Ninter), Ninter))
        
    return (intervals, Ninter, Winter)

def formules() -> None:
    """Вывод формулы"""
    plt.figure("Формулы", figsize=[5,3.7])
    formulaSig = r'$\sigmaв = \sqrt{Dв}$'
    formulavibDisp = r'$Dв = {\frac{1}{n} \sum_{i=1}^k ni*xi^2} - Xв^2$'
    formulavibX = r'$Xв = \frac{1}{n} \sum_{i=1}^k ni*xi$'

 
    plt.text(0.01, 0.75, formulavibX, fontsize=25)
    plt.text(0.01, 0.35, formulavibDisp, fontsize=25)
    plt.text(0.01, 0.05, formulaSig, fontsize=25)
 

    # Прячем оси для формулы
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
        
    plt.show()  
    
def calcFormules(massiveX:list, N:list) -> None:
    """Расчёт и вывод формул"""
    def XB(massiveX:list, N:list):
        """Вычисление Xв"""
        res = 0
        
        for i in range(len(massiveX)):
            res += massiveX[i] * N[i]
            
        return res/sum(N)

    def DB(massiveX:list, N:list, XB):
        """Вычисление выборочной дисперсии"""
        res = 0
        
        for i in range(len(massiveX)):
            res += massiveX[i]**2 * N[i]
            
        return res/sum(N) - XB**2

    def oB(DB):
        """Вычисление выборочного среднеквадратического отклонения"""
        return math.sqrt(DB)
    
    Xb = XB(massiveX, N)
    Db = DB(massiveX, N, Xb)
    ob = oB(Db)
    
    print(f'{Xb = }\n{Db = }\n{ob = }\n')
    formules()
    
def averIntervals(intervals:list) -> None:
    averInter = []
    
    for _ in intervals:
        averInter.append((_[0]+_[1])/2)
    
    return averInter

def XB(massiveX:list, N:list):
    """Вычисление Xв"""
    res = 0
    
    for i in range(len(massiveX)):
        res += massiveX[i] * N[i]
        
    return res/sum(N)

def DB(massiveX:list, N:list, XB):
    """Вычисление выборочной дисперсии"""
    res = 0
    
    for i in range(len(massiveX)):
        res += massiveX[i]**2 * N[i]
        
    return res/sum(N) - XB**2

def oB(DB):
    """Вычисление выборочного среднеквадратического отклонения"""
    return math.sqrt(DB)
    
def calcPlotnost(massiveX:list, N:list) -> tuple:
    '''Расчет плотности нормального распределения'''
    
    Xb = XB(massiveX, N)
    Db = DB(massiveX, N, Xb)
    ob = oB(Db)

    a = Xb
    oToch = ob
    
    plotnost = []
    Xs = []
    
    k = len(massiveX) # Кол-во точек (половина без центра)
    for i in range(k, 0, -1):
        Xs.append(a-i*ob)

    Xs.append(a)
    
    for i in range(1, k+1):
        Xs.append(a+i*ob)
    
    for i in range(len(Xs)):
        plotnost.append((1/(oToch*math.sqrt(2*math.pi)))*pow(math.e,(-1*(Xs[i]-a)**2/(2*(oToch**2)))))

    return (Xs, plotnost)

def formulesNormDistrib()->None:
    """Вывод формулы"""
    plt.figure("Формулы",figsize=[3,1.5])
    formulaPlot = r'$f = \frac{1}{\sigma\sqrt{2\pi}}  e^\frac{(Xi-a)}{2\sigma^2}$'
    
    plt.text(0.01, 0.4, formulaPlot, fontsize=25)

    # Прячем оси для формулы
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
        
    plt.show()  

def calcFormulesNormDistrib(massiveX:list, N:list)->None:
    '''Подсчет плотности и вывод ее в консоль'''
    Xs, plotnost = calcPlotnost(massiveX, N)
    del(Xs)
    print("f = ",plotnost)
    formulesNormDistrib()
    
def drawGistagramWithLine(intervals:list, NWinter:list, type:str = "Standart") -> None:
    """Вывод гистаграмм"""
    plt.figure(type, figsize=(15,5))
    X = averIntervals(intervals)
    
    lenInt = []
    for i in intervals:
        lenInt.append(i[1]-i[0])
    
    hN = []
    for _ in range(len(NWinter)):
        hN.append(NWinter[_]/len(intervals))
    
    plt.bar(X, hN, width=lenInt, facecolor="red", edgecolor="black")
    
    plt.plot(X,hN, marker='.', markersize=15, markerfacecolor='b', markeredgecolor='g')
    plt.show()

def drawPlotnost(massiveX:list, N:list) -> None:
    '''Вывод графиика плотности'''
    Xs, plotnost = calcPlotnost(massiveX, N)
    
    plt.figure("График плотности нормального распределения")
    plt.axis([Xs[0]-1, Xs[-1]+1, min(plotnost)-0.01, max(plotnost)+0.01])
    
    plt.plot([Xs[0]-0.5,Xs[0]-0.5], [min(plotnost)-0.005,max(plotnost)+0.005],color='b')
    plt.plot(Xs[0]-0.5,max(plotnost)+0.005,marker='^')
    plt.plot([Xs[0]-0.5,Xs[-1]+0.5], [min(plotnost)-0.005,min(plotnost)-0.005],color='b')
    plt.plot(Xs[-1]+0.5,min(plotnost)-0.005,marker='>')
    plt.plot(Xs,plotnost,marker='.',markersize=10, markerfacecolor='black', markeredgecolor="black", color="r", linewidth=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
       
def P(intervals:list, a, ob) -> list:
    '''Подсчёт вероятностей по Симпсону'''
    Xs = []
    for i in intervals:
        Xs.append([(i[0]-a)/ob, (i[1]-a)/ob])
    
    p = []
    
    for i in Xs:
        y = np.power(np.e, (-1*(np.power(i,2)/2)))
        p.append(integrate.simpson(y, i)/math.sqrt(2 * math.pi))
        
    return p

def drawFormulPirson():
    """Вывод формулы X наблюдаемого"""
    plt.figure("Формула X^2 набл")
    formulaXNabl = r'$X^2= \sum_{i=1}^k \frac{(Ni-nPi)^2}{nPi}} $'
 
    plt.text(0.01, 0.5, formulaXNabl, fontsize=25)

    # Прячем оси для формулы
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
        
    plt.show()  

def Pirson(intervals:list, N:list):
    p = P(intervals, XB(averIntervals(intervals), N),oB(DB(averIntervals(intervals),N,XB(averIntervals(intervals),N))))
    
    Xparts = []

    for i in range(len(N)):
        Xparts.append(((N[i] - p[i]*sum(N))**2)/(p[i]*sum(N)))

    return sum(Xparts)

def findFreedom(N:list) -> int:
    return len(N) - 3
