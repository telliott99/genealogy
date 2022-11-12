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

# problems with duplicated partial duplication of names
# must search for more 

# use birth year (could use generation easily too)

# the year is optional, for initial search
# the generation requirement is for tree building

def key_for_value_initial(property, value, year=None):
    # allow relaxed
    value = value.lower()
    if value == "Thompson Ernest":
        print value
        1/0
    for k in D:
        sD = D[k]
        if year and not sD['born'] == year:
            continue
        if value in sD[property].lower():
            return k
    return None

def key_for_value_strict(property, value, g=None):
    for k in D:
        sD = D[k]
        if g and not sD['gen'] == g:
            continue
        if value == sD[property]:
            return k
    return None

#----------------------------------------

def get_parent(k_in, kind='father'):
    # key not in D, includes key is None
    if not k_in or not k_in in D:
        return None
                
    # restrict search to the previous generation
    curr_gen = D[k_in]['gen']
    next_gen = str(int(curr_gen) + 1)

    # possibilities:
    # find a key
    # find only a name (no page)
    # find nothing
       
    n = D[k_in][kind]
    try:
        k = key_for_value_strict('name', n, g=next_gen)
        if k == None:
            k = n
    except:
        k = n
    return k
    
def get_parents(k):
    f = get_parent(k)
    m = get_parent(k, kind="mother")
    return (f,m)

#----------------------------------------
 
# spacing is still not quite right

def pp(k, level, gen):
    if not k:
        k = '*'
    sp = '. ' * 2
    s = sp * level + k
    
    # could try harder to find the generation
    # given just a name
    if not k == '*':
        pre = ('g' + str(gen)).rjust(3)
    else:
        pre = '   '    
    print pre, s
                
#----------------------------------------

k = key_for_value_initial(
    'name', input, year=y)
print "search for: ", input
if not k in D:
    print "Not found"
    sys.exit()
    
g = int(D[k]['gen'])
 
pp(k,0,g)

# Need to replace this with a proper tree
# and depth first search, level limit

f,m = get_parents(k)
for p in f,m:
    if not p:
        continue
    pp(p,1,g+1)
    gf, gm = get_parents(p)

    for gp in gf,gm:
       pp(gp,2,g+2)
       if not gp:
           continue
       ggf, ggm = get_parents(gp)
    
       for ggp in ggf,ggm:
           if not ggp:
               continue
           pp(ggp,3,g+3)
           gggf, gggm = get_parents(ggp) 
           
           for gggp in gggf,gggm:
               if not gggp:
                   continue
               pp(gggp,4,g+4)
               ggggf, ggggm = get_parents(gggp)
               pp(ggggf,5,g+5)
               pp(ggggm,5,g+5)

    
  
    
    

