from get_location import p

p += 'scripts'

fn = p + '/db.txt'
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