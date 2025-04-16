# PROGRAM CRUD (CREATE, READ, UPDATE, DELETE)
# SEE LINE 500 FOR VERIFICATION!
# NAMA  = KHOIRUN FADHILAH NU'MA
# KELAS = XI TKJ 1
# ABSEN = 12

import os
Inventory = []

def header(String):
    """Membuat header untuk sebuah string"""
    print(f"\n{'-'*30:^30}")
    print(String)
    print(f"{'-'*30:^30}")

def nama():
    """Memberikan atribut nama kapada item"""
    while True:
        Nama = input("Masukkan nama item: ").strip().lower().capitalize()
        if Nama:
            break
        else:
            print("[ERROR! nama tidak boleh kosong]")
            continue
    return Nama

def jumlah():
    """Memberikan atribut jumlah kepada item"""
    while True:
        try:
            Jumlah = int(input("Masukkan jumlah item: "))
            if Jumlah > 0:
                break
            print("[ERROR! jumlah harus lebih dari 0]")
        except ValueError:
            print("[ERROR! jumlah harus berupa angka]")
    return Jumlah

def create():
    """Menambahkan item ke dalam Inventory"""
    Nama = nama()
    for Item in Inventory:
        if Item["Nama"] == Nama:
            print(f"[ERROR! {Nama} sudah ada di dalam Inventory]")
            return
    Jumlah = jumlah()
    Inventory.append({"Nama":Nama,"Jumlah":Jumlah})
    print(f"[{Nama} ({Jumlah}) berhasil ditambahkan]")

def read():
    """Menunjukkan item di dalam Inventory"""
    header(f"{'Nama':<15}{'Jumlah':>15}")
    if not Inventory:
        print(f"{'-':^30}")
    else:
        for Item in Inventory:
            print(f"{Item['Nama']:<15}{Item['Jumlah']:>15}")
    print(f"{'###':^30}")

def update():
    """Mengupdate item di dalam list"""
    if not Inventory:
        print("[ERROR! Inventory masih kosong]")
        return
    else:
        Nama = nama()
        for Item in Inventory:
            if Item["Nama"] == Nama:
                header(f"{Item['Nama']:<15}{Item['Jumlah']:>15}")
                print("1. ADD\n2. SUBTRACT\n3. REPLACE\n0. EXIT\n")
                Panggil = input("Pilih program: ").strip().lower()
                if Panggil in ["1","a","add","+"]:
                    """Menambah jumlah item"""
                    Jumlah_A = jumlah()
                    Item["Jumlah"] += Jumlah_A
                    print(f"[{Nama} ({Jumlah_A}) -> {Nama} ({Item['Jumlah']})]")
                    return
                elif Panggil in ["2","s","subtract","-"]:
                    """Mengurangi jumlah item"""
                    Jumlah_S = jumlah()
                    if Item["Jumlah"] < Jumlah_S:
                        print("[ERROR! input melebihi jumlah stok]")
                    else:
                        Item["Jumlah"] -= Jumlah_S
                        if Item["Jumlah"] == 0:
                            Inventory.remove(Item)
                            print(f"[{Nama} dihapus dari inventory karena jumlahnya 0]")
                            return
                        else:
                            print(f"[{Nama} ({Jumlah_S}) -> {Nama} ({Item['Jumlah']})]")
                    return
                elif Panggil in ["3","replace","r"]:
                    """Mengganti item di dalam Inventory"""
                    Nama_R = nama()
                    Jumlah_R = jumlah()
                    Item["Nama"] = Nama_R
                    Item["Jumlah"] = Jumlah_R
                    print(f"[{Nama} berhasil diganti dengan {Nama_R} ({Jumlah_R})]")
                    return
                elif Panggil in ["0","e","ex","exit"]:
                    return        
                elif Panggil in ["cls","clear"]:
                    os.system("cls")
                    continue        
                else:
                    print("[ERROR! program tidak ditemukan]")
                    continue
        print(f"[ERROR! {Nama} tidak ditemukan di inventory]")
        return

def delete():
    """Menghapus item di dalam list"""
    Nama = nama()
    for Item in Inventory:
        if Item["Nama"] == Nama:
            Inventory.remove(Item)
            print(f"[{Nama} berhasil dihapus]")
            return
    print(f"[ERROR! {Nama} tidak ditemukan dalam Inventory]")

def main():
    """Program utama untuk mengakses semua perintah"""
    while True:
        header(f"{'PROGRAM CRUD PYTHON':^30}")
        print("1. CREATE\n2. READ\n3. UPDATE\n4. DELETE\n0. EXIT\n")
        Panggil = input("Pilih program: ").strip().lower()
        Programs = {
            "1": create, "c": create, "create": create,
            "2": read, "r": read, "read": read,
            "3": update, "u": update, "update": update,
            "4": delete, "d": delete, "delete": delete,
        }
        if Panggil in Programs:
            Programs[Panggil]()
        elif Panggil in ["0","e","ex","exit"]:
            print("[Program selesai]")
            break
        elif Panggil in ["cls","clear"]:
            os.system("cls")
            continue
        else:
            print("[ERROR! program tidak ditemukan]")

main()






































































































































































































































































































































































# PROGRAM INI DIBUAT OLEH:
# NAMA  = KHOIRUN FADHILAH NU'MA
# KELAS = XI TKJ 1
# ABSEN = 12
# JIKA IDENTITAS DI LINE 3-5 TIDAK SESUAI MAKA
# PROGRAM INI TELAH DICOPY OLEH OLEH ORANG LAIN!