import os, sys
from collections import Counter

u = '/Users/telliott_admin'
p = u + '/Dropbox/Github/genealogy/markdown'

L = list()
dirs = [p + '/g' + str(n) for n in range(15)]
for d in dirs:
    sL = [d + '/' + f for f in os.listdir(d) if not f[0] == '.']
    sL.sort()
    L.extend(sL)

L2 = list()
for path in L:
    fh = open(path)
    data = fh.read()
    fh.close()
    sL = data.strip().split('\n')
    sL = [e for e in sL if e]
    L2.append(sL[2])
    
mo = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30,
      'May':31, 'Jun':30, 'Jul':31, 'Aug':31,
      'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
      
mL = mo.keys()

dL = list()
for e in L2:
    sL = e.split()
    for i,w in enumerate(sL):
        if w in mL and len(sL[i+1]) <= 2:
            dL.append(sL[i:i+2])

mL = [e[0] for e in dL]
C = Counter(mL)
print C.most_common(12)

'''
> python script.py 
[('May', 11), ('Jul', 11), ('Aug', 10), ('Apr', 10), ('Sep', 9), ('Dec', 9), ('Oct', 9), ('Jan', 7), ('Nov', 7), ('Mar', 6), ('Jun', 5), ('Feb', 4)]
> 
'''           
            
  
    