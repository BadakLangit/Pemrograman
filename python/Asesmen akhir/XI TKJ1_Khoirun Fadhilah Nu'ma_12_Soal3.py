# Nama  : Khoirun Fadhilah Nu'ma
# Kelas : XI TKJ 1
# Absen : 12

# Program Aplikasi Berat Badan Ideal

nama = input('Nama\t\t\t: ')

while True:
    kelamin = input('Kelamin (Pria/Wanita)\t: ').lower().capitalize()
    if kelamin in ['Pria', 'Wanita']:
        break
    else:
        print('[Error : Kelamin tidak diketahui]')

while True:        
    try:
        tinggi = int(input('Tinggi badan(cm)\t: '))
        break
    except ValueError:
        print('[Error : Tinggi badan harus berupa angka]')

if kelamin == 'Pria':
    bbi = tinggi - 100
else:
    bbi = tinggi - 110

print(f'\nBerat badan ideal\t: {bbi}kg')