import math
import matplotlib.pyplot as plt
from Task_1 import XB, outputTable


def formules2() -> None:
    """Вывод формулы"""
    plt.figure("Формулы", figsize=[4.5,1.7])
    formulavibX = r'$λ^*=Xв = \frac{1}{n} \sum_{i=1}^k ni*xi$'

    plt.text(0.01, 0.4, formulavibX, fontsize=25)
 
    # Прячем оси для формулы
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
        
    plt.show()  

def calcFormules2(massiveX:list, N:list) -> None:
    """Расчёт и вывод формул"""
    def XB(massiveX:list, N:list):
        """Вычисление Xв"""
        res = 0
        
        for i in range(len(massiveX)):
            res += massiveX[i] * N[i]
            
        return res/sum(N)

    λ = XB(massiveX, N)

    
    print(f'{λ = }\n')
    formules2()

def drawFormulesProbability()->None:
    """Вывод формулы плотности"""
    plt.figure("Формулы",figsize=[3.5,1.5])

    formulaPlot = r'$P(X=x_i) = \frac{λ^{x_i} e^{-λ}}{x_i!}$'

    plt.text(0.01, 0.5, formulaPlot, fontsize=25)

    # Прячем оси для формулы
    fig = plt.gca()
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
        
    plt.show()  
    
def calcProbability(massiveX:list, N:list) -> list:
    
    λ = XB(massiveX, N)
    
    def Puas(x) -> float:
        return (math.pow(λ, x) * math.pow(math.e,-λ))/math.factorial(int(x))
    
    p = list(map(Puas, massiveX))
    return p

def newN(massiveX:list, N:list)->list:
    
    p = calcProbability(massiveX, N)
    
    upgradeN =[]
    np = []
    
    for i in range(len(p)):
        np.append(sum(N)*p[i])
        
    for i in range(len(np)):
        upgradeN.append((np[i] - N[i])**2)
        
    outputTable(massiveX, upgradeN, type2="NI'")
        
    return upgradeN
    
def Pirson2(massiveX:list, N:list):
    p = calcProbability(massiveX, N)
    
    Xparts = []

    for i in range(len(N)):
        Xparts.append(((N[i] - p[i]*sum(N))**2)/(p[i]*sum(N)))

    return sum(Xparts)

def drawPoligonWP(massiveX:list, WP:list, type:str = "Standart", type2:bool = True) -> None:
    plt.figure(type)
    plt.axis([massiveX[0]-1, massiveX[-1]+1, 0, max(WP)+0.01])
    
    plt.plot([massiveX[0]-0.5,massiveX[0]-0.5], [0.005,max(WP)+0.005],color='b')
    plt.plot(massiveX[0]-0.5,max(WP)+0.005,marker='^')
    plt.plot([massiveX[0]-0.5,massiveX[-1]+0.5], [0.005,0.005],color='b')
    plt.plot(massiveX[-1]+0.5,0.005,marker='>')
    plt.plot(massiveX,WP,marker='.',markersize=10, markerfacecolor='black', markeredgecolor="black", color="r", linewidth=1)
    plt.xlabel(r'$X_i$')
    if type2:
        plt.ylabel(r'$W_i$')
    else:
        plt.ylabel(r'$P_i$')
    plt.show()
       
