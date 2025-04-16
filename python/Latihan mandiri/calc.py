items = {
    'CUP' : 2200,
    'MINI' : 1500,
    'MEDIUM' : 2300,
    'YOGHURT' : 3000,
    'PLAIN' : 5500
}

import os
os.system("cls")

print ('[MASUKKAN DATA SETORAN]'.center(50, ':') + '\n')
start_counts = {item: int(input(f'Stok awal {item:<8} = ')) for item in items}
end_counts = {item: int(input(f'Stok sisa {item:<8} = ')) for item in items}

print('\n' + '[HASIL SETORAN]'.center(50, ':') + '\n')

total = 0
for item, price in items.items():
    sold = start_counts[item] - end_counts[item]
    item_total = sold * price
    total += item_total
    print(f'{item:<8} = {sold} x {price} = {item_total}')

print(f'{'TOTAL':<8} = {total}\n')