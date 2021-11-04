try:
    filename = input('Masukan nama file : ')
    file = open(filename, "r")
    print('Isi file', filename, 'adalah : ')
    print('\n'+file.read())
except FileNotFoundError:
    print("File tidak ditemukan")
