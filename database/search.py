import sys

try:
    input = sys.argv[1]
except:
    'Please input a name to search'
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
# use birth year (could use generation easily too)

# the year requirement is for initial search
# the generation requirement is for tree building

# strict doesn't work

def key_for_value(property, value, g=None, year=None, strict=False):
    # do not need to have the full name
    value = value.lower()
    for k in D:
        sD = D[k]
        if g and not sD['gen'] == g:
            continue
        if year and not sD['born'] == year:
            continue
        if not strict:
            if value in sD[property].lower():
                return k
        else:
            if value == sD[property]:
                return k
    return None

#----------------------------------------


def get_parent(k_in, kind='father'):
    # key not in D, includes key == None
    if not k_in or not k_in in D:
        return None
                
    t = None
    #t = "Martha Comstock"
    
    # restrict name search to the previous generation
    curr_gen = D[k_in]['gen']
    next_gen = str(int(curr_gen) + 1)

    # find a key or
    # find only a name (no page)
    # find nothing
       
    n = D[k_in][kind]
    try:
        k = key_for_value('name', n, g=next_gen)
        if k == None:
            k = n
    except:
        k = n
    
    # debug
    if t and t in k_in:
        print "get parents"
        print curr_gen
        print 'k_in', k_in
        print 'k', k 
        print 'n', n
    if k == '*':
        return None
    return k
 
def pp(k,level):
    sp = ' ' * 3
    if k:
        try:
            print sp * level + k + ' - g' + D[k]['gen']
        except KeyError:
            print sp * level + k
    else:
        # pass
        print sp * level + '*'

def get_parents(k):
    f = get_parent(k)
    m = get_parent(k, kind="mother")
    return (f,m)

#----------------------------------------

k = key_for_value('name', input, year=y, strict=False)
if not k in D:
    print "Not found"
    sys.exit()
pp(k,0)

f,m = get_parents(k)
for p in f,m:
    if not p:
        continue
    pp(p,1)
    gf, gm = get_parents(p)

    for gp in gf,gm:
       pp(gp,2)
       if not gp:
           continue
       ggf, ggm = get_parents(gp)
    
       for ggp in ggf,ggm:
           if not ggp:
               continue
           pp(ggp,3)
           gggf, gggm = get_parents(ggp) 
           
           for gggp in gggf,gggm:
               if not gggp:
                   continue
               pp(gggp,4)
               ggggf, ggggm = get_parents(gggp)
               pp(ggggf,5)
               pp(ggggm,5)

    
  
    
    

