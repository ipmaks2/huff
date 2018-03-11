import heapq
import huff_tools

class HuffNode(object):
    def __init__(self, pair = None, n1 = None, n2 = None):
        self.freq = 0
        self.val = list()
        self.left = None
        self.right = None
            
        if pair:
            self.freq += pair[1]
            self.val.append(pair[0])
            return
        
        if n1:
            self.freq += n1.freq
            self.val += n1.val
            self.left = n1
            
        if n2:
            self.freq += n2.freq
            self.val += n2.val
            self.right = n2
    
    def __cmp__(self, other):
        if self.freq < other.freq:
            return -1
        elif self.freq == other.freq:
            return 0
        else:
            return 1
    
    def goLF(self, codes, prevpath=None ):
        if not prevpath:
            prevpath = []
        if self.left:
            self.left.goLF(codes, prevpath + [0])
        if self.right:
            self.right.goLF(codes, prevpath + [1])
        if len(self.val) == 1:
            codes[self.val[0]] = huff_tools.getBitMask(prevpath[:]) ## TODO not needed copy
            # print 'V:{}, Code: {}'.format(self.val, prevpath)
            
            
    
    # def __str__(self):
    #    return 'Freq: {}, Val: {}'.format(self.freq, self.val)
    
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right is not None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        if len(self.val) == 1:
            ret += "\n" + ("    "*depth) + str(self.freq) + '({})'.format(self.val)
        else:
            ret += "\n" + ("    "*depth) + str(self.freq)       

        # Print left branch
        if self.left is not None:
            ret += self.left.__str__(depth + 1)

        return ret

     
def getCodes(freq_tups, **kwargs):
    n = len(freq_tups)
    i = 1 
    h = list()
    codes = dict()

    while i <= n:
        heapq.heappush(h, HuffNode(freq_tups.pop()))
        i += 1 

       
    k = n + 1    
    while (k <= 2*n - 1):
        ni = heapq.heappop(h) # getMin
        nj = heapq.heappop(h) # getMin
        heapq.heappush(h, HuffNode(n1=ni, n2=nj))
        k += 1

    if 'debug' in kwargs:
       print h[0]

    h[0].goLF(codes)
    return codes


if __name__ == '__main__':

    tups = [('1', 100), ('2', 90), ('4', 85), ('8', 50), ('7', 20), ('3', 10), ('5', 10), ('6', 10), ('9', 9), ('0', 9)]        
    # print h[0]        
    codes = getCodes(tups, debug=1)
    for c, bits in codes.items():
        print c, bits

