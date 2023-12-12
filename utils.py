import os, time

def printBorder():
    return "==========================="

def absolutePath():
    return os.path.dirname(os.path.abspath(__file__))

def pauseClear():
    os.system("pause")
    os.system("cls")

def hariTanggal():
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    waktu = time.localtime(time.time())
    hari = hari[waktu.tm_wday]
    tanggal = waktu.tm_mday
    bulan = bulan[waktu.tm_mon-1]
    tahun = waktu.tm_year
    
    return f"{hari}, {tanggal} {bulan} {tahun}"

def waktu():
    waktu = time.localtime(time.time())
    jam = waktu.tm_hour
    
    if 0 <= jam <= 10:
        return "pagi"
    elif 11 <= jam <= 13:
        return "siang"
    elif 14 <= jam <= 17:
        return "sore"
    else:
        return "malam"

def printHeader(teks):
    print(f'''
{printBorder()} 

{teks.upper()}

{printBorder()}
''')

def printMenu(*menu):
    for i in range(len(menu)):
        print(f"[{i+1}] {menu[i].title()}")
        time.sleep(0.25)
    print()
