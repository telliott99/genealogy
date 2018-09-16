import sys

try:
    input = sys.argv[1]
except:
    'please input a full name'
    sys.exit()

y = None
try:
    y = sys.argv[2]
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
    name,born,died,father,mother = L[:5]
    rest = L[6:]
    born = born[2:]
    died = died[2:]
    father = father[2:]
    mother = mother[2:]
    
    path = rest.pop()
    spouseL = [spouse[2:] for spouse in rest]
    gen = path.split('/')[0][1:]
    k = name
    if not born == '*':
        k += ' ' + born    # keys must be unique
        
    D[k] = {'gen':gen, 
            'name':name, 
            'born':born, 'died':died, 
            'father':father, 'mother':mother,
            'spouseL':spouseL, 
            'path':path}

#------------------------------------------------

# problem:  with duplicate names, unknown keys
# must search for more 
# use birth year

# the year requirement is for initial search
# the generation requirement is for tree building

def key_for_value(property, value, g=None, year=None):
    # do not need to have the full name
    for k in D:
        sD = D[k]
        if g and not sD['gen'] == g:
            continue
        if year and not sD['born'] == year:
            continue
        if value in sD[property]:
            return k
    return None

#----------------------------------------


def get_parent(k, kind='father'):
    if not k in D:
        return None
    
    # 3 situations
    # find a key
    # find only a name (no page)
    # find nothing
        
    # restrict name search to the previous generation
    g = str(int(D[k]['gen']) + 1)
    
    n = D[k][kind]
    try:
        k = key_for_value('name', n, g=g)
    except:
        k = n
    return k
 
def pp(k,level):
    sp = ' ' * 3
    if k:
        print sp * level + k
    else:
        print sp * level + '*'

def get_parents(k):
    f = get_parent(k)
    m = get_parent(k, kind="mother")
    return (f,m)

#----------------------------------------

k = key_for_value('name', input, year=y)
if not k in D:
    print "Not found"
    sys.exit()

print k

f,m = get_parents(k)
for p in f,m:
    pp(p,1)
    if not p:
        continue
    gf, gm = get_parents(p)

    for gp in gf,gm:
       pp(gp,2)
       if not gp:
           continue
       ggf, ggm = get_parents(gp)
    
       for ggp in ggf,ggm:
           pp(ggp,3)
           if not ggp:
               continue
           gggf, gggm = get_parents(ggp)
           pp(gggf,4)
           pp(gggm,4)
    
  
    
    

