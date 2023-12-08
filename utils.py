import os

def header():
    border = "==========================="

    print(f'''
{border}

SELAMAT DATANG DI EKOS

{border}
    ''')
    
def pauseClear():
    os.system("pause")
    os.system("cls")
    
def peran():
    print('''
[*] Pemilik        
[*] Penghuni
[x] Keluar
''')

def menu():
    print('''
[*] Daftar
[*] Masuk
[x] Keluar      
''')
