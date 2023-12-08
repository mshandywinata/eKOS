dataPenghuni = open(f"data/penghuni/shandy.txt", "r")
barisData = dataPenghuni.readlines()
username = barisData[0]
password = barisData[1]

print(username.rstrip("\n"))
print(password.rstrip("\n"))
