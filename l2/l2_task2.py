x = float(input("Введите число: "))
temp=x
result=x;
for i in range(1,7):
    temp = temp*x*x/(2*i)/(2*i+1)
    result= result+temp*pow(-1,i)
print("Сумма=",result)