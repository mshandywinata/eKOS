# FITUR DAN UTILITAS YANG DIMILIKI PENGHUNI KOS
import os, utils, utilsPemilik

folderAkunPenghuni = utils.lokasiAbsolut + "/data/penghuni/"

# mendaftarkan penghuni kos dengan prasyarat nama kos harus sesuai dengan pemilik yang terdaftar
def daftar():
    while True:
        os.system("cls")
        utils.printHeader("daftar sebagai penghuni")
        
        # memastikan jika akun pemilik sudah terdaftar
        if not os.listdir(utilsPemilik.folderAkunPemilik):
            print("Akun pemilik belum terdaftar!")
            print("Silakan daftarkan akun pemilik terlebih dahulu!")
            utils.pauseClear()
            return False
        
        else:
            print("Ketik (<) pada kolom username untuk\nkembali ke menu sebelumnya\n")
            username = input("Username: ")
            if username == "<":
                return False
            
            password = input("Password: ")
            namaKos = input("Nama Kos: ")
            
            if username.strip() and password.strip() and namaKos.strip():
                
                if username.replace(" ", "").isalpha() == False or namaKos.replace(" ", "").isalpha() == False:
                    print("\nUsername dan nama kos hanya boleh berupa huruf!")
                    utils.pauseClear()
                
                elif len(username) < 5 or len(namaKos) < 5:
                    print("\nUsername dan nama kos minimal 5 karakter!")
                    utils.pauseClear()
                    
                elif len(password) < 8:
                    print("\nPassword minimal 8 karakter!")
                    utils.pauseClear()
                
                else:
                    with open(utilsPemilik.fileAkunPemilik, "r") as dataPemilik:
                        barisData = dataPemilik.readlines()
                    namaKosPemilik = barisData[2].strip()
                
                    if utils.cariFile(folderAkunPenghuni, username) == True:
                        print(f"\nAkun dengan username {username} sudah terdaftar")
                        print("Silakan gunakan username lain atau masuk dengan username tersebut!")
                        utils.pauseClear()
                        return True
                    
                    elif namaKos != namaKosPemilik:
                        print(f"\nNama kos kamu salah!\nPastikan nama kos cocok dengan nama kos yang terdaftar pada akun pemilik.")
                        utils.pauseClear()
                
                    else:
                        with open(folderAkunPenghuni + f"{username}.txt", "w") as dataPenghuni:
                            dataPenghuni.write(f"{username}\n{password}\n{namaKos}")
                    
                        print("\nBerhasil terdaftar!")
                        utils.pauseClear()
                        return True
                
            else:
                utils.inputKosong()

# masuk ke akun penghuni yang sudah terdaftar
def masuk():
    while True:
        os.system("cls")
        utils.printHeader("masuk sebagai penghuni")
        
        if not os.listdir(utilsPemilik.folderAkunPemilik):
            print("Akun pemilik belum terdaftar!\nSilakan daftarkan akun pemilik terlebih dahulu!")
            utils.pauseClear()
            return None
        
        elif not os.listdir(folderAkunPenghuni):
            print("Belum ada akun penghuni yang terdaftar!\nSilakan daftar terlebih dahulu!")
            utils.pauseClear()
            return False
        
        else:
            print("Ketik (<) pada kolom username untuk\nkembali ke menu [Daftar]\n")
            global username
            username = input("Username: ")
            if username == "<":
                return False
            
            password = input("Password: ")

            if username.strip() and password.strip():
                if utils.cariFile(folderAkunPenghuni, username) == True:
                    with open(folderAkunPenghuni + f"{username}.txt", "r") as dataPenghuni:
                        barisData = dataPenghuni.readlines()
                
                    dataUsername = barisData[0].strip()
                    dataPassword = barisData[1].strip()
                    
                    if username == dataUsername and password == dataPassword:
                        print(f"\nBerhasil masuk ke akun {username}!")
                        utils.pauseClear()
                        return True
                    
                    elif username != dataUsername:
                        print(f"\nUsername kamu salah")
                        utils.pauseClear()
                        
                    else:
                        print(f"\nPassword kamu salah")
                        utils.pauseClear()
                        
                else:
                    print("\nAkun kamu belum terdaftar, silakan masuk ke menu daftar!")
                    utils.pauseClear()
                    return False
            
            else:
                utils.inputKosong()

# tampilan beranda 
def beranda():
    while True:
        os.system("cls")
        utils.printHeader("beranda")
        
        with open(folderAkunPenghuni + f"/{username}.txt", "r") as dataPenghuni:
            barisData = dataPenghuni.readlines()
            
        dataUsername = barisData[0].strip()
        dataNamaKos = barisData[2].strip()
        
        print(f"Selamat datang di Kos {dataNamaKos}")
        print(f"Selamat {utils.waktu()}, {dataUsername}!\n")
        utils.printMenu("informasi", "pembayaran", "keluar")
        
        inputMenu = input("> ")
        
        if inputMenu == "1":
            informasi()
        elif inputMenu == "2":
            pembayaran()
        elif inputMenu == "3":
            break
        else:
            utils.inputTidakValid()

# tampilan menu informasi dengan submenu lihat informasi
def informasi():
    while True:
        os.system("cls")
        utils.printHeader("informasi")
        utils.printMenu("lihat informasi", "kembali")
        pilih = input('> ')

        if pilih == '1':
            utilsPemilik.lihatInformasi()
        elif pilih == '2':
            break
        else:
            utils.inputTidakValid()

# tampilan menu pembayaran dengan submenu tambah pembayaran
def pembayaran():
   while True:
        os.system("cls")
        utils.printHeader("Pembayaran")
        utils.printMenu("tambah pembayaran", "kembali")
        pilihan = input("> ")

        if pilihan == "1":
            tambahPembayaran()
        elif pilihan == "2":
            break
        else:
            utils.inputTidakValid()

# menambahkan riwayat pembayaran
# ditulis pada file akun penghuni pada baris selanjutnya
# dengan format [tanggal] tujuan: nominal
def tambahPembayaran():
    while True:
        os.system("cls")
        utils.printHeader("Tambah Pembayaran")
        tanggal = utils.hariTanggal()
        tujuan = input("Tujuan Pembayaran: ")
        nominal = input("Nominal: Rp")

        if tujuan.strip() and nominal.strip():    
            if tujuan.replace(" ", "").isalpha() == False or nominal.isdigit() == False:
                print("\nInput tujuan pembayaran hanya boleh berupa huruf dan input harga hanya boleh berupa angka!")
                utils.pauseClear()
                
            else:
                with open(f"{folderAkunPenghuni}{username}.txt", "a") as file:
                    file.writelines(f"\n[{tanggal}] {tujuan}: Rp{nominal}")
                
                print("Pembayaran Berhasil")
                utils.pauseClear()
                break
        
        else:
            utils.inputKosong()