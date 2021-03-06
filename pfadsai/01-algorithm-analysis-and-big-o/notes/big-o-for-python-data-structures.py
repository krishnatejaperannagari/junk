# Lists
# In Python lists act as dynamic arrays and support a number of common operations through methods called on them. The two most common operations performed on a list are indexing and assigning to an index position. These operations are both designed to be run in constant time, O(1).
# Let's imagine you wanted to test different methods to construct a list that is [0,1,2...10000]. Let go ahead and compare various methods, such as appending to the end of a list, concatenating a list, or using tools such as casting and list comprehension.

def method1():
    l = []
    for n in xrange(10000):
        l = l + [n]

def method2():
    l = []
    for n in xrange(10000):
        l.append(n)

def method3():
    l = [n for n in xrange(10000)]

def method4():
    l = range(10000) # Python 3: list(range(10000))

# %timeit method1()
# %timeit method2()
# %timeit method3()
# %timeit method4()
# 10 loops, best of 3: 162 ms per loop
# 1000 loops, best of 3: 820 µs per loop
# 1000 loops, best of 3: 307 µs per loop
# 10000 loops, best of 3: 77.7 µs per loop

# It is important to keep these factors in mind when writing efficient code. More importantly begin thinking about how we are able to index with O(1). We will discuss this in more detail when we cover arrays general. For now, take a look at the table below for an overview of Big-O efficiencies.
# Table of Big-O for common list operations

# Operation   Big-O Efficiency
# index []    O(1)
# index assignment    O(1)
# append  O(1)
# pop()   O(1)
# pop(i)  O(n)
# insert(i,item)  O(n)
# del operator    O(n)
# iteration   O(n)
# contains (in)   O(n)
# get slice [x:y] O(k)
# del slice   O(n)
# set slice   O(n+k)
# reverse O(n)
# concatenate O(k)
# sort    O(n log n)
# multiply    O(nk)


# Dictionaries
# Dictionaries in Python are an implementation of a hash table. They operate with keys and values, for example:

d = {'k1':1,'k2':2}
print(d['k1'])


# Something that is pretty amazing is that getting and setting items in a dictionary are O(1)! Hash tables are designed with efficiency in mind, and we will explore them in much more detail later on in the course as one of the most important data structures to undestand. In the meantime, refer to the table below for Big-O efficiencies of common dictionary operations:

# Operation   Big-O Efficiency
# copy    O(n)
# get item    O(1)
# set item    O(1)
# delete item O(1)
# contains (in)   O(1)
# iteration   O(n)