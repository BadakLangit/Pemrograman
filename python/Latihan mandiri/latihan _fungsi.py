import os
def header():
    os.system('cls')
    print(f'{'PROGRAM MENGHITUNG LUAS':^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG':^40}')
    print(f'{'-'*40:^40}')

def input_user():
    panjang = int(input('Masukkan Nilai Panjang : '))
    lebar = int(input('Masukkan Nilai Lebar : '))
    return panjang,lebar

def luas(panjang,lebar):
    return panjang*lebar

def keliling(panjang,lebar):
    return 2*(panjang+lebar)

while True:
    header()
    PANJANG,LEBAR = input_user()
    LUAS = luas(PANJANG,LEBAR)
    KELILING = keliling(PANJANG,LEBAR)
    print(f'Nilai Luas Persegi Panjang = {LUAS}')
    print(f'Nilai Keliling Persegi Panjang = {KELILING}')

    ulang = input('Ulangi Program (y/n)? : ')
    if ulang == 'n':
        print('Program Selesai')
        break