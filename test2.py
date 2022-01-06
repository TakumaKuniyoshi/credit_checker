mandatory = {"健康運動":2, "人文":2, "社会":2, "総合":0, "キャリア関係":0, "琉大特色・地域創生":0, "日本語・日本語事情":0, "自然":0}
mandatory_total = {"(総合領域計)":2, "小計1":12, "小計2":14}
getdatory = {"健康運動":0, "人文":4, "社会":2, "総合":0, "キャリア関係":0, "琉大特色・地域創生":0, "日本語・日本語事情":0, "自然":0}
gettory_total = {"(総合領域計)":0, "小計1":6, "小計2":6}

print("取得している単位")
for i in getdatory:
    if (getdatory[i] != 0):
        print("{} {}単位".format(i,getdatory[i]))

print("")
print("卒業要件に満たしている単位")
for i in mandatory:
    if (getdatory[i] >= mandatory[i]):
        print("{} {}単位".format(i,getdatory[i]))

print("")
print("卒業要件に不足している単位")
for i in mandatory:
    if (getdatory[i] < mandatory[i]):
        print("{} {}単位".format(i,mandatory[i]))