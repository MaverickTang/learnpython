# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi = height/(weight**2)
if bmi>32:
    print("严重肥胖")
elif bmi>28:
    print("肥胖")
elif bmi>25:
    print("过重")
elif bmi>18.5:
    print("正常")
else:
    print("过轻")