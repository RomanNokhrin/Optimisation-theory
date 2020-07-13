from pulp import *
import numpy as np
import time as t

class TransportTask:
    def __init__(self):
        # Количество перевозимого товара
        self.x1 = pulp.LpVariable("x1", lowBound=0)
        self.x2 = pulp.LpVariable("x2", lowBound=0)
        self.x3 = pulp.LpVariable("x3", lowBound=0)
        self.x4 = pulp.LpVariable("x4", lowBound=0)
        self.x5 = pulp.LpVariable("x5", lowBound=0)
        self.x6 = pulp.LpVariable("x6", lowBound=0)
        self.x7 = pulp.LpVariable("x7", lowBound=0)
        self.x8 = pulp.LpVariable("x8", lowBound=0)
        self.x9 = pulp.LpVariable("x9", lowBound=0)
        self.x10 = pulp.LpVariable("x10", lowBound=0)
        self.x11 = pulp.LpVariable("x11", lowBound=0)
        self.x12 = pulp.LpVariable("x12", lowBound=0)
        self.x13 = pulp.LpVariable("x13", lowBound=0)
        self.x14 = pulp.LpVariable("x14", lowBound=0)
        self.x15 = pulp.LpVariable("x15", lowBound=0)
        self.x16 = pulp.LpVariable("x16", lowBound=0)
        self.x17 = pulp.LpVariable("x17", lowBound=0)
        self.x18 = pulp.LpVariable("x18", lowBound=0)
        self.x19 = pulp.LpVariable("x19", lowBound=0)
        self.x20 = pulp.LpVariable("x20", lowBound=0)
        self.x21 = pulp.LpVariable("x21", lowBound=0)
        self.x22 = pulp.LpVariable("x22", lowBound=0)
        self.x23 = pulp.LpVariable("x23", lowBound=0)
        self.x24 = pulp.LpVariable("x24", lowBound=0)
        self.x25 = pulp.LpVariable("x25", lowBound=0)
        self.quantityStock = [70,46,39,41,55] # Количество товара на складе
        self.quantityOrdered = [23,38,30,15,8] # Количество заказанного товара
        
    def taskOptimization(self):
        # Определение
        self.task = pulp.LpProblem('0',pulp.LpMaximize)
        self.task += (-7*self.x1 - 1*self.x2 - 1*self.x3 - 4*self.x4 - 2*self.x5
                      -3*self.x6 - 5*self.x7 - 6*self.x8 - 6*self.x9 - 8*self.x10 
                      -8*self.x11 - 2*self.x12 - 4*self.x13 - 3*self.x14 - 7*self.x15 
                      -3*self.x16 - 4*self.x17 - 2*self.x18 - 5*self.x19 - 8*self.x20 
                      -8*self.x21 - 1*self.x22 - 4*self.x23 - 7*self.x24 - 6*self.x25), "Функция цели"
        
        # Условие
        self.task += self.x1 + self.x2 + self.x3 + self.x4 + self.x5 <= self.quantityStock[0],"1" 
        self.task += self.x6 + self.x7 + self.x8 + self.x9 + self.x10 <= self.quantityStock[1],"2"
        self.task += self.x11 + self.x12 + self.x13 + self.x14 + self.x15 <= self.quantityStock[2],"3"
        self.task += self.x16 + self.x17 + self.x18 + self.x19 + self.x20 <= self.quantityStock[3],"4"
        self.task += self.x21 + self.x22 + self.x23 + self.x24 + self.x25 <= self.quantityStock[4],"5"        
        self.task += self.x1 + self.x6 + self.x11 + self.x16 + self.x21 == self.quantityOrdered[0],"6"
        self.task += self.x2 + self.x7 + self.x12 + self.x17 + self.x22 == self.quantityOrdered[1],"7"
        self.task += self.x3 + self.x8 + self.x13 + self.x18 + self.x23 == self.quantityOrdered[2],"8"
        self.task += self.x4 + self.x9 + self.x14 + self.x19 + self.x24 == self.quantityOrdered[3],"9"
        self.task += self.x5 + self.x10 + self.x15 + self.x20 + self.x25 == self.quantityOrdered[4],"10"
        # Решение                    
        self.task.solve()
                    
# Создаем экземпляр класса TransportTask
transportTask = TransportTask()

start = t.time() # Время начала выполнения
transportTask.taskOptimization() # Запуск
stop = t.time() # Время завершения выполнения    
 
print ("Результат:")
for variable in transportTask.task.variables():
    print (variable.name, "=", variable.varValue)
    
print ("Стоимость доставки:")
print (abs(value(transportTask.task.objective)))

print ("Время выполнения:")
print(stop - start)