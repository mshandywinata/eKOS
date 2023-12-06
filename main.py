import utils, utilsPemilik, utilsPenghuni

border = "========================"

print(f'''
{border}

SELAMAT DATANG DI EKOS

{border}
''')

utils.peran()
peran = input("> ").lower()

if peran == "penghuni":
    utilsPenghuni.registerPenghuni()
