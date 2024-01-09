# STRUKTUR UTAMA PROGRAM
import utils, utilsPemilik, utilsPenghuni, os

def main():
    while True:
        os.system("cls")
        utils.printHeader("selamat datang di ekos")
        utils.printMenu("pemilik", "penghuni", "keluar")
        pengguna = input("> ")
        
        if pengguna == "1":
            while True:
                os.system("cls")
                utils.printHeader("daftar/masuk sebagai pemilik")
                utils.printMenu("daftar", "masuk", "kembali")
                
                opsiMenu = input("> ")
                
                if opsiMenu == "1":
                    sudahTerdaftar = utilsPemilik.daftar()
                    if sudahTerdaftar:
                        continue
                
                elif opsiMenu == "2":
                    sudahMasuk = utilsPemilik.masuk()
                    if sudahMasuk == True:
                        utilsPemilik.beranda()
                    else:
                        utilsPemilik.daftar()

                elif opsiMenu == "3":
                    break
                    
                else:
                    utils.inputTidakValid()
                
        elif pengguna == "2":
            while True:
                os.system("cls")
                utils.printHeader("daftar/masuk sebagai penghuni")
                utils.printMenu("daftar", "masuk", "kembali")
                
                opsiMenu = input("> ")
                
                if opsiMenu == "1":
                    sudahTerdaftar = utilsPenghuni.daftar()
                    if sudahTerdaftar:
                        continue
                
                elif opsiMenu == "2":
                    sudahMasuk = utilsPenghuni.masuk()
                    if sudahMasuk == True:
                        utilsPenghuni.beranda()
                    elif sudahMasuk == None:
                        continue
                    else:
                        utilsPenghuni.daftar()

                elif opsiMenu == "3":
                    break
                    
                else:
                    utils.inputTidakValid()
        
        elif pengguna == "3":
            os.system("cls")
            exit()
            
        else:
            print("\nMasukkan input yang valid!")
            utils.pauseClear()

main()