import pickle as pkl

with open("./2021_10_6.pkl", 'rb') as f:
    data = pkl.load(f)

## print(data[0])




cum = {}
for i in data:
    c = i['New_chord']
    s = i['Space_num']
    ## L = len(c)
    
    for j, k in zip(c, s):
        for _ in range(int(k)):
            cum[j] = cum.get(j,0) + 1


from matplotlib import pyplot as plt
import numpy as np

cum = sorted(cum.items(), key = lambda x : x[1], reverse = True)

x = [i[0] for i in cum]
y = [i[1] for i in cum]


plt.figure(figsize = (10,4))
plt.plot(x,y)
plt.yscale('log')
plt.show()
