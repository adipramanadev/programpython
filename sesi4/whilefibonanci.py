max_angka = int(input("Masukkan angka maksimum untuk deret Fibonacci: "))
a, b = 0, 1

print("Deret Fibonacci:")
while a <= max_angka:
    print(a, end=" ")
    a, b = b, a + b  # Mengupdate nilai a dan b
