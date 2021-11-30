teks = input('Teks Asli  : ')
n = int(input('Nilai N    : '))
teksSandi = ''
for i in teks.upper():
    value = ord(i)
    newValue = value+n 
    if newValue <= 65:
        newValue = 32
    elif newValue >= 90:
        newValue = 65
    teksSandi += (chr(newValue))
file = open("d:jawabanNo6.txt", "a+")
file.write(f'{teksSandi}')
print(f'Teks Sandi : {teksSandi}')
file.close()
