import pickle as pkl
from decimal import Decimal

with open("./2021_10_16.pkl", 'rb') as f:
    data = pkl.load(f)

# print(data[3])

spring = []
summer = []
fall = []
winter = []

for i in data:
    try:
        c = i['New_chord']
        m = i['Date'][-2:]
        if m[0] == '0':
            m = m[1::]
        if 3<= int(m) <= 5:
            spring.append(c)
        elif 6 <= int(m) <= 8 :
            summer.append(c)
        elif 9 <= int(m) <= 11:
            fall.append(c)
        elif 1<= int(m) <=2 or int(m) == 12:
            winter.append(c)

    except:
        pass

Spring = {}
Summer = {}
Fall = {}
Winter = {}
for i in spring:
    for j in i:
        Spring[j] = Spring.get(j,0) +1
for i in summer:
    for j in i:
        Summer[j] = Summer.get(j,0) +1
for i in fall:
    for j in i:
        Fall[j] = Fall.get(j,0) +1
for i in winter:
    for j in i:
        Winter[j] = Winter.get(j,0) +1

from matplotlib import pyplot as plt

Spring = sorted(Spring.items(), key = lambda x : x[1], reverse = True)
Summer = sorted(Summer.items(), key = lambda x : x[1], reverse = True)
Fall = sorted(Fall.items(), key = lambda x : x[1], reverse = True)
Winter = sorted(Winter.items(), key = lambda x : x[1], reverse = True)
# print(Spring, Summer, Fall, Winter)
x1 = [i[0] for i in Spring]
y1 = [i[1] for i in Spring]
s = sum(y1)
for i in range(len(y1)):
    y1[i] /= s
x2 = [i[0] for i in Summer]
y2 = [i[1] for i in Summer]
s = sum(y2)
for i in range(len(y2)):
    y2[i] /= s
x3 = [i[0] for i in Fall]
y3 = [i[1] for i in Fall]
s = sum(y3)
for i in range(len(y3)):
    y3[i] /= s
x4 = [i[0] for i in Winter]
y4 = [i[1] for i in Winter]
s = sum(y4)
for i in range(len(y4)):
    y4[i] /= s

print(f'spring {x1}', '\n', f'summer {x2}', '\n', f'winter {x3}', '\n', f'winter {x4}')

plt.figure(figsize = (10,4))
plt.plot(x1,y1, 'yo')
plt.plot(x2,y2, 'go')
plt.plot(x3,y3, 'ro')
plt.plot(x4,y4, 'bo')
#plt.yscale('log')
plt.show()