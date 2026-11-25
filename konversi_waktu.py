detik_total = int(input("Masukkan jumlah detik: "))

jam = detik_total // 3600
sisa_detik = detik_total % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("Hasil konversi:", jam, "jam", menit, "menit", detik, "detik")
