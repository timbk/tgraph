## Tree class for visualisation of hirachical lists

# get the charactar for the pos(ition) of a node with width
def bracket_sign(width,pos,key='',espace=0):
    if key==None:
        return ''
    prep=('-' if width!=2 else '_') if pos==int((width-1)/2) else ' '
    prep=''.join([prep for i in range(espace+1)])
    if width==1:
        return prep+'-'
    elif pos==0:
        return prep+'/'
    elif pos==width-1:
        return prep+'\\'
    else:
        return prep+'|'

# tree class
class tree:
    # constructor
    def __init__(self):
        self.root_node=tree_node(None)
    # insert a new node with key ch at chain
    def insert(self,chain,ch):
        self.root_node.insert_child(chain,ch)
    def insertn(self,chain,chs):
        for ch in chs:
            self.insert(chain,ch)
    # finde the path to the given key (returns None if not found)
    def find(self):
        return False
    # simple print of the tree (for debuging)
    def sprint(self):
        self.root_node.sprint(0)
        return 
    # get all keys at depth
    def get_keys_depth(self,depth):
        return self.root_node.get_keys_depth(depth)
    # pretty print of the tree 
    def pprint(self,nindent=4):
        assert nindent>0
        for line in self.root_node.pprint(nindent):
            print(line)
    # get the width of the whole tree
    def get_width(self):
        return self.root_node.get_width()


# represents a node in the tree
class tree_node:
    # constructor
    def __init__(self,key):
        self.childs=list()
        self.key=key
        self.size=0
    # implement equality check 
    def __eq__(self,x):
        return self.key==x
    # add a new child at the path chain=[key1,key2,..]
    def insert_child(self,chain,ch):
        if len(chain)==0:
            if ch not in self.childs:
                self.childs.append(tree_node(ch))
                self.size+=1
                return True
            else:
                raise Exception('Error: tree_node: key <%s> already exists in %s'%(str(ch),str(chain)))
        else:
            pos=[i for i in range(len(self.childs)) if self.childs[i]==chain[0]]
            if len(pos)<1:
                raise Exception('Error: tree_node: key does not exist')
            if len(pos)>1:
                raise Exception('Error: tree_node: duplicated key')
            if self.childs[pos[0]].insert_child(chain[1:],ch):
                self.size+=1
                return True
        return False
    # simple print
    def sprint(self,indent):
        for curr in self.childs:
            print(''.join(['\t' for i in range(indent)]),curr.key)
            curr.sprint(indent+1)
    # get all keys at a specific depth
    def get_keys_depth(self,depth):
        if depth>0:
            ret=[]
            for cc in self.childs:
                ret+=cc.get_keys_depth(depth-1)
            return ret
        else:
            ret=[]
            for cc in self.childs:
                ret.append(cc.key)
            return ret
    # calculate the 'width' of this nodes subbranch 
    def get_width(self):
        if len(self.childs)==0:
            return 1
        ret=0
        for cc in self.childs:
            ret+=cc.get_width()
        return ret
    # build a Pretty PRINT of the graph
    def pprint(self,nindent):
        ckey=self.key if self.key!=None else ''
        if len(self.childs)==0:
            return [str(ckey)]
        else:
            spacer=''.join([' ' for i in str(ckey)])
            ret=[]
            for cc in self.childs:
                ret+=cc.pprint(nindent)
            for i in range(len(ret)):
                if i==int((len(ret)-1)/2):
                    ret[i]=ckey+bracket_sign(len(ret),i,self.key,nindent-len(ckey)%nindent-1)+ret[i]
                else:
                    ret[i]=spacer+bracket_sign(len(ret),i,self.key,nindent-len(ckey)%nindent-1)+ret[i]
            return ret




# generate a tree for testing purposes
def sample_tree():
    t=tree()
    t.insertn([],['a','b','c','d'])
    t.insertn(['a'],['1','2','3'])
    t.insertn(['b'],['x','y','z'])
    t.insertn(['b','x'],['!','?'])
    t.insertn(['c'],['hello'])
    return t
