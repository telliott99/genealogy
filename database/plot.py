import sys, argparse

parser = argparse.ArgumentParser(
    description='Plot a family tree')
    
parser.add_argument('-n', '--name',
    help="name of the individual",
    type=str)
    
parser.add_argument('-y', '--year', 
    help="birth year of the individual",
    default=None,
    type=str)

parser.add_argument('-d', '--depth', 
    help="depth of search",
    default=3,
    type=int)

parser.add_argument('-l', '--links', 
    help="provide links",
    default=False,
    type=bool)

args = parser.parse_args()
input = args.name
year = args.year
depth = args.depth
 
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
    gen = int(path.split('/')[0][1:])
    k = name
    if not born == '*':
        k += ' ' + born    # keys must be unique
        
    D[k] = {'key':k,
            'gen':gen, 
            'name':name, 
            'born':born, 
            'died':died, 
            'father':father, 
            'mother':mother,
            'spouseL':spouseL, 
            'path':path}

#------------------------------------------------

'''
problems with partial duplication of names
want to allow parts of names

optional restriction: birth year
(could allow generation easily too)
'''

def key_for_input_string(name, year=None):
    n = name.lower()
    for k in D:
        sD = D[k]
        if year and not sD['born'] == year:
            continue
        if n in sD['name'].lower():
            return k
    return None

#------------------------------------------------

'''
usual situation, suppose I have the key for:

Thomas Anthony Elliott
b 1955
d *
f Norman Elliott
m Jean Francis Foster
o Meenal Bhopatkar
o Joan Carlyn Olson
g1/thomas_anthony_elliott.md

namely:
Thomas Anthony Elliott 1955
'''

# returns key if it exists, or None
def key_for_parent(k_in, kind='father'):
    try:
        parent_name = D[k_in][kind]
        parent_gen = D[k_in]['gen'] + 1
    except:
        return None
    for k in D:
        sD = D[k]
        if not sD['gen'] == parent_gen:
            continue
        if sD['name'] == parent_name:
            return k
    return None
   
#----------------------------------------

k = key_for_input_string(input, year=year)
if not k in D:
    print "search for: ", input
    print "Not found"
    sys.exit()
    
#----------------------------------------e
 
def add_gen(k):
    global i
    try:
        gen = D[k]['gen']
        i = int(gen)
    except:
        gen = i + 1
        
    pre = ('g' + str(gen)).ljust(3)
    return pre + ' ' +  k
                
#----------------------------------------

# globals are bad!

def do_parent_stuff(k, pL):
    for parent_type in parent_types:
        p = key_for_parent(k, kind=parent_type)
        if not p:   # find parent by name
             try:
                 p = D[k][parent_type]
             except:
                 p = None
        pL.append(p)
        if not p:
            continue
        do_parent_stuff(p, pL)

#----------------------------------------

g = D[k]['gen']
depth += g
sp = ' . ' * g
print 'g' + str(g) + sp + ' ' + k


parent_types = ['father','mother']
            
pL = list()
do_parent_stuff(k,pL)

sL = list()
for e in pL:
    if not e:
        continue
    mod = add_gen(e)
    sL.append(add_gen(e))
    
pL = sL[:]

#---------------------------------------------
# filter and format output

for e in pL:
    gen, rest = e.split(' ', 1)
    g = int(gen[1:])
    if g > depth:
        continue
    print gen + g * ' . ' + rest





