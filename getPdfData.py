import tabula
import pandas

#成績表右下の単位情報を取得
def getCreditData(filePath:str):
    area = [202,543,468,800]
    data = tabula.read_pdf(filePath,pages=1,area=area)
    data = data[0]
    dataright = data[['単位修得状況','必須単位','修得単位']]
    dataright = dataright.dropna(how='all')
    dataright = dataright.fillna(0)
    dataleft = data[['単位修得状況.1','必須単位.1','修得単位.1']]
    dataleft = dataleft.dropna(how='all')
    dataleft = dataleft.fillna(0)
    dataright = dataright.to_dict(orient='list')
    name = dataright['単位修得状況']
    RequiredCredits = dataright['必須単位']
    CreditEarned = dataright['修得単位']

    dataleft = dataleft.to_dict(orient='list')
    name += dataleft['単位修得状況.1']
    RequiredCredits += dataleft['必須単位.1']
    CreditEarned += dataleft['修得単位.1']
    RequiredCreditsDict = dict(zip(name,RequiredCredits))
    CreditEarnedDict = dict(zip(name,CreditEarned))
    for key in list(RequiredCreditsDict):
        if RequiredCreditsDict[key] == 0 and CreditEarnedDict[key] == 0:
            del RequiredCreditsDict[key],CreditEarnedDict[key]

    return [RequiredCreditsDict,CreditEarnedDict]
