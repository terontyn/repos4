a=[]
n=int(input("Введите число чисел в массиве:"))
for i in range(n):
    a.append(int(input("Введите элемент массива: ")))
print(a)

mn = min(a)
mx = max(a)
imn = a.index(mn)
imx = a.index(mx)
a[imn],a[imx] = a[imx],a[imn]
for i in range(n):
    print(a[i], end=' ')
