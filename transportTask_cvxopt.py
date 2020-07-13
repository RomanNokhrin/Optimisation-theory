from cvxopt.modeling import variable, op
import time as t

class TransportTask:
    def __init__(self):
        self.x = variable(25, 'x')
        # Стоимость доставки
        self.c = [7,1,1,4,2,3,5,6,6,8,8,2,4,3,7,3,4,2,5,8,8,1,4,7,6]
        
        self.z = (self.c[0]*self.x[0]+self.c[1]*self.x[1]+self.c[2]*self.x[2]+self.c[3]*self.x[3]+self.c[4]*self.x[4]
                 +self.c[5]*self.x[5]+self.c[6]*self.x[6]+self.c[7]*self.x[7]+self.c[8]*self.x[8]+self.c[9]*self.x[9]
                 +self.c[10]*self.x[10]+self.c[11]*self.x[11]+self.c[12]*self.x[12]+self.c[13]*self.x[13]+self.c[14]*self.x[14]
                 +self.c[15]*self.x[15]+self.c[16]*self.x[16]+self.c[17]*self.x[17]+self.c[18]*self.x[18]+self.c[19]*self.x[19]
                 +self.c[20]*self.x[20]+self.c[21]*self.x[21]+self.c[22]*self.x[22]+self.c[23]*self.x[23]+self.c[24]*self.x[24])

    def taskOptimization(self):
         # Условие
        self.mass1 = (self.x[0] + self.x[1] + self.x[2] + self.x[3] + self.x[4] <= 70)
        self.mass2 = (self.x[5] + self.x[6] + self.x[7] + self.x[8] + self.x[9] <= 46)
        self.mass3 = (self.x[10] + self.x[11] + self.x[12] + self.x[13] + self.x[14] <= 39)
        self.mass4 = (self.x[15] + self.x[16] + self.x[17] + self.x[18] + self.x[19] <= 41)
        self.mass5 = (self.x[20] + self.x[21] + self.x[22] + self.x[23] + self.x[24] <= 55)

        self.mass6 = (self.x[0] + self.x[5] + self.x[10] + self.x[15] + self.x[20] == 23)
        self.mass7 = (self.x[1] + self.x[6] + self.x[11] + self.x[16] + self.x[21] == 38)
        self.mass8 = (self.x[2] + self.x[7] + self.x[12] + self.x[17] + self.x[22] == 30)
        self.mass9 = (self.x[3] + self.x[8] + self.x[13] + self.x[18] + self.x[23] == 15)
        self.mass10 = (self.x[4] + self.x[9] + self.x[14] + self.x[19] + self.x[24] == 8)
        # Решение 
        self.x_non_negative = (self.x >= 0)    
        self.problem = op(self.z,[self.mass1,self.mass2,self.mass3,self.mass4,self.mass5
                                 ,self.mass6,self.mass7,self.mass8,self.mass9,self.mass10,self.x_non_negative])
    
        self.problem.solve(solver='glpk')
        
        print("Результат Xopt:")
        for i in self.x.value:
            print(i)
        print("Стоимость доставки:")
        print(self.problem.objective.value()[0])


        
# Создаем экземпляр класса TransportTask
transportTask = TransportTask()

start = t.time() # Время начала выполнения
transportTask.taskOptimization() # Запуск
stop = t.time() # Время завершения выполнения    

print("Время выполнения:")
print(stop - start)     
