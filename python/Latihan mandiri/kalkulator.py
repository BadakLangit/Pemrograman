print('''
Kalkulator Sederhana
Khoirun Fadhilah Nu'ma
12 / XI TKj 1
''')

while True:
    try:
        angka1 = float(input('Angka pertama\t= '))
        angka2 = float(input('Angka kedua\t= '))
        break
    except ValueError:
        print('[Input harus berupa angka]\n')

print('''
==================
[+] -> Penjumlahan
[-] -> Pengurangan
[*] -> Perkalian
[/] -> Pembagian
==================
''')

while True:
    operators = ['+', '-', '*', '/']
    input_operator = input('Operator\t> ').strip()
    if input_operator in operators:
        break
    else:
        print('[Operator tidak tersedia]\n')

if input_operator == '+':
    hasil = angka1 + angka2
elif input_operator == '-':
    hasil = angka1 - angka2
elif input_operator == '*':
    hasil = angka1 * angka2
elif input_operator == '/' and angka2 != 0:
    hasil = angka1 / angka2
else:
    hasil = 'Tak terdefinisi'

print(f'\n{angka1} {input_operator} {angka2}\t= {hasil}\n')