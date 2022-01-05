import pickle as pkl

with open("./2021_10_6.pkl", 'rb') as f:
    data = pkl.load(f)



cum_1990 = {}
cum_2010 = {}
for i in data:
    c = i['New_chord']
    d = i['Date'][:4]
    
    if d == '':
        continue
    if int(d) < 2005:
        for j in c:
            cum_1990[j] = cum_1990.get(j,0) + 1
    elif int(d) > 2005:
        for j in c:
            cum_2010[j] = cum_2010.get(j,0) + 1



from matplotlib import pyplot as plt
import numpy as np

cum_1990 = sorted(cum_1990.items(), key = lambda x : x[1], reverse = True)
cum_2010 = sorted(cum_2010.items(), key = lambda x : x[1], reverse = True)

x1 = [i[0] for i in cum_1990]
y1 = [i[1] for i in cum_1990]
L1 = sum(y1)
for i in range(len(y1)):
    y1[i] = y1[i] / L1
x2 = [i[0] for i in cum_2010]
y2 = [i[1] for i in cum_2010]
L2 = sum(y2)
for i in range(len(y2)):
    y2[i] = y2[i] / L2

fig,ax = plt.subplots(nrows=1, ncols=2)
plt.figure(figsize = (10,4))
ax[0].plot(x1,y1, 'og')
ax[1].plot(x2,y2, 'rs')
plt.legend(('1990s', '2010s'))
#plt.yscale('log')
plt.show()
##plt.figure(figsize = (10,4))
##plt.plot(x1,y1, 'og')
##plt.plot(x2,y2, 'rs')
##plt.legend(('1990s', '2010s'))
##plt.yscale('log')
##plt.show()
