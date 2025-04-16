def daftar_belanja():
    belanja = []
    harga = []

    while True:
        item = input("Item belanja\t\t: ").strip()
        price = int(input("Masukkan harga barang\t:"))
        belanja.append(item)
        harga.append(price)
        total = 0
        print(f"[{item}] telah ditambahkan")

        while True:
            lanjut = input("\nAdakah item lain? (y/n)\t: ").strip().lower()
            if lanjut == 'y':
                break
            elif lanjut == 'n':
                print("\nDaftar Belanja Akhir\t:")
                for i, barang in enumerate(belanja, start=1):
                    print(f"{i}. {barang}")
                for i, price in enumerate(harga, start=1):
                    print(f"{i}. {harga}")
                    total += price
                    print(total)
                return
            else:
                print("Input tidak valid.")

daftar_belanja()