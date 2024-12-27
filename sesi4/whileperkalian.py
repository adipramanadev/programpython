angka = int(input("Masukkan angka untuk tabel perkalian: "))
i = 1 #dimulai dari angka 1

print(f"Tabel Perkalian {angka}:")
while i <= 10:
    print(f"{angka} x {i} = {angka * i}")
    i += 1  # Menambahkan 1 untuk iterasi berikutnya
