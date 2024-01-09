# UTILITAS YANG DIGUNAKAN UNTUK SELURUH FILE PROGRAM
import os, time

# memberi lokasi absolut dari file program sehingga bisa dijalankan di luar working directory
lokasiAbsolut = os.path.dirname(os.path.abspath(__file__))
border =  "======================================="

# meminta input berupa tombol bebas dan membersihkan terminal
def pauseClear():
    os.system("pause")
    os.system("cls")

# menampilkan header 
def printHeader(teks):
    print(f'''
{border} 

{teks.upper()}

{border}
''')

# menampilkan menu secara terurut sebanyak argumen yang diberi
def printMenu(*menu):
    for i in range(len(menu)):
        print(f"[{i+1}] {menu[i].title()}")
        time.sleep(0.125)
    print()
    
# peringatan input kosong
def inputKosong():
    print("\nKolom input tidak boleh ada yang kosong!")
    pauseClear()

# peingatan input tidak valid
def inputTidakValid():
    print("\nMasukkan inputan yang valid!")
    pauseClear()

# memetakan hari dan tanggal dalam bahasa Indonesia
def hariTanggal():
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    
    waktu = time.localtime(time.time())
    hari = hari[waktu.tm_wday]
    tanggal = waktu.tm_mday
    bulan = bulan[waktu.tm_mon - 1]
    tahun = waktu.tm_year
    
    return f"{hari}, {tanggal} {bulan} {tahun}"

# menentukan waktu berdasarkan jam di komputer dalam bahasa Indonesia
def waktu():
    waktu = time.localtime(time.time())
    jam = waktu.tm_hour
    
    if 4 <= jam <= 10:
        return "pagi"
    elif 11 <= jam <= 13:
        return "siang"
    elif 14 <= jam <= 17:
        return "sore"
    else:
        return "malam"

# mencari file txt yang ada dalam suatu lokasi tertentu
def cariFile(lokasiFile, namaFileTarget):
    for file in os.listdir(lokasiFile):
        if file.endswith(".txt") and file.rstrip(".txt") == namaFileTarget:
                return True
    return False