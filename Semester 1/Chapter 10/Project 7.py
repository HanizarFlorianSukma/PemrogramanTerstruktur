file = open("d:jawabanNo6.txt", "r")
teksSandi = (file.read())
n = 2
print(f'Teks Sandi : {teksSandi}\nNilai N    : {n}')
teksAsli = ''
for i in teksSandi:
    value = ord(i)
    newValue = value-n
    if newValue == 30:
        newValue = 32
    elif newValue < 65:
        newValue = 90 - (64-newValue)
    teksAsli += (chr(newValue))
file = open("d:jawabanNo7.txt", "a+")
file.write(f'{teksAsli}')
print(f'Teks Asli  : {teksAsli}')
file.close()
