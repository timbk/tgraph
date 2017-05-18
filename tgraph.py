#!/usr/bin/python3
import sys
import ttree as tree

usage_message='usage: graph.py [-I X] inputfile1 inputfil2 ..\nwhere X is the indentation width'
notint_message='The parameter to \'-I\' must be a positive integer'

# extract information from line x of the input file
def spl_indent(x):
    i=0
    while i<len(x) and (x[i] in [' ','\t']):
        i+=1
    return i,x[i:]

# check sysargs
flist=sys.argv[1:]
if len(sys.argv)<2:
    print(usage_message)
    exit(0)
if sys.argv[1]=='-I':
    if len(sys.argv)<4:
        print(usage_message)
        exit(0)
    try:
        indent=int(sys.argv[2])
    except:
        print(notint_message)
        exit(0)
    if indent<=0:
        print(notint_message)
        exit(0)
    flist=flist[2:]
else:
    indent=10

# main loop
for fname in flist:
    # load data
    with open(fname) as f:
        data=filter(lambda x: len(x[1])>1,[spl_indent(i[:-1]) for i in f])

    # create graph and add central node
    depth=[-1]
    cnode=fname.split('.')
    cnode=' '.join(cnode[:-1]) if len(cnode)>1 else cnode[0]
    cnode=cnode.split('/')[-1]
    node_chain=[cnode]
    T=tree.tree()
    T.insert([],cnode)

    # add the rest of the nodes
    for i in data:
        while len(depth)>1 and i[0]<=depth[-1]:
            del depth[-1],node_chain[-1]
        T.insert(node_chain,i[1])
        depth.append(i[0])
        node_chain.append(i[1])

    # print result
    T.pprint(indent)
