import numpy as np
import pandas as pd
import xlrd
import os
import janitor
import random
import pprint

adm = pd.read_csv (r'ActiveMonitorData.txt')
adm.to_csv (r'ActiveMonitorData', index=None)

#Group Parameters Class
class grouparam:
    def __init__(self, irid, astar, profile):
        self.irid = irid
        self.astar = astar
        self.profile = profile
    def __str__(self):
      return str(vars(self))
    def __repr__(self):
      return str(vars(self))

print(type(adm.iloc[0,5]))

adm[' ProfileRight'] = adm[' ProfileRight'].astype(str)
pprint.pprint(type(adm.iloc[0,5]))
#adm[' ProfileRight'] = adm[' ProfileRight'].str.replace('Profile',' ')
adm.head()

p1 = grouparam(2161, 221, 2)
print(p1.irid)


my_dict = dict()
for i in range(idx):
    #print(adm.iloc[i,2])
    p1 = grouparam(adm.iloc[i,8], adm.iloc[i,11], adm.iloc[i,2])
    my_dict[adm.iloc[i,7]] = p1

pprint.pprint(my_dict)

agd = pd.read_csv (r'/content/sample_data/group.csv')


idx2= len(agd)
my_dict2 = dict()
for i in range(idx2):
    #print(adm.iloc[i,2])
    mlist = agd.iloc[i,10]
    mlistArr = mlist.split(",")

    #pprint.pprint(mlistArr)

    for x in range(len(mlistArr)):
        mkey = mlistArr[x].strip()
        #pprint.pprint(mkey)
        p1 = grouparam(agd.iloc[i,4], agd.iloc[i,2], agd.iloc[i,13])
        my_dict2[mkey] = p1

#pprint.pprint(my_dict)
#pprint.pprint(my_dict2)

clean_dict = {key.strip(): item.strip() for key, item in my_dict2.items()}
pprint.pprint(clean_dict)




