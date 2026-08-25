#----------------------- Chapter -9- itertools and functional programming tools ---------------------------------

#itertools - infinite iterators
#itertools are the builtin functions in python which are useful for iterations
#itertools are useful to iterate over large iteratable datasets like list,tuple and dictionary
#most useful in iterations permutations and combinations

print("*"*25+"Itertools module"+"*"*25)
import itertools
for i in itertools.count(10,5):   #count(start,step) used to iterate through infinite numbers
    print(i)
    if i>40:
        break

#cycle() method is used to iterate in a cycle through the itrable object in a specified iterations
#next() is used to access the next element in the iterable object at end of object the next element is the starting element in the array
fruits=itertools.cycle(['APPLE','banana','orange','cherry'])
for i in range(10):
    print(next(fruits))

#repeate() used to repeate the same data infite times until you iterate through it

a=[1,2,3,4]
for j in itertools.repeat(a,10):#repeates a 10 times
    print(j)

#itertools combinational tools
print("*"*25+" itertools combinational tools "+"*"*25)

#permutations() provides the all possible permutations of elements provided with permutation size
#permutations(iterable oject,permutation size)
permutations=list(itertools.permutations(['a','b','c'],2))
print(f"permutations for {['a','b','c']} in size of 2 are:",permutations)

#combinations() provides all possible combianations of the oject you provide with the combination size
#combinations(iterable object,combinations size)
combinations=list(itertools.combinations('python',3))
print('combinations for python are :',combinations)

#combinations with replacement 
#all combinations are generated with replacement of elements

combinations=list(itertools.combinations_with_replacement("abc",2))
print("Combinations with replacement is :",combinations)

#product() method provides cartesian product for ex:(1,2),(a,b) = (1*a),(2*a),(1*b),(2*b)
#it generates all possible combinations by taking 1 element from each iterable object
#can use repeat parameter to repeat one iterable objects as many and generate cartesian product

cartesian_product=list(itertools.product([1,2],[3,4]))
print("cartesian product of [1,2] and [3,4] is:",cartesian_product)

car_pro2=list(itertools.product([1,0],repeat=2))
print("Cartesian product of [1,0] repeat=2 is:",car_pro2)

#Itertools filtering and slicing 
#chain() combines all iterables provided into a single iterable object
print("*"*25+" filtering and slicing "+"*"*25)

chain=list(itertools.chain([1,2],[2,3],[3,4],[4,5]))
print("Total combined iterables are:",chain)

slice=list(itertools.islice(itertools.count(),1,10,2))
print("Itertool islice method :",slice)

#take while/drop while
#take while takes the element if the functions returns true
#drop while drops element if function in drop while is true

take_while=list(itertools.takewhile(lambda x:x<5, [1,2,3,4,5,6,7,8,9]))
print("Take_while",take_while)

drop_while=list(itertools.dropwhile(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9]))
print("Drop_while:",drop_while)

#filter false 
#filter false is opposite of filter it elemenets the filter element but gives the elements which will not be in filter true

filter=list(itertools.filterfalse(str.isupper,'aAbBcCdD'))
print('filter_false:',filter)

#mask selection you can acces the required element in an iterable object by providing the list of indexs to select
selection=list(itertools.compress('ABCDE',[1,0,1,0,1]))
print("mask selection:",selection) #[A,C,E]

#groupby is a method to groups the consecutive elements that have same key/value
#returns an iterator of (key,group) pairs
#group is itself a iterator

data = [
 {'dept': 'Eng', 'name': 'Alice'},
 {'dept': 'Eng', 'name': 'Bob'},
 {'dept': 'HR', 'name': 'Carol'},
 {'dept': 'HR', 'name': 'Dave'},
]

data.sort(key=lambda x:x['dept'])
print(data)

for dept,members in itertools.groupby(data,key=lambda x:x['dept']):
    names=[m['name'] for m in members]
    print(f"{dept} ---->  {names}")

#zip_longest,starmap,accumulate
#Zip_longest is used to combine two iterables until the longest iterable objects ends 
#used to combine the unequal length of iterables

a=[1,2,3,4]
b=[5,6,7]
zip_longest=list(itertools.zip_longest(a,b,fillvalue='x')) #fillvalue is a value that will replace if an empty place occurs
print('after combining the both iterators with zip_longest method:',zip_longest)

#starmap is like the map function starmap applies the functions on each elements in an iterables but here in 
#starmap ierable elements are the tuples or dictionarys starmap automatically unpacks the tuples or dictionary
#and applies functions to it

powers=list(itertools.starmap(pow,[(1,2),(2,3),(4,5)]))
print("Calculating the power of numbers with starmap function:",powers) #(1**2)=1 ,2**3 = 8,4**5=1024

#accumulate is used to calculate the accumulate sum or product of the numbers that we provide

accumulate=itertools.accumulate([2,4,6,8,10])
print("The accumulate sum of the numbers given is :",list(accumulate))

import operator
accumulate_pro=itertools.accumulate([1,2,3,4,5],operator.mul)
print("Accumulate product of the numbers is:",accumulate_pro)

#functools--functional utilities
#functools is a built in python module which provides the functionalities like partial,lru_cache, and reduce
#partial is a functool method creates a new function with one or more prefilled arguments of an existing function
#we can hold the prefilled arguments and pass the remaining arguments and call the newly created function to exicute the 
#before existing function
#let a(e,f) be the existing function then partial function is b=partial(a(a=2)) -->b(3)
#partial commonly used in callbacks,event handling
print("*"*25+" functools-functional utilities "+"*"*25)
import functools
def add(a,b):
    return a+b
partial_func=functools.partial(add,b=10)
print("sum of 10,20 with partial function is:",partial_func(20))

#lru_cache is a decorator in functools it is used to store the functions cache once the function called the results
#stored if same function called with the same arguments instead of executing the function the cache stored in the lru
#cache is returned so there no unnecesory function calls
#lru_cache has a parameter called maxsize, we can define the maximum size of the cache by providing the maxsize argument

from functools import lru_cache

@lru_cache(maxsize=120)
def square(a):
    print("Calculating.........")
    return a**2
print(square(10))
print(square(10))

#reduce method in functools applies the function repeatedly until it returns a single value it process the elements
#from left to right and returns a single valur from the iterable object

from functools import reduce
a=[1,2,3,4,5,6]
product = reduce(lambda x,y:x*y,a)
print(f"product of the numbers {a} with reduce function is: ",product)
