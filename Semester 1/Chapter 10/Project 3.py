file = open("d:/file2.txt", "r").readlines()
dataList = []
for i in range(len(file)):
    data = file[i].rstrip("\n")
    pecahData = data.split("|")
    dataDict = {'nim':pecahData[0], 'nama':pecahData[1], 'alamat':pecahData[2]}
    dataList.append(dataDict)
print(dataList)
