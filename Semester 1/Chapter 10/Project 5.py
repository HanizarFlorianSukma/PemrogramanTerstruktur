file = open("d:/file5.txt", "r").read()
for i in file:
    data = file.split("\n")
bil1 = [i.split('|')[0] for i in data]
bil2 = [i.split('|')[1] for i in data]
intBil1 = list(map(int, bil1))
intBil2 = list(map(int, bil2))
for (item1, item2) in zip(intBil1, intBil2):
    hasil = (item1+item2)
    fil = open("d:jawabanNo5.txt", "a+")
    fil.write(f'{hasil}\n')
    print(item1+item2)
