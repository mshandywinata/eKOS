import os, utils

def daftar():
    os.system("cls")
    username = input("Username: ")
    password = input("Password: ")
    namaKos = input("Nama Kos: ")
    
    try:
        dataPenghuni = open(f"data/penghuni/{username}.txt", "r")
        print(f"Akun dengan username {username} sudah terdaftar")
        utils.pauseClear()
    
    except FileNotFoundError:
        dataPenghuni = open(f"data/penghuni/{username}.txt", "w")
        dataPenghuni.write(f"{username}\n{password}\n{namaKos}")
    
    print("Berhasil terdaftar!")
    utils.pauseClear()
    
def masuk():
    os.system("cls")
    while True:
        username = input("Username: ")
        password = input("Password: ")
    
        try:
            dataPenghuni = open(f"data/penghuni/{username}.txt", "r")
            barisData = dataPenghuni.readlines()
            dataUsername = barisData[0].rstrip("\n")
            dataPassword = barisData[1].rstrip("\n")
            
            if username == dataUsername and password == dataPassword:
                print("good!")
                break
            else:
                print()
                
        except FileNotFoundError:
            print("Kamu belum terdaftar!\n")
            utils.pauseClear()
            break

def beranda():
    pass
        