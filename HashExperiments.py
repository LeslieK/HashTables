from openAddressing import DoubleProbingHashST
import string


def doubleHashLinearProbe(M=11):
    d = DoubleProbingHashST(M)
    count = 0
    with open("TaleOfTwoCities.txt", mode='r', encoding='utf-8') as f:
        for line in f:
            words = (word for word in line.split() if len(word) > 7)
            for w in words:
                if d.get(w):
                    d.put(w, d.get(w) + 1)
                else:
                    d.put(w, 1)
                count += 1
    print(count)
    d.a.plotData()


def makeKeys(data):
    letters = string.ascii_uppercase
    keys = []
    it = map(letters.find, data)
    for i in it:
        keys.append(i)
    return keys


def bits(n):
    """
    convert an integer to binary
    """
    if n == 0:
        return 0
    res = []
    while n > 0:
        res.append(n % 2)
        n = n // 2
    return int("".join([str(b) for b in res[::-1]]))


def hashFuncExp(a, M):
    """
    explore the distribution of bits as a result
    of hashing a key using
    different values for a and M
    """

    def hfunc():
        def f(k):
            return (a * k) % M
        return f

    f = hfunc()
    keys = makeKeys('ABCRSTXYZ')

    for k in keys:
        h = f(k)
        print(bits(h), string.ascii_uppercase[k])
    print()


def explorePrimes():
    print('neither prime')
    hashFuncExp(6, 128)

    print('a prime, M not prime')
    hashFuncExp(5, 128)

    print('a not prime, M prime')
    hashFuncExp(6, 127)

    print('a prime, M prime')
    hashFuncExp(5, 127)

#############################################
if __name__ == "__main__":

    explorePrimes()





