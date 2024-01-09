# FITUR DAN UTILITAS YANG DIIMILIK PEMILIK KOS
import os, utils

folderInformasi = utils.lokasiAbsolut +  "/data/pemilik/informasi/"
folderAkunPenghuni = utils.lokasiAbsolut + "/data/penghuni/"
folderAkunPemilik = utils.lokasiAbsolut + "/data/pemilik/akun/"
fileAkunPemilik = folderAkunPemilik + "akun.txt"

# mendaftarkan akun baru pemilik kos, dengan jumlah max. 1
def daftar():
    while True:
        os.system("cls")
        utils.printHeader("daftar sebagai pemilik")
        
        # jika akun telah ada, memberi pilihan untuk menghapus
        if os.path.isfile(fileAkunPemilik) == True:
            print("Akun pemilik sudah terdaftar!\nSilakan gunakan akun tersebut untuk masuk\natau hapus data terlebih dahulu\nuntuk membuat akun pemilik yang baru\n")
            utils.printMenu("hapus data", "kembali")
            opsiMenu = input("> ")
            if opsiMenu == "1":
                sudahTerhapus = hapusData()
                if sudahTerhapus:
                    continue
            elif opsiMenu == "2":
                return False
            else:
                utils.inputTidakValid()
                continue
        
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
                    print("\nUsername dan nama kos minimal terdiri dari 5 karakter!")
                    utils.pauseClear()
                    
                elif len(password) < 8:
                    print("\nPassword minimal terdiri dari 8 karakter!")
                    utils.pauseClear()
                    
                else:
                    with open(fileAkunPemilik, "w") as dataPemilik:
                        dataPemilik.write(f"{username}\n{password}\n{namaKos}")
                
                    print("\nBerhasil terdaftar!")
                    utils.pauseClear()
                    return True
                
            else:
                print("\nKolom input tidak boleh ada yang kosong!")
                utils.pauseClear()

# menghapus seluruh data yang sudah ada
def hapusData():
    while True:
        os.system("cls")
        utils.printHeader("hapus data")
        print("Ketik (<) pada kolom username untuk\nkembali ke menu sebelumnya\n")
        
        username = input("Username: ")
        if username == "<":
            return False
        password = input("Password: ")
        passwordKonfirmasi = input("Konfirmasi Password: ")
        
        if username.strip() and password.strip() and passwordKonfirmasi.strip():
            
            if os.path.isfile(fileAkunPemilik) == True:
                with open(fileAkunPemilik, "r") as dataPemilik:
                    barisData = dataPemilik.readlines()
            
                dataUsername = barisData[0].strip()
                dataPassword = barisData[1].strip()
                
                if username == dataUsername and password == dataPassword and password == passwordKonfirmasi:
                    konfirmasi = input(f"\nApakah Anda yakin ingin menghapus akun {username}\nbeserta informasi dan semua akun penghuni yang telah terdaftar? ((y)a/(t)idak): ").lower()
                    
                    if konfirmasi == "y":
                        os.remove(fileAkunPemilik)
                        for i in os.listdir(folderInformasi):
                            os.remove(folderInformasi + i)
                        for i in os.listdir(folderAkunPenghuni):
                            os.remove(folderAkunPenghuni + i)
                            
                        print(f"\nBerhasil menghapus seluruh data!")
                        utils.pauseClear()
                        return True
                    elif konfirmasi == "t":
                        return False
                    
                    else:
                        utils.inputTidakValid()
                        continue
                
                elif username != dataUsername:
                    print(f"\nUsername Anda salah")
                    utils.pauseClear()
                    
                elif password != dataPassword:
                    print(f"\nPassword Anda salah")
                    utils.pauseClear()
                    
                elif password != passwordKonfirmasi:
                    print(f"\nPassword konfirmasi tidak cocok")
                    utils.pauseClear()
                    
                else:
                    utils.inputTidakValid()
                    continue
                    
            else:
                print("\nBelum ada akun pemilik yang terdaftar, silakan masuk ke menu daftar!")
                utils.pauseClear()
                return False
        
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

# masuk ke akun yang sudah terdaftar
def masuk():
    while True:
        os.system("cls")
        utils.printHeader("masuk sebagai pemilik")
        
        if not os.path.isfile(fileAkunPemilik):
            print("Akun pemilik belum terdaftar!\nSilakan daftar terlebih dahulu untuk membuat akun baru\n")
            utils.pauseClear()
            return False
        
        print("Ketik (<) pada kolom username untuk\nkembali ke menu [Daftar]\n")
        
        username = input("Username: ")
        if username == "<":
            return False
        password = input("Password: ")

        if username.strip() and password.strip():
            
            if os.path.isfile(fileAkunPemilik) == True:
                with open(fileAkunPemilik, "r") as dataPemilik:
                    barisData = dataPemilik.readlines()
            
                dataUsername = barisData[0].strip()
                dataPassword = barisData[1].strip()
                
                if username == dataUsername and password == dataPassword:
                    print(f"\nBerhasil masuk ke akun {username}!")
                    utils.pauseClear()
                    return True
                
                elif username != dataUsername:
                    print(f"\nUsername Anda salah")
                    utils.pauseClear()
                    
                else:
                    print(f"\nPassword Anda salah")
                    utils.pauseClear()
                
                    
            else:
                print("\nBelum ada akun pemilik yang terdaftar, silakan masuk ke menu daftar!")
                utils.pauseClear()
                return False
        
        else:
            print("\nKolom input tidak boleh ada yang kosong!")
            utils.pauseClear()

# tampilan beranda 
def beranda():
    while True:
        os.system("cls")
        utils.printHeader("beranda")
        
        with open(fileAkunPemilik, "r") as dataPemilik:
            barisData = dataPemilik.readlines()
            
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

# menu informasi dengan beberapa submenu untuk CRUD 
def informasi():
    while True:
        os.system("cls")
        utils.printHeader("informasi")
        utils.printMenu("tambah informasi", "lihat informasi", "edit informasi","hapus informasi", "kembali")
        pilih = input('> ')

        if pilih == '1':
            tambahInformasi()
        elif pilih == '2':
            lihatInformasi()
        elif pilih == '3':
            editInformasi()
        elif pilih == '4':
            hapusInformasi()
        elif pilih == '5':
            break
        else:
            utils.inputTidakValid()

# menambahkan informasi baru dengan judul yang berbeda
# format informasi: judul.txt, isi, dan hari & tanggal
def tambahInformasi():
    while True:
        os.system("cls")
        utils.printHeader('tambah informasi')
        judul = input('Judul Informasi: ').lower() + '.txt'

        if len(judul.rstrip('.txt')) == 0:
            utils.inputKosong()
            continue
        elif judul.rstrip('.txt').replace(" ","").isalpha() == False:
            print('Judul hanya boleh berupa huruf')
            utils.pauseClear()
            continue
        else:
            if judul in os.listdir(folderInformasi):
                print('Judul sudah ada')
                utils.pauseClear()
                continue
            isi = input('Isi: ')
            judul = judul.rstrip('.txt')
            if judul.strip() and isi.strip():
                isi = f'{isi}\n\n{utils.hariTanggal()}'
                with open(f'{folderInformasi}{judul}.txt', 'w') as file:
                    file.write(isi)

                print('Informasi berhasil ditambahkan\n')
                
            else:
                utils.inputKosong()
                continue

            lanjut = input('Apakah anda ingin lanjut membuat informasi? ((y)a/(t)idak): ').lower()

            if lanjut == 'y':
                continue
            elif lanjut == 't':
                print('Terimakasih\n')
                break
            else:
                utils.inputTidakValid()
                break

# menampilkan informasi yang telah tersedia di folder informasi
# digunakan di bagian pemilik dan penghuni
def lihatInformasi():
    os.system("cls")
    utils.printHeader("lihat informasi")
    
    if not os.listdir(folderInformasi):
            print('Belum ada informasi yang ditambahkan')
            
    else:
        for judul in os.listdir(folderInformasi):
            print(utils.border)
            print(f"{judul.strip('.txt').title()}")
            with open(f'{folderInformasi}{judul}', 'r') as file:
                data = file.read()
            print(data)
            print(utils.border)

    utils.pauseClear()

# mengubah isi informasi dan mengganti hari & tanggal dengan yang baru
def editInformasi():
    while True:
        os.system("cls")
        utils.printHeader('edit informasi')
        
        if not os.listdir(folderInformasi):
            print('Belum ada informasi yang ditambahkan')
            utils.pauseClear()
            break
            
        else:
            judul = input('Judul Informasi: ').lower()
            if utils.cariFile(folderInformasi, judul) == True:
                print(f"Judul: {judul.strip('.txt')}")
                with open(f'{folderInformasi}{judul}.txt', 'r') as file:
                    data = file.read()
                print(data)

                perintah = input('Apakah anda ingin mengedit informasi? ((y)a/(t)idak): ').lower()

                if perintah == 'y':
                    isi = input('Isi informasi baru: ')
                    hari = utils.hariTanggal()
                    isi = f'{isi}\n\nDiedit/diperbarui pada: {hari}'
                    with open(f'{folderInformasi}{judul}.txt', 'w') as file1:
                        file1.write(isi)
                    print('Informasi berhasil diubah')
                    utils.pauseClear()
                    return
                elif perintah == 't':
                    return
                else:
                    utils.inputTidakValid()
                    break
            else:
                print('Judul belum dibuat')
                utils.pauseClear()
                return

# menghapus informasi yang ada pada folder informasi
def hapusInformasi():
    while True:
        os.system("cls")
        utils.printHeader('hapus informasi')
        
        if not os.listdir(folderInformasi):
            print('Belum ada informasi yang ditambahkan')
            utils.pauseClear()
            break
            
        else:
            judul = input('Judul Informasi: ').lower()
            if utils.cariFile(folderInformasi, judul) == True:
                with open(f'{folderInformasi}{judul}.txt', 'r') as file:
                    data = file.read()
                print(data)
                perintah = input('Apakah anda ingin menghapus informasi? ((y)a/(t)idak): ').lower()

                if perintah == 'y':
                    os.remove(f'{folderInformasi}{judul}.txt')
                    print('Informasi berhasil dihapus')
                    utils.pauseClear()
                    return
                if perintah == 't':
                    return
                else:
                    utils.inputTidakValid()
                    break
            else:
                print('Judul belum dibuat')
                utils.pauseClear()
                return

# menampilkan riwayat pembayaran berdasarkan username penghuni kos
def pembayaran():
    while True:
        os.system("cls")
        utils.printHeader("Pembayaran")
        utils.printMenu("tampilkan bukti pembayaran", "kembali")

        pilihan = input("> ")

        if pilihan == '1':
           usernamePenghuni = input("\nMasukkan Nama Penghuni: ")
           if utils.cariFile(folderAkunPenghuni, usernamePenghuni) == True:
                with open(folderAkunPenghuni + f"{usernamePenghuni}.txt", "r") as dataPenghuni:
                    barisData = dataPenghuni.readlines()

                if len(barisData) >= 4:
                    for i in barisData[3:]:
                        print(f"{i}")
                    utils.pauseClear()
                    continue

                else:
                    print("\nPenghuni belum memiliki riwayat pembayaran")
                    utils.pauseClear()
                    continue
           else:
               print("Nama Penghuni salah")
               utils.pauseClear()
               continue
           
        elif pilihan == '2':
            break

        else:
            utils.inputTidakValid()