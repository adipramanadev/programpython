fibonanci = int(input("Masukkan Jumlah bilangan fibonanci :"))
a, b = 0 , 1
print("Fibonacci : ", end = "")
for i in range(fibonanci):
    print(a, end = ' ')
    a, b = b, a + b