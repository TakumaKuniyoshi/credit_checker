import getPdfData

path = "./成績表.pdf"
data = getPdfData.getCreditData(path)
out = getPdfData.creditCalculation(data)
print(out[0])
print(out[1])