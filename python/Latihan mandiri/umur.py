# Program menghitung umur dengan library datetime
import datetime

nama = input('Nama lengkap\t= ')
tanggal = int(input('Tanggal lahir\t= '))
bulan = int(input('Bulan lahir\t= '))
tahun = int(input('Tahun lahir\t= '))

hari_ini = datetime.date.today()
hari_lahir = datetime.date(tahun, bulan, tanggal)

umur = hari_ini.year - hari_lahir.year

# Cek apakah user sudah ulang tahun di tahun ini
if hari_ini < datetime.date(hari_ini.year, hari_lahir.month, hari_lahir.day):
    umur -= 1

print(f"Umur anda\t= {umur} tahun")