import os, sys, re
from get_location import p

p += 'source'
L = list()
dirs = [p + '/g' + str(n) for n in range(15)]
for d in dirs:
    sL = [d + '/' + f for f in os.listdir(d) if not f[0] == '.']
    sL.sort()
    L.extend(sL)

def test1():
    for e in L:
        print(e)
    sys.exit()
#test1()

D = dict()

no_data = '*'

'''
patterns for names:
y 
y *
y X Y
y X Y (Z)
y X c. Y
y [X Y](../gX/file)
y [X Y] (../gX/file)
others?
'''

def extract_name(t):
    L = t.split(' ', 1)
    symbol = L.pop(0)
    if not L:
        if not symbol in 'fmo-':
            print(t)
            sys.exit()
        return no_data
    s = L[0]

    if not '[' in s:
        return s.strip()
        
    else:
        # can use '(' and not '(..'
        # because already returned X Y (Z)
        name = s.split('(')[0]
        if not '[' in name and ']' in name:
            print('format error', name)
            sys.exit()
        if name[0] == '[':
            name = name[1:]
        if name[-1] == ']':
            name = name[:-1]
        return name 
        
def extract_year(s):
    m = re.search('\d\d\d\d', s)
    if m:
        return m.group(0)
    return no_data

'''
    dg = '0123456789 '
    sL = [c for c in s if c in dg]
    try:
        s = ''.join(sL)
        sL = s.split()
        for e in sL:
            if len(e) == 4:
                return e
    except:
        pass
'''

def process(data, fn):
    part1,part2,part3 = data.strip().split('<hr>')
    
    sL = part1.strip().split('\n')
    sL = [e for e in sL if not e == '']
    
    # gen = sL[0].split('=')[1].split('>')[0][1:] # no 'g'
    name = sL[1].split('<b>')[1].split('<')[0]
    
    born = extract_year(sL[2].strip())
    died = extract_year(sL[3].strip())
    
    father = extract_name(sL[4].strip())
    mother = extract_name(sL[5].strip())
        
    pL = [name,'b ' + born, 'd ' + died,
          'f ' + father, 'm ' + mother ]
    print('\n'.join(pL))
    
    sL = part2.strip().split('\n')
    sL = [e for e in sL if not e == '']
    spouseL = [e for e in sL if e.startswith('o')]
    
    if not spouseL:
        print('o *')
    else:
        for line in spouseL:
            print('o ' + extract_name(line))
    f = fn.split('/',7)[-1]
    print(f)
    print()

def run():
    for fn in L:
        fh = open(fn)
        data = fh.read().strip()
        fh.close()
        process(data,fn)

if __name__ == "__main__":
    run()