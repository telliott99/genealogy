import os, sys

u = '/Users/telliott_admin'
p = u + '/Dropbox/Github/genealogy'

L = list()
dirs = [p + '/g' + str(n) for n in range(13)]
for d in dirs:
    sL = [d + '/' + f for f in os.listdir(d) if not f[0] == '.']
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

def extract_date(s):
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

def process(L,f):
    gen = L[0].split('=')[1].split('>')[0]
    name = L[1].split('<b>')[1].split('<')[0]
    father = extract_name(L[4].strip())
    mother = extract_name(L[5].strip())

    born = extract_date(L[2].strip())
    died = extract_date(L[3].strip())
    full = name + ' ' + '-'.join((born,died))
    #full = full.replace(no_data,'')
    
    f = f.split('/',6)[-1]
    # if f.split('/')[0] != gen: 1/0
    pL = [gen,name,full,father,mother,f]
    print '\n'.join(pL) + '\n'


for f in L:
    fh = open(f)
    data = fh.read().strip().split('\n')
    data = [s for s in data if not s == '']
    fh.close()
    try:
        process(data,f)
    except:
        print data
        sys.exit()

    
    