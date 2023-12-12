import os, utils

folderInformasi = utils.absolutePath() +  f"/data/pemilik/informasi/"
akunPemilik = utils.absolutePath() + f"/data/pemilik/akun/akun.txt"

def daftar():
    while True:
        os.system("cls")
        utils.printHeader("daftar")

        username = input("Username: ")
        password = input("Password: ")
        namaKos = input("Nama Kos: ")
        
        if username.strip() and password.strip() and namaKos.strip():
            try:
                dataPemilik = open(akunPemilik, "r")
                print(f"\nAkun pemilik Kos sudah terdaftar")
                print("Silakan gunakan akun tersebut untuk masuk!")
                utils.pauseClear()
                return True
            
            except FileNotFoundError:
                dataPemilik = open(akunPemilik, "w")
                dataPemilik.write(f"{username}\n{password}\n{namaKos}")
                dataPemilik.close()
            
                print("\nBerhasil terdaftar!")
                utils.pauseClear()
                return True
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

def masuk():
    while True:
        os.system("cls")
        utils.printHeader("masuk")
        
        global username
        username = input("Username: ")
        password = input("Password: ")
        global namaKos
        namaKos = input("Nama Kos: ")

        if username.strip() and password.strip() and namaKos.strip():
            try:
                dataPemilik = open(akunPemilik, "r")
                barisData = dataPemilik.readlines()
                dataUsername = barisData[0].rstrip("\n")
                dataPassword = barisData[1].rstrip("\n")
                dataNamaKos = barisData[2].rstrip("\n")
                dataPemilik.close()
                
                if username == dataUsername and password == dataPassword and namaKos == dataNamaKos:
                    print(f"\nBerhasil masuk ke akun {username}!")
                    utils.pauseClear()
                    return True

                elif username != dataUsername or password != dataPassword:
                    print(f"\nUsername atau password kamu salah")
                    utils.pauseClear()
                else:
                    print(f"\nNama kos kamu salah")
                    utils.pauseClear()
                    
            except FileNotFoundError:
                print("\nAkun kamu belum terdaftar, silakan masuk ke menu daftar!")
                utils.pauseClear()
                return False
        
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

def beranda():
    while True:
        os.system("cls")
        utils.printHeader("beranda")
        print(f"Selamat datang di Kos {namaKos}")
        print(f"Selamat {utils.waktu()}, {username}!\n")
        utils.printMenu("informasi", "pembayaran", "keluar")
        
        inputMenu = input("> ").lower()
        
        if inputMenu == "1":
            informasi()
            continue
        elif inputMenu == "2":
            print("\nFitur ini belum tersedia, maaf!")
            utils.pauseClear()
            continue
        elif inputMenu == "3":
            break
        else:
            print("\nMasukkan inputan yang valid!")
            utils.pauseClear()

def informasi():
    while True:
        os.system("cls")
        utils.printHeader("informasi")
        utils.printMenu("lihat informasi", "tambah informasi", "ubah informasi", "hapus informasi", "kembali")
        
        inputMenu = input("> ").lower()
        
        if inputMenu == "1":
            lihatInformasi()
            continue
        elif inputMenu == "2":
            tambahInformasi()
            continue
        elif inputMenu == "3":
            ubahInformasi()
        elif inputMenu == "4":
            ditemukan = hapusInformasi()
            if ditemukan:
                continue
            else:
                print("\nTidak ada informasi dengan judul tersebut!")
                utils.pauseClear()
        elif inputMenu == "5":
            break
        else:
            print("\nMasukkan inputan yang valid!")
            utils.pauseClear()

def lihatInformasi():
    os.system("cls")
    utils.printHeader("lihat informasi")
    
    if not os.listdir(folderInformasi):
        print("\nBelum ada informasi yang ditambahkan!")
        utils.pauseClear()
        return False
    else:
        print()
        for file in os.listdir(folderInformasi):
            if file.endswith(".txt"):
                print(f"\nJudul: {file.rstrip('.txt')}")
                print(f"Isi: {open(folderInformasi + file, 'r').read()}\n")
        
    utils.pauseClear()
            
def tambahInformasi():
    while True:
        os.system("cls")
        utils.printHeader("tambah informasi")
        judul = input("Judul: ").title()
        isi = input("Isi: ")
        
        if judul.strip() and isi.strip():
            informasi = open(folderInformasi + f"{judul}.txt", "w")
            hariTanggal = utils.hariTanggal()
            isi = f"{isi}\n\nDiunggah pada: {hariTanggal}"
            informasi.write(isi)
            
            print("\nBerhasil menambahkan informasi!")
            utils.pauseClear()
            break
            
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

def ubahInformasi():
    while True:
        os.system("cls")
        utils.printHeader("ubah informasi")
        judul = input("Judul: ").title()
        
        if judul.strip():
            for file in os.listdir(folderInformasi):
                if file.endswith(".txt"):
                    if file.rstrip(".txt") == judul:
                        print(f"\nJudul: {file.rstrip('.txt')}")
                        print(f"Isi: {open(folderInformasi + file, 'r').read()}\n")
                        
                        while True:
                            print("Apakah kamu ingin mengubah informasi tersebut? (y/t)")
                            inputMenu = input("> ").lower()
                            
                            if inputMenu == "y":
                                isi = input("Isi: ")
                                hariTanggal = utils.hariTanggal()
                                isi = f"{isi}\n\nDiunggah pada: {hariTanggal}"
                                informasi = open(folderInformasi + f"{judul}.txt", "w")
                                informasi.write(isi)
                                
                                print("\nBerhasil mengubah informasi!")
                                utils.pauseClear()
                                break
                                
                            elif inputMenu == "t":
                                break
                                
                            else:
                                print("\nMasukkan input yang valid!")
                                utils.pauseClear()
                                
                        return
                else:
                    print("\nBelum ada informasi yang dibuat")
                    utils.pauseClear()
                    break
                
            print("\nTidak ada informasi dengan judul tersebut!")
            utils.pauseClear()
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

def hapusInformasi():
    while True:
        os.system("cls")
        utils.printHeader("hapus informasi")
        judul = input("Judul: ").title()
        
        if judul.strip():
            for file in os.listdir(folderInformasi):
                if file.endswith(".txt"):
                    if file.rstrip(".txt") == judul:
                        print(f"\nJudul: {file.rstrip('.txt')}")
                        print(f"Isi: {open(folderInformasi + file, 'r').read()}\n")
                        
                        while True:
                                print("Apakah kamu ingin menghapus informasi tersebut? (y/t)")
                                inputMenu = input("> ").lower()
                                
                                if inputMenu == "y":
                                    os.remove(folderInformasi + file)
                                    print("\nBerhasil menghapus informasi!")
                                    utils.pauseClear()
                                    break
                                    
                                elif inputMenu == "t":
                                    break
                                    
                                else:
                                    print("\nMasukkan input yang valid!")
                                    utils.pauseClear() 
                        return
                else:
                    print("\nBelum ada informasi yang dibuat")
                    utils.pauseClear()
                    break
                
            print("\nTidak ada informasi dengan judul tersebut!")
            utils.pauseClear()  
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

def pembayaran():
    pass
