def pohon(): #Membuat pohon dari karakter
    n = int(input('Masukkan range : '))
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        pattern = 'Δ' * (2 * i + 1)
        print (spaces + pattern)
    print (' ' * (n - 1) + 'Δ' + '\n')
def vokal(): #Mengubah huruf vokal
    teks = input('Masukkan kalimat\t: ')
    ganti = input ('Masukkkan pengganti\t: ')
    for huruf in 'aiueoAIUEO':
            teks = teks.replace(huruf, ganti)
    print (f'[{teks}]')
def faktorial(): #Menghitung bilangan faktorial
    n = int(input('Masukkan angka : '))
    faktorial = 1
    for i in  range(1, n + 1):
          faktorial *= i
    print (f'{n} faktorial adalah {faktorial}')
def penjumlahan(): #Menjumlahkan angka dari 1 sampai input
    n = int(input('Masukkan angka : '))
    jumlah = 0
    i = 1
    while i <= n:
        jumlah += i
        i += 1
    print(f'hasil dari 1 sampai {n} adalah {jumlah}')
def genap(): #Print bilangan genap dengan batas input
	n = int(input('Masukkan angka : '))
	i = 2
	while i <= n:
		print(i)
		i += 2


programs = {
    'pohon' : pohon,
    'vokal' : vokal,
    'faktorial' : faktorial,
    'penjumlahan' : penjumlahan,
    'genap' : genap
}
for program in programs:
    print(f'[{program}]')
while True:
    panggil = input('\nMasukkan nama program : ')
    if panggil in programs:
        print('\n' + '[PROGRAM]'.center(50, ':') + '\n')
        programs[panggil]()
        break
    elif panggil == 'exit':
        break
    else:
        print(f'[Program {panggil} tidak ditemukan]')