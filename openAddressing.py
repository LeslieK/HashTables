import math
import string
from visualizerAccumulator import VisualAnalyzer


DELTA = [0, 0, 1, 1, 3, 1, 3, 1, 5, 3, 3, 9, 3, 1, 3, 19, 15, 1, 5, 1, 3, 9, 3, 15, 3, 39, 5, 39, 57, 3, 35, 1]
PRIMES = [2 ** k - DELTA[k] for k in range(len(DELTA))]
LOAD = .5
R = 31

def trace_Py2(f):
    indent = '    '
    def _f(*args):
        signature = '{}({})'.format(f.__name__, ', '.join(map(repr, args)))
        print('{}--> {}'.format(trace.level * indent, signature))
        trace.level += 1
        try:
            result = f(*args)
            print('{}<-- {} -> {}'.format((trace.level - 1) * indent, signature, result))
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f

def trace(f):
    indent = '    '
    def _f(*args):
        nonlocal level  # python 3
        signature = '{}({})'.format(f.__name__, ', '.join(map(repr, args)))
        print('{}--> {}'.format(level * indent, signature))
        level += 1
        try:
            result = f(*args)
            print('{}<-- {} -> {}'.format((level - 1) * indent, signature, result))
        finally:
            level -= 1
        return result
    level = 0
    return _f

class DoubleProbingHashST:
    """
    This implementation hashes ascii characters.
    """

    def __init__(self, M, keys=None, values=None):
        self.lgM = round(math.log(M, 2))
        self.M = M             # size of table
        self.tombs = 0         # number of to-be-deleted keys
        self.count = 0         # number of equality tests

        self.a = VisualAnalyzer(13600, 12, title="Double Hashing Linear Probing Hash Table")

        if keys:
            self.keys = keys
            self.values = values
            self.N = len(keys)
        else:
            self.keys = [None] * self.M
            self.values = [None] * self.M
            self.N = 0         # number of key-value pairs


    def _hash(self, key):
        return (11 * key) % self.M

    def _hash2(self, key):                           # 26 + 5 = 31
        # hash must be nonzero
        # hash must be relatively prime with M  (M must be prime)
        q = PRIMES[self.lgM - 1]       # get largest prime < size
        return q - (key % q)           # q, q-1, ..., 1 (never 0!)

    def avgCostHit(self):
        """
        return avg number of probes for a search hit
        assumes universal hashing
        """
        alpha = (self.N + self.tombs) / self.M
        return .5 * (1 + 1 / (1 - alpha))

    def avgCostMiss(self):
        """
        return avg number of probes for a search miss
        assumes universal hashing
        """
        alpha = (self.N + self.tombs) / self.M
        return .5 * (1 + 1 / (1 - alpha) ** 2)

    #@trace
    def put(self, key, value):
        if isinstance(key, str):
            key = toInt(key)
        if self.N + self.tombs >= self.M * LOAD:
            self._resize(self.lgM + 1)
        i = self._hash(key)
        skip = self._hash2(key)
        while self.keys[i] is not None:
            self.count += 1
            # 'equals' applies to strings, numbers
            if self.keys[i] == key and not self._isTombstone(i):
                self.count += 1     
                # key already in table
                self.values[i] = value  # update value

                self.a.addDataValue(self.count)
                self.count = 0

                return i
            elif self.keys[i] == key:
                self.count += 2
                # update tombstone
                self.values[i] = value
                self.tombs -= 1
                self.N += 1

                self.a.addDataValue(self.count)
                self.count = 0

                return i
            # continue probing
            self.count += 2
            i = (i + skip) % self.M  # M must be prime
        self.keys[i] = key
        self.values[i] = value
        self.N += 1

        self.a.addDataValue(self.count)
        self.count = 0

        return i   # index

    #@trace
    def get(self, key):
        if isinstance(key, str):
            key = toInt(key)
        i = self._hash(key)
        skip = self._hash2(key)
        while self.keys[i] is not None:
            self.count += 1
            if self.keys[i] == key and not self._isTombstone(i):
                self.count += 1
                # found key
                #self.a.addDataValue(self.count)
                #self.count = 0

                return self.values[i]
            # continue probing
            self.count += 1
            i = (i + skip) % self.M

        #self.a.addDataValue(self.count)
        #self.count = 0
        return None

    def allkeys(self):
        for i in range(self.M):
            if self.keys[i] is not None and not self._isTombstone(i):
                yield self.keys[i]
            else:
                continue

    def delete(self, key):
        self.put(key, None)
        self.tombs += 1
        self.N -= 1
        if (self.N) <= self.M * LOAD * .25:
            self._resize(self.lgM - 1)

    def _isTombstone(self, i):
        return self.values[i] is None

    #@trace
    def _resize(self, new_lgM):
        # size is prime
        new_size = PRIMES[new_lgM]
        t = DoubleProbingHashST(new_size)  # a new hash table
        for i in range(self.M):
            # rehash keys into new hash table
            if self.keys[i] is not None and not self._isTombstone(i):
                t.put(self.keys[i], self.values[i])
        self.keys = t.keys
        self.values = t.values
        self.M = new_size
        self.lgM = new_lgM  # set lgM
        self.tombs = 0
        self.count += 2

def toInt(s):
    """
    s: an ascii string
    """
    key = 0
    for c in s:
        key = (R * key + ord(c))  # ord() assumes c is encoded to 1 byte
    return key

def toStr(n):
    """
    n: a number
    returns a string 1-byte characters (a word)
    """
    stack = []
    while n > 0:
        c = n % R
        n = n // R
        print(c, chr(c))
        stack.append(c)
    new_string = ''.join(map(chr, stack[::-1]))
    return new_string


    


    n >> R


     










    
