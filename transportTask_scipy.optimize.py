from scipy.optimize import linprog as lin
import time as t

class TransportTask:
    def __init__(self):
        # Стоимость доставки
        self.x  = [7,1,1,4,2,3,5,6,6,8,8,2,4,3,7,3,4,2,5,8,8,1,4,7,6]
        self.quantityStock = [70,46,39,41,55]
        self.quantityOrdered = [23,38,30,15,8]
    
        self.a_ub = [[1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                     [0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
                     [0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0, 0,0,0,0,0],
                     [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1, 0,0,0,0,0],
                     [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 1,1,1,1,1]] 
 
        self.a_eq = [[1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0, 1,0,0,0,0],
                     [0,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0, 0,1,0,0,0],
                     [0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0, 0,0,1,0,0],
                     [0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0, 0,0,0,1,0],
                     [0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1, 0,0,0,0,1]] 
        
    def taskOptimization(self):
        self.start = t.time() # Время начала выполнения 
        print(lin(self.x, self.a_ub, self.quantityStock, self.a_eq, self.quantityOrdered)) # Результат
        self.stop = t.time() # Время завершения выполнения
        print ("Время выполнения:")
        print(self.stop - self.start)
        
        
# Создаем экземпляр класса TransportTask
transportTask = TransportTask()
transportTask.taskOptimization()