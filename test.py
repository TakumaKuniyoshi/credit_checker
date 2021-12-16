import getPdfData

path = "./成績表.pdf"
data = getPdfData.getCreditData(path)

print(data[0])
print()
print(data[1])
#テスト