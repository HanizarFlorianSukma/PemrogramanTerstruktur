cari = input('Masukkan NIM yang mau dicari : ')
file = open("d:/file2.txt", "r").readlines()
dataList = []
for i in range(len(file)):
    data = file[i].rstrip("\n")
    pecahData = data.split("|")
    dataDict = {'nim':pecahData[0], 'nama':pecahData[1], 'alamat':pecahData[2]}
    dataList.append(dataDict)
for item in dataList:
    if item['nim'] == cari:
        print(f"\nData Mahasiswa\n\nNIM\t: {item['nim']}\nNama\t: {item['nama']}\nAlamat\t: {item['alamat']}")
        break
else:
    print("Data mahasiswa tidak ditemukan.")
