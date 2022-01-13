#仮の成績
grade_2 = {"健康運動":2, "人文":4, "社会":6, "総合":2, "キャリア関係":0, "琉大特色・地域創生":0, "総合領域":0, 
"日本語・日本語事情":0, "小計１":14, "自然":0, "小計２":14, "情報関係":2, "英語":8, "ドイツ語":0, "フランス語":0, 
"スペイン語":0, "中国語":4, "その他":0, "外国語計":12, "共通":30, "専門基礎":8, "専門基礎指定外":0, 
"情報技術":2, "総合力演習":5, "研究実験":6, "数学基礎":6, "知能情報コア":20, "工学融合（選択）":0, "数学基礎（選択）":0, 
"知能情報アドバンスト":0, "知能情報関連":0, "数情計":0, "選択（工学共通）":0, "自由":2, "教職":0, "数情等計":2, "専門計":30, "合計":60}

HEALTH_EXERCISE = 2 #健康運動2
HUMANITIES = 2 #人文2
SOCIRTY = 2 #社会2
COMPREHENSIVE = 2 #総合領域2
SUBTOTAL_1 = 12 #小計１12
SUBTOTAL_2 = 14 #小計２14
INFO = 2 #情報関係2
ENGLISH = 8 #英語8
FOREIGN_LANGUAGE = 12 #外国語計12
COMMON = 30 #共通計30

BASIC = 8 #専門基礎8

INFORMATION_TECHNOLOGY = 2 #情報技術2
EXERCISE = 7 #総合力演習7
EXPERIMENT = 15 #研究実験15
MATH = 6 #数学基礎6
CORE = 26#知能情報コア26
FUSION = 4 #工学融合（選択）4
SUBTOTAL_3 = 22#数情計22
SUBTOTAL_4 = 36 #数情等計36
SPECIALIZE = 92 #専門計92

TOTAL = 130 #合計130

#現在の単位数を出力する
def now_grade(garde):
    print("「現在の取得単位数」")

    '''現在の単位数の出力'''
    print("・共通教育")
    print("健康運動 : " + str(grade_2["健康運動"]))

    print("人文：" + str(grade_2["人文"]))

    print("社会：" + str(grade_2["社会"]))

    print("総合：" + str(grade_2["総合"]))

    print("キャリア関係：" + str(grade_2["キャリア関係"]))

    print("琉大特色・地域創生：" + str(grade_2["琉大特色・地域創生"]))

    print("総合領域：" + str(grade_2["総合領域"]))

    print("小計１：" + str(grade_2["小計１"]))

    print("自然：" + str(grade_2["自然"]))

    print("小計２：" + str(grade_2["小計２"]))
    
    print("情報関係：" + str(grade_2["情報関係"]))

    print("英語：" + str(grade_2["英語"]))

    print("ドイツ語：" + str(grade_2["ドイツ語"]))

    print("中国語：" + str(grade_2["中国語"]))

    print("スペイン語：" + str(grade_2["スペイン語"]))

    print("その他：" + str(grade_2["その他"]))

    print("外国語：" + str(grade_2["外国語計"]))

    print("・専門教育")

    print("専門基礎：" + str(grade_2["専門基礎"]))

    print("専門基礎指定外：" + str(grade_2["専門基礎指定外"]))

    print("情報技術：" + str(grade_2["情報技術"]))

    print("総合力演習：" + str(grade_2["総合力演習"]))
    
    print("研究実験：" + str(grade_2["研究実験"]))

    print("数学基礎：" + str(grade_2["数学基礎"]))
    
    print("知能情報コア：" + str(grade_2["知能情報コア"]))
    
    print("工学融合（選択）：" + str(grade_2["工学融合（選択）"]))

    print("数学基礎（選択）：" + str(grade_2["数学基礎（選択）"]))

    print("知能情報アドバンスト：" + str(grade_2["知能情報アドバンスト"]))

    print("知能情報関連：" + str(grade_2["知能情報関連"]))

    print("数情計：" + str(grade_2["数情計"]))

    print("選択（工学共通）：" + str(grade_2["選択（工学共通）"]))

    print("自由：" + str(grade_2["自由"]))

    print("教職：" + str(grade_2["教職"]))
    
    print("数情等計：" + str(grade_2["数情等計"]))

    print("共通必要単位数：" + str(grade_2["共通"]))

    print("専門必要単位数：" + str(grade_2["専門計"]))

    print("合計必要単位数：" + str(grade_2["合計"]))

    print()



#必要単位数が計算上0以下になった場合に0に調整する
def grade_adjust(subject):
    if subject < 0:
        subject = 0

    return subject



#必要単位数を出力する
def calc(grade_2):
    print("「必要単位数」")
    '''必要必須単位の出力'''
    health_exercise = HEALTH_EXERCISE - grade_2["健康運動"]
    health_exercise = grade_adjust(health_exercise)
    print("健康運動 : " + str(health_exercise))

    humanities = HUMANITIES - grade_2["人文"]
    humanities = grade_adjust(humanities)
    print("人文：" + str(humanities))

    society = SOCIRTY - grade_2["社会"]
    society = grade_adjust(society)
    print("社会：" + str(society))

    print("総合：0")
    print("キャリア関係：0")
    print("琉大特色・地域創生：0")

    comprehensive = COMPREHENSIVE - grade_2["総合領域"]
    comprehensive = grade_adjust(comprehensive)
    print("総合領域：" + str(comprehensive))

    print("日本語・日本語事情：0")

    subtotal_1 = SUBTOTAL_1 - grade_2["小計１"]
    subtotal_1 = grade_adjust(subtotal_1)
    print("小計１：" + str(subtotal_1))

    print("自然：0")

    subtotal_2 = SUBTOTAL_2 - grade_2["小計２"]
    subtotal_2 = grade_adjust(subtotal_2)
    print("小計２：" + str(subtotal_2))

    info = INFO - grade_2["情報関係"]
    info = grade_adjust(info)
    print("情報関係：" + str(info))

    english = ENGLISH - grade_2["英語"]
    english = grade_adjust(english)
    print("英語：" + str(english))

    print("ドイツ語：0")
    print("フランス語：0")
    print("スペイン語：0")
    print("中国語：0")
    print("その他：0")

    foreign_language = FOREIGN_LANGUAGE - grade_2["外国語計"]
    foreign_language = grade_adjust(foreign_language)
    print("外国語：" + str(foreign_language))

    basic = BASIC - grade_2["専門基礎"]
    basic = grade_adjust(basic)
    print("専門基礎：" + str(basic))

    print("専門基礎指定外：0")

    information_technology = INFORMATION_TECHNOLOGY - grade_2["情報技術"]
    information_technology = grade_adjust(information_technology)
    print("情報技術：" + str(information_technology))

    exercise = EXERCISE - grade_2["総合力演習"]
    exercise = grade_adjust(exercise)
    print("総合力演習：" + str(exercise))

    experiment = EXPERIMENT - grade_2["研究実験"]
    experiment = grade_adjust(experiment)
    print("研究実験：" + str(experiment))

    math = MATH - grade_2["数学基礎"]
    math = grade_adjust(math)
    print("数学基礎：" + str(math))

    core = CORE - grade_2["知能情報コア"]
    core = grade_adjust(core)
    print("知能情報コア：" + str(core))
    
    fusion = FUSION - grade_2["工学融合（選択）"]
    fusion = grade_adjust(fusion)
    print("工学融合（選択）：" + str(fusion))

    print("数学基礎（選択）：0")
    print("知能情報アドバンスト：0")
    print("知能情報関連：0")

    subtotal_3 = SUBTOTAL_3 - grade_2["数情計"]
    subtotal_3 = grade_adjust(subtotal_3)
    print("数情計：" + str(subtotal_3))

    print("選択（工学共通）：0")
    print("自由：0")
    print("教職：0")

    subtotal_4 = SUBTOTAL_4 - grade_2["数情等計"]
    subtotal_4 = grade_adjust(subtotal_4)
    print("数情等計：" + str(subtotal_4))

    common_sum = grade_2["共通"]
    required_common = COMMON - common_sum
    required_common = grade_adjust(required_common)
    print("共通必要単位数：" + str(required_common))

    specialize_sum = grade_2["専門計"]
    required_specialize = SPECIALIZE - specialize_sum
    required_specialize = grade_adjust(required_specialize)
    print("専門必要単位数：" + str(required_specialize))

    sum = grade_2["合計"]
    required_total = TOTAL - sum
    required_total = grade_adjust(required_total)
    print("合計必要単位数：" + str(required_total))
    print()

now_grade(grade_2)
calc(grade_2)

