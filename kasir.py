nama = input("Nama barang: ")
harga = int(input("Harga satuan: "))
jumlah = int(input("Jumlah beli: "))
persen = float(input("Diskon (%): "))

total = harga * jumlah
diskon = total * persen / 100
bayar = total - diskon

print("Nama barang:", nama)
print("Total belanja:", total)
print("Diskon:", diskon)
print("Total bayar:", bayar)
