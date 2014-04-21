
uses python 3.3

Insert string.ascii_uppercase into a hash table, t = LinearProbingHashST(M=13)
M is table size
$ python HashTables.py

Explore the distribution of bits after hashing a key with a hash function:
hash = (a * key) % M
where each variables a and M can be prime or non-prime
dependencies: openAddressing.py
$ python HashExperiments.py

HashTableExperiments.ipynb:
dependencies: openAddressing.py, visualizerAccumulator.py
This ipython notebook inserts the words from a "Tale of Two Cities" into
a hash table that uses Double Hash open adressing.
The plots show the cumulative mean cost of inserting the nth word into the table.
The peaks in cost indicate where the table is resized.

