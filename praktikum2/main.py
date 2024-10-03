from cekbilangan import checkOddEvenNumber
from cekKesehatan import healltyCheck
from cekNilai import examCheck


check = True
while check:
    print("""========apa yang anda inginkan========
1. cek kesehatans
2. cek bilangan ganjil atau genap
3. cek nilai
======================================""")
    answer = int(input('masukkan nomor yang sesuai untuk melakukan pengecekkan! '))
    if answer == 1:
        age = int(input('masukkan usia Anda (0 - 100) '))
        blood = int(input('masukkan tekanan darah Anda '))
        print(healltyCheck(age=age, blood=blood))

    elif answer == 2:
        angka = input('masukkan sebuah angka! ')
        print(checkOddEvenNumber(angka))
    
    elif answer == 3:
        nilai = int(input('masukkan nilai Anda: '))
        print(examCheck(nilai))
    else:
        print('anda memasukkan angka yang salah! ')
    check = input('apakah Anda ingin melakukan pengecekkan lagi? (y/n) ').lower()
    if 'y' not in check:
        check = False

print('Terimakasih telah melakukan pengecekkan!')