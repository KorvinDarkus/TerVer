def prepareKriticArray() -> None:
    """Функция подготовки массив по столбцам таблицы крит. значений"""
    arr1 = []
    arr2 = [] 
    arr3 = []
    
    with open('tableKritic.txt', "r") as file:  
        str = file.read().replace('\n',' ').split(' ')
        
        for _ in range(3, len(str), 3):
            arr1.append(str[_])
            arr2.append(str[_+1])
            arr3.append(str[_+2])
        
    arr1 = list(map(float, arr1))  
    arr2 = list(map(float, arr2))
    arr3 = list(map(float, arr3))
    
    return (arr1, arr2, arr3)

def getValueKritic(v:int, a:float) -> float:
    """Получнеие критического значения по степени свободы и уровню значимости"""
    arr1, arr2, arr3 = prepareKriticArray()
    
    if(a == 0.01):
        return arr1[v-1]
    elif(a == 0.025):
        return arr2[v-1]
    elif(a == 0.05):
        return arr3[v-1]
    
    return None