import utils, utilsPemilik, utilsPenghuni
import os

while True:
    os.system("cls")
    utils.header()
    utils.peran()
    peran = input("> ").lower()
        
    if peran == "penghuni":
        os.system("cls")
        utils.menu()
        
        opsiMenu = input("> ").lower()
        os.system("cls")

        if opsiMenu == "daftar":
            utilsPenghuni.daftar()
        
        elif opsiMenu == "masuk":
            utilsPenghuni.masuk()
            
        elif opsiMenu == "keluar":
            exit()
        
    elif peran == "pemilik":
        utilsPemilik.daftar()
        break
    
    elif peran == "keluar":
        os.system("cls")
        exit()
        
    else:
        print("\nMasukkan input yang valid!")
        utils.pauseClear()
