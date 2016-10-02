KPCB Engineering Fellows Program - Challenge Problem
====================================================
Applicant: Hunter Lee
Email: hl130@duke.edu  
Language: Python 3.5.1  

Problem:  
--------
Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). Your data structure should be optimized for algorithmic runtime and memory usage. You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

The solution should be delivered in one class (or your language's equivalent) that provides the following functions:

* **constructor(size)** : return an instance of the class with pre-allocated space for the given number of objects.
* **boolean set(key, value)** : stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
* **get(key)** : return the value associated with the given key, or null if no value is set.
* **delete(key)** : delete the value associated with the given key, returning the value on success or null if the key has no value.
* **float load()** : return a float value representing the load factor ((items in hash map)/(size of hash map)) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.

If your language provides a built-in hashing function for strings (ex. hashCode in Java or __hash__ in Python) you are welcome to use that. If not, you are welcome to do something naive, or use something you find online with proper attribution.


Solution:
---------
Hash Map Data Structure is implemented using Robin Hood hashing. Hashing is done using Python's built-in hash() function. Runtime considerations were given, and linear probing was chosen because it provides better performance thanks to locality of reference. The Robin Hood algorithm is applied to reduce the variance of probe lengths of elements in the data structure. Shorter probe lengths mean shorter distance Hash Map has to traverse to retrieve a key-value pair, and the statistics script backs it up with numbers. Other hashing techniques considered include quadratic hashing and separate chaining.

Memory considerations include the use of string interning. Python, according to CPython, can intern strings that can save memory usage and potentially boost performance. Other considerations include avoiding use of generators, zip, enumerate, etc. to reduce overhead.

* **HashMapRH.py** : Hash map implementation using Robin Hood hashing
* **HashMap.py** : Naive hash map implementation using linear probing
* **HashMapTest.py** : Python unittest for HashMapRH
* **HashMapStats.py** : Quick statistics for runtime and variance to compare Robin Hood and naive implementations (takes a few seconds to run depending on size of the hash map)

To run test (Python 3.5.1):

    python HashMapTest.py
      or
    py -3 HashMapTest.py

To run statistics:

    python HashMapStats.py
      or
    py -3 HashMapStats.py


Performance Comparison:
---------
Sample run HashMapStats.py gives,

Variance in probe lengths: 1) Naive: 253129.6427774678  2) Robin Hood Hashing: 252874.37325051508
Robin Hood Hashing has lower variance. Difference in variance: 255.26952695270302

Performance - get(key): 1) Naive: 9.086416163391145e-06  2) Robin Hood Hashing: 3.950615723213542e-06
Performance - delete(key): 1) Naive: 5.925923584820314e-06  2) Robin Hood Hashing: 3.950615723213539e-06
For get(key), Robin Hood Hashing is faster by 5.135800440177602e-06 seconds
For delete(key), Robin Hood Hashing is faster by 1.9753078616067746e-06 seconds

We see generally better worst-case performance in the Robin Hood implementation. Runtime is not drastically different as both essentially are based upon linear probing. The gap seems to widen as variance increases.


Attribution:
---------
http://guilload.com/python-string-interning/
https://en.wikipedia.org/wiki/Hash_table#Robin_Hood_hashing
