buah = ["apel", "jeruk", "apel", "pisang", "jeruk", "apel"]
frekuensi = {}

for item in buah:
    if item in frekuensi:
        frekuensi[item] += 1
    else:
        frekuensi[item] = 1

print("Frekuensi:")
for k, v in frekuensi.items():
    print(f"{k}: {v}")
