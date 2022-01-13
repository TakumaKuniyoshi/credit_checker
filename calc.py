grade = {"Japanese":2, "Math_1_A":2, "Math_2_B":2, "English":4, "Science":1, "Social studies":1.5}
grade_2 = {"健康運動":2, "人文":4, "社会":6, "総合":2, "キャリア関係":2, "琉大特色・地域創生":2}
health_exercise = 2 #健康運動2
humanities = 2 #人文2
society = 2 #社会2
comprehensive = 2 #総合領域2
subtotal_1 = 12 #小計１12
subtotal_2 = 14 #小計２14
english = 8 #英語8
foreign_language = 12 #外国語計12
common = 30 #共通計30

basic = 8 #専門基礎8

information_technology = 2 #情報技術2
exercise = 7 #総合力演習7
experiment = 15 #研究実験15
math = 6 #数学基礎6
core = 26#知能情報コア26
fusion = 4 #工学融合（選択）4
subtotal_3 = 22#数情計22
subtotal_4 = 36 #数情等計36
specialize = 92 #専門計92

total = 130 #合計130



def calc(grade):
    common_sum = grade["Japanese"]+grade["English"]+grade["Social studies"]
    required_common = common - common_sum
    print("共通必要単位数：" + str(required_common))

    basic_sum =  grade["Math_1_A"]
    required_basic = basic - basic_sum
    print("専門基礎必要単位数：" + str(required_basic))

    specialize_sum = grade["Math_2_B"]+grade["Science"]
    required_specialize = specialize - specialize_sum
    print("専門必要単位数：" + str(required_specialize))

    sum = common_sum + basic_sum + specialize_sum
    required_total = total - sum
    print("合計必要単位数：" + str(required_total))

    print("現在の共通科目の取得単位数：" + str(common_sum))

    print("現在の専門基礎科目の取得単位数：" + str(basic_sum))

    print("現在の専門科目の取得単位数：" + str(specialize_sum))

    current = total - required_total
    print("現在の合計取得単位数：" + str(current))

calc(grade)

'''
print("共通教育 \n 健康運動　\n 人文　\n 社会 \n 総合 \n キャリア関係 \n 流大特色・地域創生 \n 日本語・日本語事情 \n 自然 \n 情報関係 \n 英語 \n ドイツ語 \n フランス語 \n スペイン語 \n 中国語 \n その他")
print("専門基礎教育 \n 専門基礎 \n 専門基礎指定外")
print("専門教育 \n 情報技術 \n 総合力演習 \n 研究実験 \n 数学基礎 \n 知能情報コア \n 工学融合（選択） \n 数学基礎（基礎） \n 知能情報アドバンスト \n 知能情報関連 \n 選択（工学共通） \n 自由 \n 教職")
print("合計")
'''