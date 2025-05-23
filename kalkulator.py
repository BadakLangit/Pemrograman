def kalkulator(**keywords):
    operator = keywords.get("operator")
    angka1 = keywords.get("angka1")
    angka2 = keywords.get("angka2")

    if operator == "+":
        return angka1 + angka2
    elif operator == "-":
        return angka1 - angka2
    elif operator == "*":
        return angka1 * angka2
    elif operator == "/":
        return angka1 / angka2 if angka2 != 0 else "undefined"
    else:
        return "error"
    
def main():
    while True:
        try:
            operator = input("> Masukkan operasi (+-*/): ")
            angka1 = float(input("> Masukkan angka1: "))
            angka2 = float(input("> Masukkan angka2: "))
        except ValueError:
            print("error")
            continue
        hasil= kalkulator(operator=operator, angka1=angka1, angka2=angka2)
        print(f"Hasil = {hasil}")

        konfirmasi = input("Ulangi program? (y): ").lower().strip()
        if konfirmasi != "y":
            break

main()