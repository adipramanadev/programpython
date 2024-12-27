number = int(input('Masukkan pengulangan Anda :'))

for x in range(1 , number + 1): 
    if x % 2 !=0 :
        print('BIlangan Ganjil', x)
    else: 
        print('Bilangan Genap', x)
      