import random                  
def sdvig(massive,k):              #функция для сдвига элементов строки
    for i in range(0,k):               #повтор сдвига на одну позиции k раз
        massive.insert(0,massive.pop())     #перестановка последнего элемента в начало списка
print('Ввести количество строк матрицы')
m=int(input())
print('Ввести количество столбцов в матрице')
n=int(input())
print('Ввести шаг сдвига')
k=int(input())                         
massive=[]                   

for i in range(0,m):             #проходимся по строкам
    massive.append([])           
    for j in range(0,n):         #проходимся по элементам строки
        massive[i].append(int(random.random() * 100))     
print(massive)                  

for l in range(0,m):            #проходимся по строкам массива
    if l%2==0:                  #если строка четная
        sdvig(massive[l],k)     #вызываем функцию сдвига
print(massive)                  #печатаем получившийся
