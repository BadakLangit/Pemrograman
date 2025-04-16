import os

Inventory = []

def header(Prompt):
    '''Membuat header untuk sebuah prompt'''
    print(f"\n{'-' * 30 :^30}")
    print(Prompt)
    print(f"{'-' * 30 :^30}")
    
def clear():
    '''Membersihkan terminal'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def input_user(Prompt, Is_Number=False):
    '''Mengambil value string dan int dari user'''
    while True:
        Value = input(Prompt).strip()
        if not Value:
            print("[ERROR! Input tidak boleh kosong]")
            continue
        elif Is_Number:
            try:
                Number = int(Value)
                if Number > 0:
                    return Number
                else:
                    print("[ERROR! Jumlah harus lebih dari 0]")
            except ValueError:
                print("[ERROR! Masukkan angka yang valid]")
        else:
            return Value.capitalize()
        
def find(Nama):
    '''Mencari item di dalam Inventory'''
    for Item in Inventory:
        if Item["Nama"].lower() == Nama.lower():
            return Item
    return None

def create():
    '''Menambahkan item dan jumlahnya ke dalam Inventory'''
    Nama = input_user("Masukkan item baru: ")
    if find(Nama):
        print("[ERROR! Item sudah ada di Inventory]")
        return
    Jumlah = input_user("Masukkan jumlah item: ", Is_Number=True)
    Inventory.append({"Nama": Nama, "Jumlah": Jumlah})
    print(f"[{Nama} ({Jumlah}) berhasil ditambahkan ke dalam Inventory]")

def read():
    '''Menunjukkan item dalam Inventory dalam bentuk tabel'''
    header(f"{'Nama' :<15}{'Jumlah' :>15}")
    if not Inventory:
        print(f"{'-' :^30}")
    else:
        for Item in Inventory:
            print(f"{Item['Nama'] :<15}{Item['Jumlah'] :>15}")
    print(f"{'###' :^30}")

def add(Item):
    '''Menambahkan jumlah item di dalam Inventory'''
    Jumlah_add = input_user("Masukkan jumlah untuk ditambah: ", Is_Number=True)
    Item["Jumlah"] += Jumlah_add
    print(f"[{Item['Nama']} berhasil ditambah menjadi ({Item['Jumlah']})]")

def subtract(Item):
    '''Mengurangkan jumlah item di dalam Inventory'''
    Jumlah_subtract = (input_user("Masukan jumlah untuk dikurang: ", Is_Number=True))
    if Item["Jumlah"] < Jumlah_subtract:
        print("[ERROR! Jumlah input melebihi stok]")
    else:
        Item["Jumlah"] -= Jumlah_subtract
        if Item["Jumlah"] == 0:
            Inventory.remove(Item)
            print(f"[{Item['Nama']} dihapus dari Inventory karena jumlahnya 0]")
        else:
            print(f"[{Item['Nama']} berhasil dikuang menjadi ({Item['Jumlah']})]")

def replace(Item):
    '''Mengganti item dan jumlahnya di dalam Inventory'''
    Item["Nama"] = input_user("Masukkan item baru: ")
    Item["Jumlah"] = input_user("Masukkan jumlah item: ", Is_Number=True)
    print(f"[Item berhasi diganti menjadi {Item['Nama']} ({Item['Jumlah']})]")

def update():
    '''Mengontrol program add, subtract, dan replace'''
    if not Inventory:
        print("[ERROR! Inventory masih kosong]")
        return
    Nama = input_user("Masukkan nama item: ")
    Item = find(Nama)
    if not Item:
        print(f"[ERROR! {Nama} tidak ditemukan]")
        return
    header(f"{Item['Nama'] :<15}{Item['Jumlah'] :>15}")
    print("1. Add\n2. Subtract\n3. Replace\n0. Exit\n")
    Actions = {
        "1": add, "a": add, "add": add,
        "2": subtract, "s": subtract, "subtract": subtract,
        "3": replace, "r": replace, "replace": replace,
    }
    Call = input_user("Pilih program: ").lower()
    if Call in Actions:
        Actions[Call](Item)
    elif Call in ["0", "e", "exit"]:
        return
    else:
        print("[ERROR! Program tidak ditemukan]")

def delete():
    '''Menghapus item di dalam Inventory'''
    Nama = input_user("Masukkan item untuk dihapus: ")
    Item = find(Nama)
    if Item:
        Inventory.remove(Item)
        print(f"[{Nama} berhasil dihapus dari Inventory]")
    else:
        print(f"[ERROR! {Nama} tidak ditemukan]")

def main():
    '''Program untuk mengontrol function CRUD'''
    clear()
    while True:
        header(f"{'Program CRUD Python' :^30}")
        print("1. Create\n2. Read\n3. Update\n4. Delete\n0. Exit")
        Actions = {
            "1": create, "c": create, "create": create,
            "2": read, "r": read, "read": read,
            "3": update, "u": update, "update": update,
            "4": delete, "d": delete, "delete": delete,
            "cls": clear, "clear": clear,
        }
        Call = input_user("Pilih program: ").lower()
        if Call in Actions:
            Actions[Call]()
        elif Call in ["0", "e", "exit"]:
            print("[Program selesai]")
            break
        else:
            print("[ERROR! Program tidak ditemukan]")

main()