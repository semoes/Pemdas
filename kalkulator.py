angka1 = float(input("Masukkan angka pertama: "))
operator = input("Pilih operasi (+, -, *, /): ")
angka2 = float(input("Masukkan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Tidak bisa membagi dengan nol"
else:
    hasil = "Operator tidak dikenal"

print("Hasil:", hasil)
