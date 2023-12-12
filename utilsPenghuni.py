import os, utils, utilsPemilik

def daftar():
    while True:
        os.system("cls")
        utils.printHeader("daftar")

        username = input("Username: ")
        password = input("Password: ")
        namaKos = input("Nama Kos: ")
        
        if username.strip() and password.strip() and namaKos.strip():
            
            akunPenghuni = utils.absolutePath() + f"/data/penghuni/{username}.txt"

            try:
                dataPenghuni = open(akunPenghuni, "r")
                print(f"\nAkun dengan username {username} sudah terdaftar")
                print("Silakan gunakan username lain atau masuk dengan username tersebut!")
                utils.pauseClear()
                return True
            
            except FileNotFoundError:
                dataPenghuni = open(akunPenghuni, "w")
                dataPenghuni.write(f"{username}\n{password}\n{namaKos}")
                dataPenghuni.close()
            
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

        if username.strip() and password.strip():
            try:
                akunPenghuni = utils.absolutePath() + f"/data/penghuni/{username}.txt"
                dataPenghuni = open(akunPenghuni, "r")
                barisData = dataPenghuni.readlines()
                dataUsername = barisData[0].rstrip("\n")
                dataPassword = barisData[1].rstrip("\n")
                dataNamaKos = barisData[2].rstrip("\n")
                dataPenghuni.close()
                
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
        elif inputMenu == "3":
            break
        else:
            print("\nMasukkan inputan yang valid!")
            utils.pauseClear()

def informasi():
    while True:
        os.system("cls")
        utils.printHeader("informasi")
        utils.printMenu("lihat informasi", "kembali")
        
        inputMenu = input("> ").lower()
        
        if inputMenu == "1":
            utilsPemilik.lihatInformasi()
            continue
        elif inputMenu == "2":
            break
        else:
            print("\nMasukkan inputan yang valid!")
            utils.pauseClear()
