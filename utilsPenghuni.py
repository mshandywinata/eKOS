import os 

def daftar():
    os.system("cls")
    username = input("Username: ")
    password = input("Password: ")
    namaKos = input("Nama Kos: ")
    
    dataPenghuni = open(f"data/penghuni/{username}.txt", "w")
    dataPenghuni.write(f"{username}\n{password}\n{namaKos}")
    
def login():
    os.system("cls")
    username = input("Username: ")
    password = input("Password: ")
    
    try:
        dataPenghuni = open(f"data/penghuni/{username}.txt", "w")
    except FileNotFoundError:
        print("Kamu belum terdaftar!")
        