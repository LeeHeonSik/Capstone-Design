import pickle as pkl
from decimal import Decimal

with open("./2021_10_31.pkl", 'rb') as f:
    data = pkl.load(f)


# for i in range(len(data)):
#     print(data[i]['Genre']['whouploaded'])


############################################
# #### 장르별 누적 분포  ##########################
##################################################
# cum_ost = {}
# cum_pop = {}
# cum_ballad = {}
# cum_indie = {}
# cum_rock = {}
# for i in data:
#     c = i['New_chord']
#     s = i['Space_num']
#     g = i['Genre']

#     if g == 'ost':
#         for j in c:
#             cum_ost[j] = cum_ost.get(j,0) + 1
#     elif g == 'pop':
#         for j in c:
#             cum_pop[j] = cum_pop.get(j,0) + 1
#     elif g == '발라드':
#         for j in c:
#             cum_ballad[j] = cum_ballad.get(j,0) + 1
#     elif g == '인디음악':
#         for j in c:
#             cum_indie[j] = cum_indie.get(j,0) + 1
#     elif g == '록/메탈':
#         for j in c:
#             cum_rock[j] = cum_rock.get(j,0) + 1
#     else:
#         continue

# from matplotlib import pyplot as plt

# cum_ost = sorted(cum_ost.items(), key = lambda x : x[1], reverse = True)
# cum_pop = sorted(cum_pop.items(), key = lambda x : x[1], reverse = True)
# cum_ballad = sorted(cum_ballad.items(), key = lambda x : x[1], reverse = True)
# cum_indie = sorted(cum_indie.items(), key = lambda x : x[1], reverse = True)
# cum_rock = sorted(cum_rock.items(), key = lambda x : x[1], reverse = True)


# x1 = [i[0] for i in cum_ost]
# y1 = [i[1] for i in cum_ost]
# s = sum(y1)
# for i in range(len(y1)):
#     y1[i] /= s
# x2 = [i[0] for i in cum_pop]
# y2 = [i[1] for i in cum_pop]
# s = sum(y2)
# for i in range(len(y2)):
#     y2[i] /= s
# x3 = [i[0] for i in cum_ballad]
# y3 = [i[1] for i in cum_ballad]
# s = sum(y3)
# for i in range(len(y3)):
#     y3[i] /= s
# x4 = [i[0] for i in cum_indie]
# y4 = [i[1] for i in cum_indie]
# s = sum(y4)
# for i in range(len(y4)):
#     y4[i] /= s
# x5 = [i[0] for i in cum_rock]
# y5 = [i[1] for i in cum_rock]
# s = sum(y5)
# for i in range(len(y5)):
#     y5[i] /= s

# # print(f'cum_ost {x1}', '\n', f'cum_pop {x2}', '\n', f'cum_ballad {x3}', '\n', f'cum_indie {x4}', '\n', f'cum_rock {x5}')


# plt.figure(figsize = (10,4))
# # plt.plot(x1,y1, 'r', label = 'ost')
# # plt.plot(x2,y2, 'y', label = 'pop')
# plt.plot(x3,y3, 'g', label = 'ballad')
# # plt.plot(x4,y4, 'b', label = 'indie')
# # plt.plot(x5,y5, 'm', label = 'rock')
# # plt.legend(('ost', 'pop', 'ballad', 'indie', 'rock'))
# plt.legend()
# # plt.yscale('log')
# plt.show()

#####################################################
# #### 계절별 누적 분포  ##############################
#################################################

# spring = []
# summer = []
# fall = []
# winter = []

# for i in data:
#     try:
#         c = i['New_chord']
#         m = i['Date'][-2:]
#         if m[0] == '0':
#             m = m[1::]
#         if 3<= int(m) <= 5:
#             spring.append(c)
#         elif 6 <= int(m) <= 8 :
#             summer.append(c)
#         elif 9 <= int(m) <= 11:
#             fall.append(c)
#         elif 1<= int(m) <=2 or int(m) == 12:
#             winter.append(c)

#     except:
#         pass

# Spring = {}
# Summer = {}
# Fall = {}
# Winter = {}
# for i in spring:
#     for j in i:
#         Spring[j] = Spring.get(j,0) +1
# for i in summer:
#     for j in i:
#         Summer[j] = Summer.get(j,0) +1
# for i in fall:
#     for j in i:
#         Fall[j] = Fall.get(j,0) +1
# for i in winter:
#     for j in i:
#         Winter[j] = Winter.get(j,0) +1

# from matplotlib import pyplot as plt

# Spring = sorted(Spring.items(), key = lambda x : x[1], reverse = True)
# Summer = sorted(Summer.items(), key = lambda x : x[1], reverse = True)
# Fall = sorted(Fall.items(), key = lambda x : x[1], reverse = True)
# Winter = sorted(Winter.items(), key = lambda x : x[1], reverse = True)
# # print(Spring, Summer, Fall, Winter)
# x1 = [i[0] for i in Spring]
# y1 = [i[1] for i in Spring]
# s = sum(y1)
# for i in range(len(y1)):
#     y1[i] /= s
# x2 = [i[0] for i in Summer]
# y2 = [i[1] for i in Summer]
# s = sum(y2)
# for i in range(len(y2)):
#     y2[i] /= s
# x3 = [i[0] for i in Fall]
# y3 = [i[1] for i in Fall]
# s = sum(y3)
# for i in range(len(y3)):
#     y3[i] /= s
# x4 = [i[0] for i in Winter]
# y4 = [i[1] for i in Winter]
# s = sum(y4)
# for i in range(len(y4)):
#     y4[i] /= s

# print(f'spring {x1}', '\n', f'summer {x2}', '\n', f'winter {x3}', '\n', f'winter {x4}')

# plt.figure(figsize = (10,4))
# plt.plot(x1,y1, 'yo')
# plt.plot(x2,y2, 'go')
# plt.plot(x3,y3, 'ro')
# plt.plot(x4,y4, 'bo')
# #plt.yscale('log')
# plt.show()

###################################
#### 연대별 누적 분포 ########################
#############################################
cum_1900 = {}
cum_1990 = {}
cum_2000 = {}
cum_2010 = {}
_1900, _1990, _2000, _2010 = 0, 0, 0, 0

r = 0
for i in data:
    c = i['New_chord']
    d = i['Date'][:4]
    
    if d == '':
        continue
    if int(d) <= 1990:
        for j in c:
            cum_1900[j] = cum_1900.get(j,0) + 1
        _1900 +=1
        if i['Genre'] == '록/메탈':
            r += 1
    elif int(d) <= 2000:
        for j in c:
            cum_1990[j] = cum_1990.get(j,0) + 1
        _1990 += 1
    elif int(d) <=2010:
        for j in c:
            cum_2000[j] = cum_2000.get(j,0) + 1
        _2000 += 1
    elif int(d) > 2010:
        for j in c:
            cum_2010[j] = cum_2010.get(j,0) + 1
        _2010 += 1

from matplotlib import pyplot as plt
import numpy as np

cum_1900 = sorted(cum_1900.items(), key = lambda x : x[1], reverse = True)
cum_1990 = sorted(cum_1990.items(), key = lambda x : x[1], reverse = True)
cum_2000 = sorted(cum_2000.items(), key = lambda x : x[1], reverse = True)
cum_2010 = sorted(cum_2010.items(), key = lambda x : x[1], reverse = True)


x1 = [i[0] for i in cum_1900]
y1 = [i[1] for i in cum_1900]
L1 = sum(y1)
for i in range(len(y1)):
    y1[i] = y1[i] / L1
x2 = [i[0] for i in cum_1990]
y2 = [i[1] for i in cum_1990]
L2 = sum(y2)
for i in range(len(y2)):
    y2[i] = y2[i] / L2
x3 = [i[0] for i in cum_2000]
y3 = [i[1] for i in cum_2000]
L3 = sum(y3)
for i in range(len(y3)):
    y3[i] = y3[i] / L3
x4 = [i[0] for i in cum_2010]
y4 = [i[1] for i in cum_2010]
L4 = sum(y4)
for i in range(len(y4)):
    y4[i] = y4[i] / L4

print(f'~1990 {x1}', '\n', f'1991~2000 {x2}', '\n', f'2001~2010 {x3}', '\n', f'2011~ {x4}')
print(_1900, _1990, _2000, _2010, r)

fig,ax = plt.subplots(nrows=2, ncols=2)
ax[0][0].plot(x1,y1, 'r', label = '~1990')
ax[0][1].plot(x2,y2, 'y', label = '1991~2000')
ax[1][0].plot(x3,y3, 'b', label = '2001~2010')
ax[1][1].plot(x4,y4, 'g', label = '2011~')
# plt.legend(('~1990', '1991~2000', '2001~2010', '2011~'))
plt.legend()
plt.show()