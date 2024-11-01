print()
print('Soal Nomor 1')
# Nomor 1

kendaraan = ['Beat karbu', 'motor', '200', 'pink', 2]

kendaraan.append('13jt')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'Honda')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))

print()
print('Soal Nomor 2')
# Nomor 2

hitung_luas = int(input("""Pilih salah satu:
1.Hitung luas persegi
2.Hitung luas lingkaran
3.Hitung luas segitiga           
 """))

match hitung_luas:
    case 1:
        print('Menghitung Luas persegi')
        sisi = int(input('masukkan nilai sisi'))
        hitung_luas_persegi = sisi**2
        print(f'Jadi luas persegi dengan sisi {sisi} cm, adalah {hitung_luas_persegi} cm^2')
    case 2:
        print('Menghitung Luas Lingkaran')
        jari_jari = int(input('Masukkan nilai jari_jari'))
        phi = 22/7
        hitung_luas_lingkaran = phi*jari_jari**2
        print(f'Jadi luas lingkaran dengan sisi {jari_jari} cm, adalah {hitung_luas_lingkaran} cm^2')
    case 3:
        print('Menghitung Luas Segitiga')
        alas = int(input('Masukkan nilai alas'))
        tinggi = int(input('Masukkan nilai tinggi'))
        hitung_luas_segitiga = 1/2*alas*tinggi
        print(f'Jadi luas segitiga dengan alas {alas} cm, dan tinggi {tinggi} cm, adalah {hitung_luas_segitiga} cm^2')
    case _:
        print('Pilihan Tidak Valid')

