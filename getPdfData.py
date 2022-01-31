import tabula

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


    keyDict = dict(zip(name,name))
    keyDict['小計1'] = '人文+社会+総合領域'
    keyDict['小計2'] = '人+社+総+自然'
    keyDict['その他'] = 'その他言語'
    return creditCalculation([RequiredCreditsDict,CreditEarnedDict,keyDict])
    
def creditCalculation(data):
    RequiredCreditsDict = data[0]
    CreditEarnedDict = data[1]
    keyDict = data[2]
    necessary = {}
    finish = {}
    i = 0
    keylanguage = []
    for key in list(RequiredCreditsDict):
        if (keyDict[key][-1] ==  '語' and not(key =='英語')):
            keylanguage += [key]
            if CreditEarnedDict[key] > 0:
                RequiredCreditsDict[key] = 4
                finish[key] = CreditEarnedDict[key]
        if(RequiredCreditsDict[key] != 0 or CreditEarnedDict[key] != 0):
            if RequiredCreditsDict[key] > CreditEarnedDict[key]:
                n = RequiredCreditsDict[key]-CreditEarnedDict[key]
                if n%1 == 0:
                    n = int(n)
                necessary[keyDict[key]] = n
            else:
                n = CreditEarnedDict[key]
                if n%1 == 0:
                    n = int(n)
                finish[keyDict[key]] = n
        
    if CreditEarnedDict['英語'] >= 8:
        if CreditEarnedDict['英語'] >= 12:
            for key in keylanguage:
                necessary[key] = 0
                del necessary[key]
            return [necessary,finish]
        for key in keylanguage:
            if CreditEarnedDict[key] >= 4:
                for key in keylanguage:
                    if CreditEarnedDict[key] > 0:
                        finish[key] = CreditEarnedDict[key]
                    necessary[key]=0
                    del necessary[key]
                return [necessary,finish]

    return [finish,necessary]