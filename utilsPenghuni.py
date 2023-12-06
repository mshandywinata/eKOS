import os 

def registerPenghuni():
    os.system("cls")
    username = input("Username: ")
    password = input("Password: ")
    namaKos = input("Nama Kos: ")
    
    dataPenghuni = open(f"data/penghuni/{username}{namaKos}.txt", "w")
    dataPenghuni.write(f"{username}\n{password}\n{namaKos}")
    
    