import utils, utilsPemilik, utilsPenghuni
import os

def main():
    while True:
        os.system("cls")
        utils.printHeader("selamat datang di ekos")
        utils.printMenu("pemilik", "penghuni", "keluar")
        peran = input("> ").lower()
        
        if peran == "1":
            while True:
                os.system("cls")
                utils.printHeader("daftar/masuk sebagai pemilik")
                utils.printMenu("daftar", "masuk", "kembali")
                
                opsiMenu = input("> ").lower()
                os.system("cls")
                
                if opsiMenu == "1":
                    sudahTerdaftar = utilsPemilik.daftar()
                    if sudahTerdaftar:
                        continue
                
                elif opsiMenu == "2":
                    sudahMasuk = utilsPemilik.masuk()
                    if sudahMasuk:
                        utilsPemilik.beranda()
                    else:
                        utilsPemilik.daftar()

                elif opsiMenu == "3":
                    break
                    
                else:
                    print("\nMasukkan input yang valid!")
                    utils.pauseClear()
                
        elif peran == "2":
            while True:
                os.system("cls")
                utils.printHeader("daftar/masuk sebagai penghuni")
                utils.printMenu("daftar", "masuk", "kembali")
                
                opsiMenu = input("> ").lower()
                os.system("cls")
                
                if opsiMenu == "1":
                    sudahTerdaftar = utilsPenghuni.daftar()
                    if sudahTerdaftar:
                        continue
                
                elif opsiMenu == "2":
                    sudahMasuk = utilsPenghuni.masuk()
                    if sudahMasuk:
                        utilsPenghuni.beranda()
                    else:
                        utilsPenghuni.daftar()

                elif opsiMenu == "3":
                    break
                    
                else:
                    print("\nMasukkan input yang valid!")
                    utils.pauseClear()
        
        elif peran == "3":
            os.system("cls")
            exit()
            
        else:
            os.system("cls")
            print("\nMasukkan input yang valid!")
            utils.pauseClear()

main()
