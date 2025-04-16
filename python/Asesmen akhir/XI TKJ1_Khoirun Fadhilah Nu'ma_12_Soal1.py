# Nama  : Khoirun Fadhilah Nu'ma
# Kelas : XI TKJ 1
# Absen : 12

# Program Manajemen Daftar Belanja

keranjang = []
for i in range(5):
    barang = input('Masukkan barang\t: ').capitalize().strip()
    keranjang.append(barang)

def list_barang():
    print('\nList barang belanja\t:')
    for i, barang in enumerate(keranjang, start=1):
        print(f'{i}. {barang}')
list_barang()

barang_2 = input('\nMasukkan barang baru\t: ').capitalize().strip()
keranjang.insert(1, barang_2)
list_barang()

while True:
    try:
        barang_hapus = int(input('\nNomor yang dihapus\t: '))
        del keranjang[barang_hapus - 1]
        break
    except ValueError:
        print('Input salah')
    
list_barang()