import math

x = float(input("Введите число x: "))
n = int(input("Введите число n: "))
temp=x
result=0
for i in range(n):
    temp = math.sin(temp)
    #print("temp",temp)
    result += temp
    #print(result)
print("Сумма=",result)