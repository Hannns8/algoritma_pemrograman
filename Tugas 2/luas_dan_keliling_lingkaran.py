import math

jari_jari = float(input('masukkan jari jari lingkaran '))
luas_lingkaran = math.pi * math.pow(jari_jari, 2)
keliling_lingkaran = 2 * math.pi * jari_jari

print(f'Luas lingkaran : {luas_lingkaran}\nKeliling Lingkaran: {keliling_lingkaran}')