n = int(input('Введите число чисел в последовательности: '))
s = 0

for i in range(n):
    i = int(input('Введите число: '))
    if (i>0) and i%2 == 0:
        
        s = s+i #суммирование
     
print("сумма=", s)
