file = open("d:/file1.txt", "r")
genap = 0
ganjil = 0
for i in file:
    newContent = int(i)
    if newContent%2 == 0:
        genap += 1
    else:
        ganjil += 1

print(f'Banyaknya bilangan genap  : {genap}')
print(f'Banyaknya bilangan ganjil : {ganjil}')
file.close()
