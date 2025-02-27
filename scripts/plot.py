import sys
from setup_parser import parser

args = parser.parse_args()
from get_database import D


'''
Files deal with exact dupes by appending birth year

But this doesn't work for initial search by name
Also, want to allow search with part of a name

Add an optional restriction: birth year
python plot.py -n "Tho" -b 1955
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

k = key_for_input_string(args.name, year=args.born)
if not k in D:
    print("Searched for: ", args.name)
    print("Not found")
    sys.exit()

#------------------------------------------------

'''
Usual situation, I have a key, namely:
Thomas Anthony Elliott 1955
I desire a particular parent
Do not allow relaxed search here.

Record will contain parents name but not
necessarily the birth year, so must search dict for key.
'''

# returns key if it exists, or None
def key_for_parent(k_in, kind='father'):
    if not k_in in D:
        return None
    parent_name = D[k_in][kind]
    parent_gen = D[k_in]['gen'] + 1

    for k in D:
        # to make name search work better
        if not D[k]['gen'] == parent_gen:
            continue
        if D[k]['name'] == parent_name:
            return k
    return None
                       
#----------------------------------------
# recursive call for each of parents
# generates depth-first search
# this version is very wasteful
# we generate the whole list, filter for depth later

def do_parent_stuff(k, pL):
    for parent_type in parent_types:
        g = D[k]['gen'] + 1

        p = key_for_parent(k, kind=parent_type)
        if p:
            # we append a real key
            # might as well look up the generation now
            pL.append((g,p))    
          
        else:
            # find parent by name
            n = D[k][parent_type]
            if not n:
                return
            # or we append a tuple of name, gen
            g = D[k]['gen'] + 1
            pL.append((g,n))
            return
        
        do_parent_stuff(p, pL)
       

parent_types = ['father','mother']

# have k from input string above
g = D[k]['gen']  
pL = [(g,k)]
do_parent_stuff(k,pL)

depth = args.depth
depth += g  # adjust depth for starting generation

# adjust depth for a logic error I haven't found yet
depth -= 1

# filter and format output

for g, rest in pL:
    if g > depth:
        continue
    print(('g' + str(g)).ljust(3) + g * ' . ' + ' ' + rest)

