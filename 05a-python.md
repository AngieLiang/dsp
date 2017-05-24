# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

* Similarity:  
        1. Duplicates - Both tuples and lists allow for duplicates.  
        2. Indexing, Selecting, & Slicing - Both tuples and lists index using integer values found within brackets. So, if you want the first 3 values of a given list or tuple, the syntax would be the same.  
        3. Comparing & Sorting - Two tuples or two lists are both compared by their first element, and if there is a tie, then by the second element, and so on. No further attention is paid to subsequent elements after earlier elements show a difference.  
* Differnece:  
        1. Syntax - Lists use [], tuples use ()  
        2. Mutability - Elements in a given list are mutable, elements in a given tuple are NOT mutable.  
        3. Homo vs. Heterogeneity of Elements - List objects are homogenous (objects/subjects of the same type); Tuple objects are heterogeneous (mostly heterogenous objects, but not forced)  
        4. Looping vs. Structures - Although both allow for looping (for x in my_list...), it only really makes sense to do it for a list. Tuples are more appropriate for structuring and presenting information.  
* Tuples will work as keys in dictionary:  
        As hashtables (dictionaries) require that its keys are hashable and therefore immutable, only tuples can act as dictionary keys, not lists.  
   
    
    

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

* Similarity:  
They are both data structures and both mutable.  
* Difference:  
        1. Sets can not contain duplicates while lists can.  
        2. Sets are unordered; lists are ordered.  
        3. sets can contain only objects that are hashable; lists can contain any kind of object.   
        4. Sets can be used to perform operations such as unions and intersections.   
        5. As list are ordered list are comparatively slow to execute whereas sets are fast.  
* Example:  
        Sets:  
            a = set([1, 2, 3, 4])  
            b = set([3, 4, 5, 6])  
        Lists:  
            a = [1, 1, 9, 2, 3, 4, 2, 6, 7, 8, 6]  
            queue = ['a', 'b', 'c', 'd', 'c']  
    
* Sets are significantly faster when it comes to determining if an object is present in the set.  
        Sets are implemented using hash tables. Whenever you add an object to a set, the position within the memory of the set object is determined using the hash of the object to be added. When testing for membership, all that needs to be done is basically to look if the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list needs to be searched, which will become slower as the list grows.  
    
    

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is an anonumous function at runtime.  
Python supports a style of programming called functional programming where you can pass functions to other functions to do stuff.   
* Examples:  
    1.  
        pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]  
        pairs.sort(key=lambda pair: pair[1])  
    2.  
        cubes = list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  
    3.  
        sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))  
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.  
basic syntax for list comprehensions: [EXPRESSION FOR ELEMENT IN SEQUENCE]  
* Examples:  
    1. map:  
        squares = [x**2 for x in range(10)]  
        squares = list(map(lambda x: x**2, range(10)))  
    2. filter:  
        special_squares = [ s for s in [ x**2 for x in range(10) ] if s > 5 and s < 50 ]    
      
        squares = map(lambda x: x**2, range(10))  
        special_squares = list(filter(lambda x: x > 5 and x < 50, squares))    
    List comprehensions are more clear and consistent.  

* set comprehensions
        The syntax for set comprehensions is almost identical to that of list comprehensions, but it uses curly brackets instead of square brackets. The pattern is {EXPRESSION FOR ELEMENT IN SEQUENCE}.  
        The result of a set comprehension is the same as passing the output of the equivalent list comprehension to the set function.  
        eg:  
        nums = {n**2 for n in range(10)}  
* dictionary comprehensions
        dict comprehensions allow you to express the creation of dictionaries at runtime using a similarly concise syntax.  
        A dictionary comprehension takes the form {key: value for (key, value) in iterable}.   
        eg:  
        {x: x**3 for x in range(10) if x**3 % 4 == 0}  

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





