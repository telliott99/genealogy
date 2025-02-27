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
        k += ' ' + born
    D[k] = {'gen':gen, 'name':name, 
            'born':born, 'died':died, 
            'father':father, 'mother':mother,
            'spouseL':spouseL, 'path':path}

#------------------------------------------------

# problem:  duplicate names, must search for more 
# decided to use birth year

# the year requirement is for initial search
# the generation requirement helps for tree building

def key_for_value(property, value, g=None, year=None):
    # do not need to have the full name
    for k in D:
        sD = D[k]
        if sD[property].startswith(value):
            if g and not sD['gen'] == g:
                continue
            if year and not sD['born'] == year:
                continue
            return k
    return None

#----------------------------------------

# this strategy does not return people withouut pages

def get_parents(k):
    # pass in the key for the starting individual
    # it may happen that k is None
    if not k:
        return None
        
    f = D[k]['father']
    # restrict name search to the previous generation
    g = str(int(D[k]['gen']) + 1)
    try:
        kf = key_for_value('name',f, g)
    except:
        kf = D[k]['father']

    m = D[k]['mother']
    try:
        km = key_for_value('name',m, g)
    except:
        km = D[k]['mother']
        
    # we return the key, but only print it
    # so modify to search for name if no key (no page)
    return kf, km
 
def pp(k,level):
    sp = ' '*3
    pL = [sp * level]
    if k:
        pL.append(k)
    else:
        pL.append('*')
    print ''.join(pL)
 
#----------------------------------------

k = key_for_value('name', input, year=y)
print k

L1 = get_parents(k)
for p in L1:
    pp(p,1)

    L2 = get_parents(p)
    if not L2:
        continue
    for gp in L2:
        pp(gp,2)

        L3 = get_parents(gp)
        if not L3:
            continue
        for ggp in L3:
            pp(ggp,3)
              
            L4 = get_parents(ggp)
            if not L4:
                continue
            for gggp in L4:
                pp(gggp,4)
 
                L5 = get_parents(gggp)
                if not L5:
                    continue
                for ggggp in L5:
                    pp(ggggp,5)




