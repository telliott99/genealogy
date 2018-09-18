import os, sys

u = '/Users/telliott_admin'
p = u + '/Dropbox/Github/genealogy'

L = list()
dirs = [p + '/g' + str(n) for n in range(15)]
for d in dirs:
    sL = [d + '/' + f for f in os.listdir(d) if not f[0] == '.']
    sL.sort()
    L.extend(sL)

D = dict()

no_data = '*'

def extract_name(s):
    if len(s) == 1:
        return no_data
    if s[2] == '[':
        s = s[3:]
        return s.split(']')[0]
    else:
        return s[1:].strip()

def extract_year(s):
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
    return no_data
    


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
    print '\n'.join(pL)
    
    sL = part2.strip().split('\n')
    sL = [e for e in sL if not e == '']
    spouseL = [e for e in sL if e.startswith('o')]
    
    if not spouseL:
        print 'o *'
    else:
        for line in spouseL:
            print 'o ' + extract_name(line)
    f = fn.split('/',6)[-1]
    print f
    print

def run():
    for fn in L:
        fh = open(fn)
        data = fh.read().strip()
        fh.close()
        try:
            process(data,fn)
        except:
            print data
            sys.exit()

if __name__ == "__main__":
    run()