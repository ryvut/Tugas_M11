# No 1
print("Soal No.1")
def pemisah():
    print("~" * 40)
pemisah()
print()

# No 2
print("Soal No.2")
def hitung_luas_banyak(*sisi_list):
    return [s ** 2 for s in sisi_list]

hasil_luas = hitung_luas_banyak(5, 10, 15)
print("Luas persegi adalah:", hasil_luas)
print()

# No 3
print("Soal No.3")
def cek_genap(angka):
    return angka % 2 == 0

status_angka = cek_genap(10)
print("Status angka genap:", status_angka) 
print()

# No 3.1
print("Soal No.3.1")
def hitung_luas_persegi(sisi):
    luas = sisi ** 2
    print(f"Luas persegi adalah: {luas}")
    return luas

def rata_rata_luas(daftar_luas):
    rata = sum(daftar_luas) / len(daftar_luas)
    print(f"Rata-rata luas persegi adalah: {rata}")

daftar_sisi = [5, 10, 15]
hasil = list(map(hitung_luas_persegi, daftar_sisi))

rata_rata_luas(hasil)
print()

# No 4 
print("Soal No.4")
def salam(waktu, nama="Sobat"):
    print(f"Halo, selamat {waktu}, {nama}!")

salam("Pagi", "Andi")
salam("Sore")
print()

# No 5
print("Soal No.5")
def konversi_nilai(nilai_angka):
    if nilai_angka >= 86:
        return "A"
    elif nilai_angka >= 76:
        return "AB"
    elif nilai_angka >= 66:
        return "B"
    return "C"

try:
    nilai_angka = int(input("Masukkan skor Anda: "))
    indeks = konversi_nilai(nilai_angka)
    print(f"Nilai huruf Anda adalah: {indeks}")
except ValueError:
    print("Input harus berupa angka!")