def input_u():
    nama = input('Masukkan nama barang\t: ').lower().capitalize()
    jumlah = int(input('Masukkan jumlah barang\t: '))
    return nama, jumlah

def lihat(inventory):
    print('\nInventory:')
    if not inventory:
        # Jika tidak ada barang di inventory, print '-'
        print('-')
    else:
        # Print nama barang beserta jumlah barang
        for barang in inventory:
            print(f"{barang['nama']} ({barang['jumlah']})")

def tambah(inventory, nama, jumlah):
    for barang in inventory:
        if barang['nama'] == nama:
            # Menambahkan jumlah barang dengan nama yang sama di dalam inventory 
            barang['jumlah'] += jumlah
            print(f'[{jumlah} {nama} berhasil ditambahkan]')
            return
    # Memasukkan barang baru ke dalam inventory
    inventory.append({'nama': nama, 'jumlah': jumlah}) 
    print(f'[{jumlah} {nama} berhasil ditambahkan]')

def kurang(inventory, nama, jumlah):
    for barang in inventory:
        if barang['nama'] == nama:
            if barang['jumlah'] >= jumlah:
                # Mengurangi jumlah barang dengan nama yang sama di dalam inventory
                barang['jumlah'] -= jumlah
                print(f'[{jumlah} {nama} berhasil dikurangkan]')
                if barang['jumlah'] == 0:
                    # Menghapus barang jika jumlah barang = 0
                    inventory.remove(nama)
                return
            else:
                # Print error message jika jumlah barang di dalam inventory < input
                print(f'[ERROR! Jumlah {nama} tidak mencukupi]')
                return
    # Print error message jika barang tidak ada di dalam inventory
    print(f'ERROR! {nama} tidak ditemukan')

panel = '''
\b====================
(1) Lihat inventory
(2) Tambahkan barang
(3) Kurangkan barang
(4) Exit
====================
'''

import os
def main():
    os.system('cls')
    inventory = []
    while True:
        print(panel)
        perintah = input('Pilih perintah 1/2/3/4\t: ').strip()
        if perintah == '1':
            lihat(inventory)
        elif perintah == '2':
            nama, jumlah = input_u()
            tambah(inventory, nama, jumlah)
        elif perintah == '3':
            nama, jumlah = input_u()
            kurang(inventory, nama, jumlah)
        elif perintah == '4':
            print('[Program selesai]')
            break
        else:
            print('[ERROR! Perintah tidak ditemukan]')

main()