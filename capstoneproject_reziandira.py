# Daftar Stock

stock_barang = {

                "laptop_1":{"Nama":"Macbook Air M2(2022)", "Spesifikasi":"Chip Apple M2, RAM 24 GB, SSD 2 TB \t", "Merk":"Apple \t", "Kategori":"Laptop", "Unit":5, "Harga":20000000},
                "laptop_2":{"Nama":"Swift 5 Aerospace", "Spesifikasi":"Intel Core i7,RAM 16 GB,SSD 512 GB \t", "Merk":"Acer \t", "Kategori":"Laptop", "Unit":7, "Harga":21000000},
                "laptop_3":{"Nama":"ROG STRIX G17 G713RM", "Spesifikasi":"RYZEN 7-6800H, RAM 16 GB,SSD 512 GB \t", "Merk":"Asus \t", "Kategori":"Laptop", "Unit":10, "Harga":22000000},
                "hp_1":{"Nama":"iPhone 13 Pro Max", "Spesifikasi":"Apple A15 Bionic,Warna:Blue, RAM 512 GB", "Merk":"Apple \t", "Kategori":"Handphone", "Unit":15, "Harga":25000000},
                "hp_2":{"Nama":"Galaxy S22 Ultra 5G", "Spesifikasi":"Snapdragon 8,Warna:Black,RAM 12/256 GB", "Merk":"Samsung", "Kategori":"Handphone", "Unit":10, "Harga":19000000},
                "hp_3":{"Nama":"GP50 Pro \t", "Spesifikasi":"Snapdragon 888 4G,Warna:Gold,RAM 8/256 GB", "Merk":"Huawei ", "Kategori":"Handphone", "Unit":3, "Harga":13000000},
                "tablet_1":{"Nama":"iPad Pro (Gen 3)", "Spesifikasi":"Chip Apple M1, Warna : Space Grey, WIFI 1 TB", "Merk":"Apple \t", "Kategori":"Tablet", "Unit":5, "Harga":27000000},
                "tablet_2":{"Nama":"Galaxy Tab S8 Ultra", "Spesifikasi":"Snapdragon 8, Warna : Black, RAM 12/256 GB", "Merk":"Samsung", "Kategori":"Tablet", "Unit":2, "Harga":17000000},
                "tablet_3":{"Nama":"MatePad Pro 11", "Spesifikasi":"Snapdragon 870,Warna:Black, RAM 8/256 GB", "Merk":"Huawei ", "Kategori":"Tablet", "Unit":4, "Harga":12000000},

}      

def daftar_stock():
    while len(stock_barang)==0:
        print("Maaf, Tidak ada stock yang tersedia")
        break

    else:
        while True:
            pilihan_menu = int(input("\n ----- DAFTAR GADGET ----- \n \n 1. Laptop \n 2. Handphone \n 3. Tablet \n 4. Daftar Seluruh Gadget \n 5. Cari dengan Keyword \n 6. Kembali ke Menu Utama  \n\n Masukkan Pilihan Anda (1-6): "))
            if pilihan_menu == 1:
                    print(" Koleksi Gadget Terbaru Kami \n\n | Nama Gadget \t\t| Spesifikasi \t\t\t\t\t|Merk \t | Kategori \t| Stok \t| Harga Satuan")
                    for key in stock_barang.keys():
                        if stock_barang [key] ["Kategori"] == "Laptop":
                            print(" |{} \t|{} \t|{} |{} \t|{} \t|{} ".format(stock_barang[key]["Nama"], stock_barang[key]["Spesifikasi"], stock_barang[key]["Merk"], stock_barang[key]["Kategori"], stock_barang[key]["Unit"], stock_barang[key]["Harga"]))
                        else:
                            continue

            elif pilihan_menu == 2:
                    print(" Koleksi Gadget Terbaru Kami \n\n | Nama Gadget \t\t| Spesifikasi \t\t\t\t\t|Merk \t | Kategori \t| Stok \t| Harga Satuan")
                    for key in stock_barang.keys():
                        if stock_barang [key] ["Kategori"] == "Handphone":
                            print(" |{} \t|{} \t|{} |{} \t|{} \t|{} ".format(stock_barang[key]["Nama"], stock_barang[key]["Spesifikasi"], stock_barang[key]["Merk"], stock_barang[key]["Kategori"], stock_barang[key]["Unit"], stock_barang[key]["Harga"]))
                        else:
                            continue

            elif pilihan_menu == 3:
                    print(" Koleksi Gadget Terbaru Kami \n\n | Nama Gadget \t\t| Spesifikasi \t\t\t\t\t| Merk \t | Kategori \t| Stok \t| Harga Satuan")
                    for key in stock_barang.keys():
                        if stock_barang [key] ["Kategori"] == "Tablet":
                            print(" |{} \t|{} \t|{} |{} \t|{} \t| {} ".format(stock_barang[key]["Nama"], stock_barang[key]["Spesifikasi"], stock_barang[key]["Merk"], stock_barang[key]["Kategori"], stock_barang[key]["Unit"], stock_barang[key]["Harga"]))
                        else:
                            continue

            elif pilihan_menu == 4:
                    print(" Koleksi Gadget Terbaru Kami \n\n | Nama Gadget \t\t| Spesifikasi \t\t\t\t\t|Merk \t \t| Kategori \t| Stok \t| Harga Satuan")
                    for key in stock_barang.keys():
                        print(" |{} \t|{} \t|{} \t|{} \t|{} \t| {} ".format(stock_barang[key]["Nama"], stock_barang[key]["Spesifikasi"], stock_barang[key]["Merk"], stock_barang[key]["Kategori"], stock_barang[key]["Unit"], stock_barang[key]["Harga"]))

            elif pilihan_menu == 5:
                cari_gadget = input("Masukkan Nama Gadget yang dicari: ")
                
                for key in stock_barang.keys():
                    if stock_barang [key] ["Nama"] == cari_gadget:
                        print(" Koleksi Gadget Terbaru Kami \n\n | Nama Gadget \t\t| Spesifikasi \t\t\t\t\t| Merk \t \t | Kategori \t| Stok \t| Harga Satuan")
                        # for key in stock_barang.keys():
                            # if cari_gadget.lower() in stock_barang [key]["Nama"].lower():
                        print(" | {} \t| {} \t| {} | {} \t| {} \t| {} ".format(stock_barang[key]["Nama"], stock_barang[key]["Spesifikasi"], stock_barang[key]["Merk"], stock_barang[key]["Kategori"], stock_barang[key]["Unit"], stock_barang[key]["Harga"]))
                    else:
                        continue
                    break

                else:
                    print("Nama Gadget yang Anda cari tidak ada")

                    

            elif pilihan_menu == 6:
                menu_utama()
            
        
        else:
            print("Menu yang anda pilih tidak tersedia. Silahkan dicoba lagi.")             
            
# print(daftar_stock())

def semua_stock ():
    if len(stock_barang) == 0:
        print("Tidak ada stok yang tersedia")
    else:
        print(" \n\nKoleksi Gadget Terbaru Kami \n\n | Nama Gadget \t\t| Spesifikasi \t\t\t\t\t|Merk \t \t| Kategori \t| Stok \t| Harga Satuan")
        for key in stock_barang.keys():
            print(" |{} \t|{} \t|{} \t|{} \t|{} \t| {} ".format(stock_barang[key]["Nama"], stock_barang[key]["Spesifikasi"], stock_barang[key]["Merk"], stock_barang[key]["Kategori"], stock_barang[key]["Unit"], stock_barang[key]["Harga"]))

def tambah_gadget():
    
    while True:

        print('''
        --------------------------
        MENU MENAMBAH GADGET BARU
        --------------------------

        1. Menambahkan Gadget
        2. Kembali ke Menu Utama
        ''')

        pilihan = int(input('Masukkan pilihan Anda: '))

        if pilihan == 1:

            nama_gadget = input("Masukkan Nama Gadget yang Ingin Ditambahkan: ")
       
            for key in stock_barang.keys():
                if stock_barang [key] ["Nama"] == nama_gadget :
                    print("Gadget yang Anda masukkan sudah Ada di Stock kami")
                    break

               
            else :
                tambah_spesifikasi = input("Masukkan Spesifikasi Gadget : ")
            
                tambah_merk = input("Masukkan Merk Gadget: ")

                tambah_kategori = input("Masukkan Kategori Gadget: ")

                tambah_stock = int(input("Masukkan Stock Gadget: "))

                tambah_harga = int(input("Masukkan Harga Satuan Gadget: "))
            
            
                cek = input("Apakah Anda yakin ingin menambahkan Gagdet {}, dengan Nama : {}, Spesifikasi : {}, Merk : {}, sebanyak {} dengan harga {} (Ya/Tidak)".format(tambah_kategori, nama_gadget, tambah_spesifikasi, tambah_merk, tambah_stock, tambah_harga))
                if cek != "Ya".lower():
                    break
            
                else:
                    stock_barang[nama_gadget.lower()] = {"Nama":nama_gadget, "Spesifikasi":tambah_spesifikasi, "Merk":tambah_merk, "Kategori":tambah_kategori, "Unit":tambah_stock, "Harga":tambah_harga }
                    semua_stock()
                    break

            

        elif pilihan == 2:
            menu_utama()

# print(tambah_gadget())

def ubah_gadget ():
    
    while True:

        print('''
            --------------------------
                MENU MENGUBAH GADGET
            --------------------------

            1. Mengubah Gadget
            2. Kembali ke Menu Utama
            ''')

        pilihan = int(input('Masukkan pilihan Anda: '))

        if pilihan == 1:
    
            semua_stock()

            pilih_gadget = input("\n Masukkan Nama Gadget yang Mau Diubah Datanya: ")
    
            for key in stock_barang.keys():
                if stock_barang [key] ["Nama"] == pilih_gadget :

                    jenis_perubahan = int(input("----- PILIH JENIS PERUBAHAN ----- \n\n1. Nama \n2. Spesifikasi \n3. Merk \n4. Kategori \n5. Stok \n6. Harga Satuan \n7. Kembali ke Menu Sebelumnya \n\n Jenis Perubahan (1-7): "))
        
                    if jenis_perubahan == 1:
                
                        nama_baru = input("Masukkan Nama Gadget Baru: ")

                        for key in stock_barang.keys():
                            if stock_barang [key] ["Nama"] == nama_baru :
                                print("Nama Gadget Sudah Ada, Masukkan Nama Baru")
                                nama_baru = input("Masukkan Nama Gadget Baru: ")

                        else :
                            cek2 = input("Apakah anda yakin ingin mengubah nama {} menjadi {}? (Ya/Tidak): ".format(pilih_gadget, nama_baru))
                            if cek2 != "Ya".lower():
                                break
                            
                            else:
                                for key in stock_barang.keys():
                                    if stock_barang [key] ["Nama"] == pilih_gadget:
                                        stock_barang[key]["Nama"] = nama_baru
                                        semua_stock()
                                        break
           
                    elif jenis_perubahan == 2:
            
                        spesifikasi_baru = input("Masukkan Spesifikasi Gadget Baru: ")
                
                        cek3 = input("Apakah anda yakin ingin mengubah spesifikasi {} menjadi {} ? (Ya/Tidak): ".format(pilih_gadget, spesifikasi_baru))
                
                        if cek3 != "Ya".lower():
                            break
                        else:
                            for key in stock_barang.keys():
                                if stock_barang [key] ["Nama"] == pilih_gadget:
                                    stock_barang[key]["Spesifikasi"] = spesifikasi_baru
                                    semua_stock()
                                    break

                    elif jenis_perubahan == 3:
                
                        merk_baru = input("Masukkan Merk Gadget Baru: ")
                
                        cek4 = input("Apakah anda yakin ingin mengubah merk {} menjadi {}? (Ya/Tidak): ".format(pilih_gadget, merk_baru))
            
                        if cek4 !="Ya".lower():
                            break
                        else:
                            for key in stock_barang.keys():
                                if stock_barang [key] ["Nama"] == pilih_gadget: 
                                    stock_barang[key]["Merk"] = merk_baru
                                    semua_stock()
                                    break

                    elif jenis_perubahan == 4:

                        kategori_baru = (input("Masukkan Kategori Gadget Baru: "))

                        cek5 = input("Apakah anda yakin ingin mengubah kategori {} menjadi {}? (Ya/Tidak): ".format(pilih_gadget, kategori_baru))
                
                        if cek5 != "Ya".lower():
                            break
                        else:
                            for key in stock_barang.keys():
                                if stock_barang [key] ["Nama"] == pilih_gadget: 
                                    stock_barang [key] ["Kategori"] = kategori_baru
                                    semua_stock()
                                    break

                    elif jenis_perubahan == 5:

                        stok_baru = int(input("Masukkan Stok Gadget Baru: "))

                        cek6 = input("Apakah anda yakin ingin mengubah stok {} menjadi {}? (Ya/Tidak): ".format(pilih_gadget, stok_baru))
                
                        if cek6 != "Ya".lower():
                            break
                        else:
                            for key in stock_barang.keys():
                                if stock_barang [key] ["Nama"] == pilih_gadget: 
                                    stock_barang [key] ["Unit"] = stok_baru
                                    semua_stock()
                                    break

                    elif jenis_perubahan == 6:

                        harga_baru = int(input("Masukkan Harga Gadget Baru: "))

                        cek7 = input("Apakah anda yakin ingin mengubah harga {} menjadi {}? (Ya/Tidak): ".format(pilih_gadget, harga_baru))
                
                        if cek7 != "Ya".lower():
                            break
                        else:
                            for key in stock_barang.keys():
                                if stock_barang [key] ["Nama"] == pilih_gadget: 
                                    stock_barang [key] ["Harga"] = harga_baru
                                    semua_stock()
                                    break

                    else:
                        break

                    break
            else:
                print("Nama Gadget yang Anda masukkan tidak ada.")

        elif pilihan == 2:
            menu_utama()

# print(ubah_gadget())

def hapus_gadget ():

    while True:

        print('''
            --------------------------
                MENU MENGHAPUS GADGET
            --------------------------

            1. Menghapus Gadget
            2. Kembali ke Menu Utama
            ''')

        pilihan = int(input('Masukkan pilihan Anda: '))

        if pilihan == 1:
    
            semua_stock()

            nama_gadget = input ("\n\nMasukkan Nama Gadget yang ingin dihapus : ")

            for key in stock_barang.keys():
                    if stock_barang [key] ["Nama"] == nama_gadget:
        
                        cek8 = input("Apakah anda yakin ingin menghapus seluruh informasi untuk gadget {}? (Ya/Tidak): ".format(nama_gadget))
        
                        while cek8 != "Ya".lower():
                            break
        
                        else:
                            del stock_barang [key]
                            semua_stock()
                            break
                            # for i in stock_barang.keys():
                            #     if stock_barang [i] ["Nama"] == nama_gadget: 
                            #         del stock_barang [i]
                            #         semua_stock()
                            #         break

            else:
                print("\n\nNama Gadget yang Anda cari tidak ada")

        elif pilihan == 2:
            menu_utama()



def menu_utama():
    while True:
        menu = int(input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n WELCOME TO REZI GADGET STORE \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n\n1. Daftar Stock Gadget \n2. Menambah Gadget \n3. Mengubah Gadget \n4. Menghapus Gadget \n5. Exit \n\n\n Masukkan pilihan Anda(1-5) "))

        while menu == 1:
            daftar_stock()
    
        while menu == 2:
            tambah_gadget()

        while menu == 3:
            ubah_gadget()
    
        while menu == 4:
            hapus_gadget()

        else :
            break

print(menu_utama())