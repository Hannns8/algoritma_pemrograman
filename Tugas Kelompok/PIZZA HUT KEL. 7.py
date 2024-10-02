#Layanan pemesanan pizza dengan memilih topping crush dan ukuran pizza
def pesan_pizza():
    print("selamat datang di asisten pemesanan pizza")

    #pilih topping
    print("""\nPilih topping:
1. Peperroni (Rp. 30.000)
2. American favorite (Rp. 40.000)
3. Super supreme (Rp.40.000)
4. meat lovers (Rp. 45.000)
    """)
    
    topping_choice = int(input("masukkan pilihan topping (1/2/3/4): "))
    while type(topping_choice) == type(9):
        if topping_choice == 1:
            topping = "Peperroni"
            harga_topping = 30000
            break
        elif topping_choice == 2:
            topping = "american favorite"
            harga_topping = 40000
            break
        elif topping_choice == 3:
            topping = "super supreme"
            harga_topping = 40000
            break
        elif topping_choice == 4:
            topping = "meat lovers"
            harga_topping = 45000
            break
        else:
            print("pilihan topping tidak sesuai. silahkan ulangi kembali.")
            topping_choice = int(input("masukkan pilihan topping (1/2/3/4): "))
        
    #pilih crust dengan memasukkan angka
    print("\nPilih crust pizza:")
    print("""
1. pan crush\t: (Rp. 15.000)
2. cheese bite crust\t: (Rp. 20.000)
3. Chilli Cheesy Stuffed Crust\t: (Rp. 20.000)
4. Stuffed Crust\t:(Rp.20.000)
5. Crown Crust Carnival\t: (Rp. 25.000)
        """)


    crust_choice = int(input("masukkan pilihan crust (1/2/3/4/5): "))
    while type(crust_choice) == type(1):
        if crust_choice == 1:
            crust = "pan crust"
            harga_crust = 15000
            break
        elif crust_choice == 2:
            crust = "cheese bite crust"
            harga_crust = 20000
            break
        elif crust_choice == 3:
            crust = "chilli cheesy stuffed crust"
            harga_crust = 20000
            break
        elif crust_choice == 4:
            crust = "stuffed crust"
            harga_crust = 20000
            break
        elif crust_choice == 5:
            crust = "crown crust carnival"
            harga_crust = 25000
            break
        else:
            print("pilihan topping tidak sesuai. silahkan ulangi kembali.")
            crust_choice = int(input("masukkan pilihan crust (1/2/3/4/5): "))
    
    #pilih ukuran dengan memasukkan angka2
    print("\npilih ukuran pizza:")
    print("""1. regular ( Rp.50.000)
2. Jumbo (Rp.60.000)
3. Double regular (Rp. 65.000
4. Double jumbo (Rp. 75.000)
          """)
    size_choice = int(input("masukkan pilihan size (1/2/3/4): "))
    while type(size_choice) == type(2):
        if size_choice == 1:
            size = "regular"
            harga_size = 50000
            break
        elif size_choice == 2:
            size = "jumbo"
            harga_size = 60000
            break
        elif size_choice == 3:
            size = "double regular"
            harga_size = 65000
            break
        elif size_choice == 4:
            size = "double jumbo"
            harga_size = 75000
            break
        else:
            print("pilihan topping tidak sesuai. silahkan ulangi kembali.")
            size_choice = int(input("masukkan pilihan size (1/2/3/4): "))
    
    #tambah keju dengan pilihan yes/no
    cheese_choice = input("apakah anda ingin menambahkan extra cheese seharga Rp.10.000? (yes/no): ").lower()
    if cheese_choice == "yes":
        cheese_choice = True
        harga_keju = 10000
    else:
        cheese_choice = False
        harga_keju = 0


    #rumus hitungan dari semua pilihan
    total_harga = harga_topping + harga_crust + harga_size + harga_keju

    #detail pesanan dan tampilan total harga
    print(f"""\n
detail pesanan kamu:
topping: {topping} (Rp. {harga_topping}
crust: {crust} (Rp. {harga_crust})
size: {size} (Rp. {harga_size})"
    """)

    if cheese_choice:
        print(f"tambahan: extra cheese (Rp. {harga_keju})")
    print(f"total harga: Rp. {total_harga}")

    print("\nTerimakasih telah memesan pizza di pizza hut ;) ")

    # memanggil fungsi (def) untuk memulai program
pesan_pizza()