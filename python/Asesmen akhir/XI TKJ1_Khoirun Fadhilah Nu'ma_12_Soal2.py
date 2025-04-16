# Nama  : Khoirun Fadhilah Nu'ma
# Kelas : XI TKJ 1
# Absen : 12

# Program Kalkulator diskon penjualan
while True:
    try:
        b_awal = float(input('Masukkan total belanja\t= Rp '))
        break
    except ValueError:
        print('[Error : Input tidak valid]')

if b_awal < 50000:
    b_akhir = b_awal
elif 50000 <= b_awal <= 100000:
    b_akhir = b_awal * 0.90
elif 100000 < b_awal <= 200000:
    b_akhir = b_awal * 0.85
else:
    b_akhir = b_awal * 0.80

diskon = int((1 - (b_akhir / b_awal)) * 100)

print(f'''
Belanja awal\t= Rp {b_awal}
Besar diskon\t= {diskon}%
Total akhir\t= Rp {b_akhir}
''')