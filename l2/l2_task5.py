k = int(input("Введите k: "))

for i in range(1,k+1):
    result=0
    for c in str(i):
        result+=pow(int(c),len(str(i)))
    if(result==i):
        print(i,"является числом Амстронга")




