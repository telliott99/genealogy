import sys

try:
    input = sys.argv[1]
except:
    'please input a full name'
    sys.exit()

depth = 2
try:
    depth = int(sys.argv[2])
except:
    pass
    
#----------------------------------------

fn = 'db.txt'
fh = open(fn)
data = fh.read().strip().split('\n\n')
fh.close()

D = dict()
for e in data:
    L = e.strip().split('\n')
    gen,name,full,father,mother,path = L
    D[full] = {'gen':gen,
               'full':full,
               'name':name, 
               'father':father,
               'mother':mother, 
               'path':path}

# problem:  duplicate names, must search for more 

def dict_for_name(n, g=None):
    # do not require the full name
    for k in D:
        if k.startswith(n):
            if g and not D[k]['gen'] == g:
                continue
            return D[k]

p = dict_for_name(input)

#----------------------------------------

def get_parents(d):
    # restrict name search to the previous generation
    g = str(int(d['gen']) + 1)
    try:
        f = dict_for_name(d['father'], g)
    except:
        f = None
    try:
        m = dict_for_name(d['mother'])
    except:
        m = None
    return f,m
 
def pp(d,level):
    sp = ' '*4
    pL = [sp * level]
    try:
        pL.append(d['name'])
    except:
        pL.append('*')
    print ''.join(pL)
 
#----------------------------------------

d = dict_for_name(input)
print d['name']

for p in get_parents(d):
    pp(p,1)
    for gp in get_parents(p):
        pp(gp,2)
        for ggp in get_parents(gp):
            pp(ggp,3)
            for gggp in get_parents(ggp):
                 pp(gggp,4)







