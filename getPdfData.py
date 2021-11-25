import tabula

#成績表右下の単位情報を取得
def getCreditData(filePath:str):
    area = [202,543,468,800]
    data = tabula.read_pdf(filePath,pages=1,area=area)
    return data