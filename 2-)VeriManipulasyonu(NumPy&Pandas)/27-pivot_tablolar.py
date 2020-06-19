#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:16:08 2020

@author: baysan
"""


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')


print(titanic.pivot_table('survived',index='sex',columns='class'))

"""
odaklandığımız değişken
hangi index (gözlem birimleri)
hangi sütunlar
"""