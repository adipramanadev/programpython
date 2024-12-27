angka_benar = 3  # Angka yang harus ditebak
tebakan = 0

while tebakan != angka_benar:
    tebakan = int(input("Pilih angka antara 1 dan 5: "))
    if tebakan < 1 or tebakan > 5:
        print("Tebakan harus antara 1 dan 5. Coba lagi.")
    elif tebakan == angka_benar:
        print("Anda menang!")
    else:
        print("Tebakan salah. Coba lagi.")
