# ==================================================================
import collections

list1 = [12, 23, 45, 5, 6, 2, 86, 2]

print(sum(list1))
counter_list = collections.Counter(list1)

for el, counter in counter_list.items():
    # print(f"element {el} and its count is --> {list1.count(el)}")
    print(f"element {el} and its count is --> {counter}")
# ==================================================================
#  Merged two sorted Lists..

list1 = [12, 23, 45, 5, 6, 2, 86, 2]
list1.sort()
list2 = [22, 23, 55, 25, 56, 52, 46, 26, 52]
list2.sort()

list1_length = len(list1)
list2_length = list2.__len__()
list1_counter = 0
list2_counter = 0
merged_list = []

while (list1_counter < list1_length) and (list2_counter < list2_length):
    list1_element = list1[list1_counter]
    list2_element = list2[list2_counter]

    if list1_element < list2_element:
        merged_list.append(list1_element)
        list1_counter = list1_counter+1
    else:
        merged_list.append(list2_element)
        list2_counter = list2_counter+1

if list2_counter<list2_length:
    merged_list.extend(list2[list2_counter::])

if list1_counter< list1_length:
    merged_list.extend(list1[list1_counter::])


# ==================================================================
list1 = list(range(1,12, 1))
list_last_3 = list1[-3:]
list_last_3 --> [9, 10, 11]
list_reverse = list1[::-1]
list_reverse --> [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
combined_list =  list1 + list2

# =================== Left and Right Rotations ==============================================
if direction == 'left':
    # Rotate left
    return lst[positions:] + lst[:positions]
elif direction == 'right':
    # Rotate right
    return lst[-positions:] + lst[:-positions]
# ====================== Even numbers ============================================
even_numbers = [el for el in list1 if el%2==0]
odd_numbers = [el for el in list1 if el%2!=0]
# ========================Second Highest number==============================
first, second = float('-inf'), float('-inf')
list1 = list(range(1, 12, 1))

for el in list1:
    if el >= first:
        second = first
        first = el
    if (el < first) and (el > second):
        second = el
# =============== Using LT or GT to sort and Lambda to sort ===================================================

first, second = float('-inf'), float('-inf')
list1 = list(range(1, 12, 1)) + [12, 11, 33]

class splclass:
    def __init__(self, pr, cy):
        self.city = cy
        self.person = pr

    def __eq__(self, other):
        return self.city == other.city

    def __repr__(self):
        string_ret  = str(f"{self.city, self.person}")
        return string_ret

    def __gt__(self, other): # Or also __lt__
        return self.city < other.city

o1 = splclass('P1', 'Hyd')
o2= splclass('P2', 'Lon')
o3= splclass('P3', 'Hyd')

list2 = [o1, o2, o3]
# counter = list2.count(o1)
# list2.sort(key= lambda obj: obj.city) >> Labmda to sort.
list2.sort()
print(list2)
# ================= Creating Counter functionality =================================================
first, second = float('-inf'), float('-inf')
list1 = list(range(1, 12, 1)) + [3, 4, 4, 12, 11, 33]

counter_dict= dict()

for el in list1:
    if counter_dict.get(el) is None:
        counter_dict[el] = 1
    else:
        counter_dict[el] = counter_dict[el]+1
print(223)
# ======================== Using Set Diff ==========================================
first, second = float('-inf'), float('-inf')
list1 = list(range(1, 12, 1)) + [3, 4, 4, 12, 11, 33]

counter_dict= dict()

even_numbers = set([el for el in list1 if el%2==0])
odd_numbers = set(list1).difference(even_numbers)
print(233)
# ==================================================================
t1 = (2,3, 4)
joined_str = "-".join(map(str, t1))
print(joined_str) #--> "2-3-4"
# ==================================================================
from functools import reduce
list1 = [1, 2, 3, 4, 5]

cumulative_sum = [sum(list1[:index]) for index in range(1,5)]

mul_fun = lambda x,y: x*y
cumulative_mul = [reduce(mul_fun, list1[:index]) for index in range(1,5)]

# ==================================================================
from functools import reduce

# Using map and reduce to calculate the product of squares of even numbers
numbers = [1, 2, 3, 4, 5, 6]
result = reduce(lambda x, y: x * y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# Print the result
print(result)


# Using reduce with a start value (10) to calculate the product of squares of even numbers
start_value = 10
result = reduce(lambda x, y: x * y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)), start_value)
print(result) #Prints 23040 instead of 2340 as we start with 10

# Using map, filter reduce,
cumulative_multiplication = lambda x, y: x * y
square_num = lambda x: x ** 2
filter_even_numbers = lambda x: x % 2 == 0
start_vale_cumulative_mult = 10
result2 = reduce(cumulative_multiplication, map(square_num, filter(filter_even_numbers, numbers)), start_vale_cumulative_mult)
print(result2)


# ===================== Randomize numbers in the list =============================================
import random
list1 = [11, 22, 33, 44, 55]
random_index = list(range(1,5))
# Shuffle the list in-place
randomized_numbers=  random.shuffle(random_index)
random_list = [list1[el] for el in random_index]
print(random_list)
# ====================== Sort a tuple on second element ============================================
t1 = ((1, 3), (23, 4), (123, 1))
sorted(t1, key=lambda tp: tp[1])
# ======================Dictionary from tuple ============================================
t1 = ((1, 3), (23, 4), (123, 1), (5, 12), (22,5))
new_dict = { el[0]:el[1] for el in t1}
new_dict2 = dict(t1) # Same as above.
# ==================Reversing a tuple based on second element.====================================
t1 = ((1, 3), (23, 4), (123, 1), (5, 12), (22,5))
reversed_t1 = sorted(t1, key=lambda el: el[1])
print(reversed_t1)

# ====================Flattening multi level list============================
t1 = ((1, 3), (23, 4), (123, 1), (5, 12), (22,5))
first_level = [el for el in t1]

# Flatten the elements into a list using a list comprehension
second_level = [item
                  for subtuple in t1
                  for item in subtuple]

print(first_level)
print(second_level)

# ======================Tuple with a conditional logic=====================================
list1 = list(range(1, 10))

sq_t1 = [(el, el*el) for el in list1 if el%2==0]
print(sq_t1)
# for list in list or tuple in a tuple traversal
sq_flattened = [el_sub
    for el in sq_t1
        for el_sub in el
]
# Here note the order, its slightly counter intuitive, but when you look for loop inside for loop, its clear.

# ===================Set Default is to add elements in Dictionary ===============================
airports_dict = {
    'New York': ['JFK', 'LaGuardia', 'Newark'],
    'Los Angeles': ['LAX', 'Burbank', 'Long Beach'],
    'Chicago': ['OHare', 'Midway', 'Gary'],
    'San Francisco': [],  # No airports in this city
    'Miami': ['Miami International', 'Fort Lauderdale-Hollywood']
}

updated_dict={}
for key, value in airports_dict.items():
    # print(value + ['A new airport'])
    updated_dict.setdefault(key, value + ['A new airport'])

print(updated_dict)

# =============Sort by value ====================================
# Define a dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sort the dictionary based on keys
sorted_dict = dict(sorted(my_dict.items()))
# Sort the dictionary based on keys in descending order
sorted_dict_descending = dict(sorted(my_dict.items(), reverse=True))

# Below sorts based on second value. i.e not on key, but on value.
a1 = sorted(my_dict.items(), key = lambda x: x[0], reverse=True)
new_dict = dict(a1)

# Print the sorted dictionary
print(sorted_dict)

Logic is: dict (list of tuples) -->  becomes dictionary
#So first a items used
dict([(t1, t2), (t3, t4)]) --> {'t1':t2, 't3':t4}

# ==================================================================
# Define a dictionary
dict1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

new_dict = { key:value for key,value in dict1.items() if key%2==0 }
print(new_dict)
# ==================================================================
list1 = list(range(1, 10))
list2 = list(range(1, 10, 2))
#Check elements if the second list in first list
a1 = [el2 for el2 in list2 if el2 in list1]

# ============Flattened list =========================================
list1 = [[1, 2], [3, 4], [5, 6]]
flat_list1 = [el2 for el1 in list1 for el2 in el1 ]
print(flat_list1)

# ===================Convert a tuple to list=============================
t1 = ((1,2),(3,4))
t2 = [
        [el2 for el2 in el1]
        for el1 in t1
    ]
# --> t2 will be [[1,2], [3,4]]

# ===================Sort list of tuples on a specific element ====================================
t1 = [(11,2),(8,9), (3,4)]
t1.sort(key=lambda x:x[0])
or
t1.sort(key=lambda x:x[1])
# ==================================================================

t1 = [ [el for _ in range(1,4)]
for el in range(1,5)
    ]
# t1  --> [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
t2 = [el2
    for el1 in t1
        for el2 in el1
]
print(tuple(t2)) #[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
# ==================================================================

t1 = [ (el,)*3 for el in range(1,5) ]
# t1  --> [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]

t3 = [sub_el
for el in [ (el,)*3 for el in range(1,5) ]
    for sub_el in el]

The middle line is basically t1 in the first command
t3 flattens the elements

# ===================Creating dictionary from lists =============================
from collections import Counter
list1 = [1, 2, 3, 4]
list2 = [11, 22, 33, 44]
len_list1 = len(list2)
dict1 = dict((list1[index], list2[index])  for index in range(0, len_list1))

# Two lists of the same size
keys_list = ['a', 'b', 'c', 'd']
values_list = [1, 2, 3, 4]
# Create a dictionary from the two lists
my_dict1 = {key: value for key, value in zip(keys_list, values_list)}
my_dict2 = dict((key, value) for key, value in zip(keys_list, values_list))
my_dict3 = {key:value for key,value in zip(keys_list, values_list) if value%2==0}
# ==================================================================
# Using if AND if-else in list expression
list1 = [11, 1, 4, 5, 6, 8]
list2 = [11, 6, 8, 55, 66, 88]

common_element = [el
                  for el in list1
                  if el in list2
                  ]

replace_missing_elements = [el
                   if el in list2 else 222
                   for el in list1
                  ]

print(common_element)
print(replace_missing_elements)

list3 = list1.insert(4, 899)
print(list3)
# =====================Average of tuple elements ===================================
import statistics as sts
t1 = ((1,2,3), (3,4,5), (8,9,12))
means_t1 = [ sts.mean(el)
             for el in t1
           ]
print(means_t1)
# ====================Sorting using sorted and sort =====================================
import statistics as sts
t1 = ((1,2,3), (3,4,5), (8,9,12))
t2 = [(1,2,3), (3,4,5), (8,9,12)]
sorted_t1 = sorted(t1, key=lambda x: x[1])
t2.sort(key=lambda x:x[1])

print(sorted_t1)
print(t2)
# ======================Using Filtering ==============================
import statistics as sts
t1 = ((1,2,3), (3,4,5), (8,9,12))
t2 = [(1,2,3), (3,4,5), (8,9,12)]
t3 = [(1,10,100), (2,20,200), (3,30,300), (4, 40,400)]
sorted_t1 = sorted(t1, key=lambda x: x[1])
t2.sort(key=lambda x:x[1])
check_t1 = (1,2,3) in t1
max_ele_in_t1 = [max(el)
                 for el in t1]

t3 = [(1,10,100), (2,20,200), (3,30,300), (4, 40,400)]
t3_enum = enumerate(t3)
t3_enum_filtered = [el
                    for index, el in t3_enum if el%2==0]

print(sorted_t1)
print(t2)
print(check_t1)
print(max_ele_in_t1)
print(t3_enum)


t3 = [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]
t3_enum = enumerate(t3, start=1)
filtered_t3 = [el for idx, el in t3_enum if idx%2==0]
print(filtered_t3)

filtered_t3 = list(filter(lambda x: x[0] % 2 == 0, t3_enum))
# Extract the tuples from the filtered result
filtered_t3_tuples = [el for _, el in filtered_t3]
print(filtered_t3_tuples)

# =================Filter =============================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter odd numbers
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(filtered_numbers)
# Output: [1, 3, 5, 7, 9]
#>>>>>>>>>
numbers = [-1, 2, -3, 4, -5, 6, 7, -8, 9, 10]

# Filter positive numbers
filtered_numbers = list(filter(lambda x: x > 0, numbers))
print(filtered_numbers)
# Output: [2, 4, 6, 7, 9, 10]
#>>>>>>>>>
words = ["apple", "", "banana", "cherry", "", "date"]

# Filter non-empty strings
filtered_words = list(filter(lambda x: len(x) > 0, words))
print(filtered_words)
# Output: ['apple', 'banana', 'cherry', 'date']

#>>>>>>>>>
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = range(1, 20)

# Filter prime numbers
filtered_primes = list(filter(is_prime, numbers))
print(filtered_primes)
# Output: [2, 3, 5, 7, 11, 13, 17, 19]
#>>>>>>>>>

import os

# List files in a directory
files = os.listdir("/path/to/directory")

# Filter files with a specific extension (e.g., .txt)
filtered_files = list(filter(lambda x: x.endswith(".txt"), files))
print(filtered_files)
# Output: ['file1.txt', 'file2.txt', ...]


# ===================PRime numbers and Filter ===========================

def prime_num_check(x):
    if x<2:
        return False
    for counter in range(2, int(x**0.5)+1):
        if x%counter == 0:
            return False
    else:
        return True

numbers_list = range(1,100)

filtered_prime = list(filter(prime_num_check, numbers_list))
print(filtered_prime)
# ================Using zip(*t) and reduce ===========================
from functools import reduce

# Define a tuple of tuples
t1 = ((2, 3, 4), (12, 13, 14), (22, 23, 24))

# Calculate the element-wise sum using reduce and lambda
#  >>> The zip(*t) is the critical components.
result = [reduce(lambda x, y: x + y, items) for items in zip(*t1)]

# Print the result
print(result) # Prints 36, 39, 42]

# ==================================================================
Reversing dict keys and value when multiple keys have same values.
d1 = {'a':2, 'b':3, 'c':4, 'd':2, 'e':3}
d2 = dict()

for key,value in d1.items():
    val_from_d2 = d2.get(value)
    if val_from_d2 is None:
        d2[value]= list(key)
    else:
        val_from_d2.append(key)
        # Note: Initially I tried, this -->  d2[value] = val_from_d2.append(key)
        # But its start filling None in the d2[value] as return value of val_from_d2.append(key) is None.

# Flipping keys to value using a list expression
d1 = {'a':2, 'b':3, 'c':4, 'd':2, 'e':3}
print(d1)
nd = {}
[nd[val].append(key) if val in nd.keys() else nd.setdefault(val, [key]) for key, val in d1.items() ]


# ==============Sort the dictionary by values ============================
# Define a dictionary
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
my_dict['mango'] = 15


# Sort the dictionary keys by values
sorted_keys = sorted(my_dict.keys(), key=lambda x: my_dict[x])

# Print the sorted keys
print(sorted_keys)

# Define an initial dictionary
initial_dict = {'apple': 5, 'banana': 2, 'cherry': 8}
# Create a dictionary to update with
update_dict = {'banana': 3, 'date': 4}
# Update the initial dictionary with the update_dict
initial_dict.update(update_dict)

keys = ['apple', 'banana', 'cherry']
default_value = 0
my_dict = dict.fromkeys(keys, default_value)

# ==========Filtering and adding to another dict =======================
my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
my_dict2 = {'a1': 5, 'a2': 2, 'a3': 8, 'a4': 3}
d3 = {my_dict.setdefault(key,val) for key, val in my_dict2.items() if val>4}
print(my_dict) # Prints {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3, 'a1': 5, 'a3': 8}

list = ['a1', 'a2', 'a3']
d1 = { ind:el for ind, el in enumerate(list, start=1)}
print(d1)
# ==================================================================
# 7.	Max Value in Nested Dictionary: Find the maximum value in a nested dictionary.
def find_max_nested_dict(nested_dict):
    # Initialize the maximum value as negative infinity
    max_value = float('-inf')

    # Recursively traverse the dictionary
    for value in nested_dict.values():
        if isinstance(value, dict):
            # If the value is a dictionary, recursively find the max value in it
            max_in_nested_dict = find_max_nested_dict(value)
            max_value = max(max_value, max_in_nested_dict)
        elif isinstance(value, (int, float)):
            # If the value is an integer or float, compare and update the max value
            max_value = max(max_value, value)

    return max_value

# Example nested dictionary
nested_dict = {
    'a': {
        'x': 10,
        'y': {
            'z': 30,
            'w': 20
        }
    },
    'b': {
        'p': 50,
        'q': 40
    },
    'c': 5
}

# Find the maximum value in the nested dictionary
max_value = find_max_nested_dict(nested_dict)
print("Maximum Value:", max_value)

# ==================================================================
list1 = ['a1', 'a2', 'a3', 'a4', 'a2', 'a1']
list2 = []
[list2.append(el) for el in list1 if el not in list2]
list3 = [list2.append(el) for el in list1 if el not in list2]
#Note the list comprehensions is not catched any variable.
print(list2)  # Prints unique values.
print(list3) # Prints [None, None, None, None] four times. Not six times.

# ==================================================================
list1 = ['a1', 'a2', 'a3', 'a4', 'a2', 'a1']
"".join(el) for el in list1 # wrong
s1 = "".join(list1)


# ==================================================================
from collections import  Counter
l1 = [2, 3, 4, 5, 6, 7,7,8,8,2]
c1 = Counter(l1)
print(c1.most_common(5)[2]) #Second Most common
c1.get(5) # Returns the counter of this element 5

# ==================================================================
Set Default sets if the key is missing,
if it already exists, simply return the values.not
get method returns None if the key doesnt exists, else we can pass a default value
dict1.get(key, value_if_doesnt_exists)
# =================Defautl Dict ========================
from collections import defaultdict

settings = defaultdict(lambda: 'default_value')
user_settings = {'color': 'blue', 'size': 'medium'}
text_color = settings['text_color']  # Returns 'default_value' for missing key

settings2 = defaultdict(22) # Gives error first argument must be callable or None
settings2 = defaultdict(lambda: 22) # some default value.
print(settings2['akeynot_there']) # Prints 22


settings3 = defaultdict('') # Error: first argument must be callable or None
settings3 = defaultdict(list) #Ok, The default value is an empty list.
settings3 = defaultdict(lambda: []) #OK, but the default value is a lambda function
settings3["SomeRandomKey"] # Returns an empty list.

settings3 = defaultdict(lambda: "abc") #OK, but the default value is a lambda function
settings3["SomeRandomKey"] # Prints abc.


#The good thing about the defautl dict is that we can directly add elements, no need to check.
# Without defaultdict (requires conditional check)
if key not in normal_dict:
    normal_dict[key] = []
normal_dict[key].append('value')

# With defaultdict (no need for conditional check)
defaultdict = defaultdict(list)
defaultdict[key].append('value')

Note: When we use "get" method it returns None if the key is missing and we can pass missing value
If we use the key directly dict1["key_dont_exists"] it returns a default value
We can direclty access/append depending on the default value of the dict.
# ==================================================================
# collections.UserDict is a dictionary-like class provided by the Python collections module that is
# designed to be subclassed to create custom dictionary-like objects.
# It is meant to simplify the creation of dictionary-like classes by inheriting from it rather
# than directly subclassing the built-in dict type. UserDict is especially useful when you
# want to create a dictionary with customized behavior or add additional methods to your dictionary-like objects.

#Here I overrided the getitems and setitems so any access of keys only print the message this message is overriden.
# Only list of keys are allowed to be added such as Alice, Bob etc..

from collections import UserDict

# Create a custom dictionary-like class for contact information
class ContactBook(UserDict):
    def add_contact(self, name, phone_number):
        # Add a new contact to the dictionary
        self[name] = phone_number

    def search_contact(self, name):
        # Search for a contact by name
        if name in self:
            return self[name]
        else:
            return f"{name} not found in contacts"

    def delete_contact(self, name):
        # Delete a contact by name
        if name in self:
            del self[name]
        else:
            return f"{name} not found in contacts"

    def __getitem__(self, item):
        print("Get Items is overridden...")
        #Because of this nothing is printed...when you try to access items..

    def __setitem__(self, key1, item):
        print("here in set item block...") # Any adding new key will pass this code..
        if key1 not in ['Acc1', 'Acc2', "Alice", "Bob", "Sri"]:
            print("You cant add items as this is not in the accepted list")


# Create an instance of the custom ContactBook
contacts = ContactBook()

# Add contacts
contacts.add_contact("Alice", "123-456-7890")
contacts.add_contact("Bob", "987-654-3210")
contacts.add_contact("Sri", "986-654-3210")

# Search for contacts
print(contacts.search_contact("Alice"))  # Output: 123-456-7890
print(contacts.search_contact("Eve"))    # Output: Eve not found in contacts

# Delete a contact
contacts.delete_contact("Bob")
contacts["hello2"] = ("hello world", "Flying..")
contacts["hello"] = "123-456-678"

# Verify deletion
print(contacts.search_contact("Bob"))     # Output: Bob not found in contacts

for key, val in contacts.items():
    print(f"{key}----->{val}")

print("stop here..")
# ===================User List===============================
from collections import UserList

# Create a custom list-like class by subclassing UserList
class MyList(UserList):
    def append_twice(self, value):
        # Add a value to the list twice
        # >>>>>>> Can also be self.append. The self.data is same self which is a list type.
        self.data.append(value) #Can also be self.append. The self.data is same self which is a list type.
        self.data.append(value)

    def remove_first(self, value):
        # Remove the first occurrence of a value from the list
        if value in self.data:
            # >>>>>>> Can also be self.append. The self.data is same self which is a list type.
            self.data.remove(value)

    def add_at_second_index(self, value):
        # Remove the first occurrence of a value from the list
        self.insert(2, value)

# Create an instance of the custom list-like class
my_list = MyList([1, 2, 3])

# Use custom methods to modify the list
my_list.append_twice(4)
my_list.append_twice(44)
my_list.append_twice(444)
my_list.remove_first(2)
my_list.add_at_second_index(111)
my_list.add_at_second_index(234)
my_list.add_at_second_index(456)

# Access and manipulate the list
print(my_list)  # Output: [1, 3, 4, 4]

# ================Named Tuples ==========================
# Note that many fundamental methods of dict are like (1)items, (2)keys (3)values
# (4) get (5)setdefault, (6)pop, (7)popitem (8)update
# These are very critical and defining methods of dict, but named_tuple is not dictionary.

#The namedtuple methods like
# (1) _fields, (2)_asdict, (3)_as_tuple (4)_replace(**kwargs)

from collections import namedtuple

# Define a namedtuple class named 'Person' with fields 'name' and 'age'
Person = namedtuple('Person', ['name', 'age'])

# Create instances of the 'Person' namedtuple
person1 = Person('Alice', 30)
person2 = Person('Bob', 25)

# Access fields using dot notation
print(person1.name)  # Output: 'Alice'
print(person1.age)   # Output: 30

# You can also access fields by index, just like in regular tuples
print(person2[0])    # Output: 'Bob'
print(person2[1])    # Output: 25

# Convert namedtuple to a dictionary
person_dict = person1._asdict()
print(person_dict)   # Output: {'name': 'Alice', 'age': 30}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])
# Access the _fields attribute to get field names
field_names = Person._fields
print(field_names)  # Output: ('name', 'age', 'city')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])
# Create an instance of Person
person = Person('Alice', 30, 'New York')
# Convert the namedtuple to an ordered dictionary
person_dict = person._asdict()
print(person_dict)  # Output: OrderedDict([('name', 'Alice'), ('age', 30), ('city', 'New York')])
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])
# Create an instance of Person
person = Person('Alice', 30, 'New York')
# Replace values using _replace
new_person = person._replace(age=35, city='Los Angeles')
print(new_person)  # Output: Person(name='Alice', age=35, city='Los Angeles')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])
# Create a list of values
values = ['Bob', 25, 'Chicago']
# Create a new instance of Person using _make
person = Person._make(values)
print(person)  # Output: Person(name='Bob', age=25, city='Chicago')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Define a namedtuple class
Person = namedtuple('Person', ['name', 'age', 'city'])
# Create an instance of Person
person = Person('Alice', 30, 'New York')
# Convert the namedtuple to a regular tuple
person_tuple = person._as_tuple()
print(person_tuple)  # Output: ('Alice', 30, 'New York')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# ==================Collections Summary ==================================
__all__ = ["ChainMap", "Counter", 	---> Dictionary Like/Related
"OrderedDict", "UserDict",  "defaultdict", ---> Dictionary
"UserList", "UserString",  ---> User defined List and String
"deque",  --> List related
"namedtuple"] ---> Tuple related
# ====================Itertools -- Chain ===================================
from itertools import chain

# Combine two lists into a single iterable
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
dict1 = {"a1":2, "a2":4}
nested_list = [[11,22,33], [55,66,77]]
combined = chain(list1, tuple1, dict1, nested_list)

# Print the combined elements
for value in combined:
    print(value)  # Output: 1, 2, 3, 4, 5, 6
# It prints --> 2 3 4 5 6 a1 a2 [11, 22, 33] [55, 66, 77]
# =======================Count, Cycle, Repeat ==============================
from itertools import count
# Create an iterator starting from 1 with a step of 2
counter = count(1, 3)
# Print the first 5 values
for _ in range(5):
    print(next(counter))  # Output: 1, 4, 7, 10, 13

from itertools import cycle

# Create a cycle of the elements in a list
colors = cycle(['red', 'green', 'blue'])
# Print the first 8 colors
for _ in range(8):
    print(next(colors))  # Output: 'red', 'green', 'blue', 'red', 'green', 'blue', 'red', 'green'

from itertools import repeat
# Create an iterator that repeats the value 42 five times
repeater = repeat(42, 5)
# Print the values
for value in repeater:
    print(value)  # Output: 42, 42, 42, 42, 42

# ==================Named Tuples and Sort using Lambda============================================
from collections import namedtuple

Person = namedtuple('Person', ['Id', 'Name', 'Salary'])
p1 = Person(10, 'n1', 100)
p2 = Person(20, 'n2', 200)
p3 = Person(30, 'n3', 300)

list1 = [p2, p1, p3]
print(list1)
list1.sort(key=lambda el: el.Id)
print(list1)

# ====================Cumulative Sum===========================
from functools import reduce

list1 = [10,20,30, 40, 50, 60, 70]
cum_sum = [sum(list1[:i]) for i in range(1, 6)]
cum_mul= [reduce(lambda x,y: x*y, list1[:i], 1) for i in range(1, 6)]

print(cum_mul)
# >> Lambda Syntax: lambda input_arg1, input_arg2: input_arg1+*/input_arg2,
# >> reduce (function, sequence, start_value)

# =================Coin change problem ==============================
from itertools import combinations, combinations_with_replacement

coins = [1, 2, 5, 10, 11]
target_sum = 12

def coin_change_combinations(coins, target_sum):
    list_matching = []
    types_denominations = len(coins)
    for i in range(1, types_denominations+1):
        combinations_i = combinations_with_replacement(coins, i)
        for tp1 in combinations_i:
            if sum(tp1) == target_sum:
                list_matching.append(tp1)
    return list_matching

list_matching = coin_change_combinations(coins, target_sum)
print(list_matching)
print("end here..")
# ===============combinations, combinations_with_replacement=================
from itertools import combinations, combinations_with_replacement

# Find all 2-element combinations from a list
letters = ['A', 'B', 'C']
combs = combinations(letters, 2) # combinations_with_replacement

# Print the combinations
for combo in combs:
    print(combo)  # Output: ('A', 'B'), ('A', 'C'), ('B', 'C')

# =================permutations=========================
from itertools import permutations

# Find all 2-element permutations from a list
letters = ['A', 'B', 'C']
perms = permutations(letters, 2)

# Print the permutations
for perm in perms:
    print(perm)  # Output: ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')


# =================GroupBy==================================
# Yes, itertools.groupby requires the elements to be sorted based on the key you want to group by.
# This is because groupby groups consecutive elements with the same key. If the elements are not sorted,
# it will not work as expected, and the groups may not be accurate.
from itertools import groupby
from collections import namedtuple

# Define a namedtuple class named 'Person' with fields 'name', 'age', and 'city'
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances of the 'Person' namedtuple
person1 = Person('Alice', 30, 'London')
person2 = Person('Bob', 25, 'Paris')
person3 = Person('Charlie', 35, 'London')
person4 = Person('Dennis', 40, 'Amsterdam')

# Create a sorted list of persons based on the 'city' field
persons_all = [person1, person2, person3, person4]
sorted_persons = sorted(persons_all, key=lambda p: p.city)

# Group persons by the same city
groups = groupby(sorted_persons, key=lambda p: p.city)

# Print the groups
for key, group in groups:
    print(f'City: {key}')
    for person in group:
        print(f'    {person.name}, {person.age} years old')

# Note that 'groups' is an iterator, so printing it directly won't show its content



# =======================GroupBy===========================
from itertools import groupby

# Group elements in a list based on the first letter
words = ['apple', 'banana', 'cherry', 'avocado', 'blueberry']

# >>>>>>> Note that GroupBy requires the words to be sorted by the same criteria as of they need to grouped.
sorted_words = sorted(words, key=lambda x:x[0])
groups = groupby(sorted_words, key=lambda x: x[0])

# Print the groups
for key, group in groups:
    print(key, list(group))
# ==================IsSlice ===============================
from itertools import islice

# Slice a range of elements from a list
numbers = range(1, 100)
sliced = islice(numbers, 2, 100, 5)
# isslice(iterable_list_tuple, start, end, jump_size)

# Print the sliced elements
for value in sliced:
    print(value)  # Output: 3, 8, 13, 18, 23,.....98

# ==================================================================
from itertools import tee

# Create two independent iterators from a list
numbers = [1, 2, 3, 4, 5]
iter1, iter2, *rest = tee(numbers, 5)

# Print values from both iterators
print(list(iter1))  # Output: [1, 2, 3, 4, 5]
print(list(iter2))  # Output: [1, 2, 3, 4, 5]

print(list(rest)) #The print is below.
# [<itertools._tee object at 0x00000203E1922680>, <itertools._tee object at 0x00000203E1923BC0>,
# <itertools._tee object at 0x00000203E1921B00>]

# ===================zip_longest==========================
from itertools import zip_longest

# Combine two lists of different lengths with a fill value
list1 = [1, 2, 3]
list2 = ['A', 'B']
zipped = zip_longest(list1, list2, fillvalue='X')

# Print the combined elements
for value in zipped:
    print(value)  # Output: (1, 'A'), (2, 'B'), (3, 'X')
# ==================================================================
def print_recursion(n):
    if n == 0:
        return
    sum_val = print_recursion(n - 1)
    print(n)
prints -----> 1,2,3,4,5,6
# ==================================================================
def print_recursion(n):
    print(n)
    if n == 0:
        return
    print_recursion(n - 1)

prints -----> 6,5,4,3,2,1
# Note after return is completed, the rest of the stack is continued from very first iteration.
# ==============================================================
def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    reverse(string[1:])
    print(temp, end='')

# Note: After the recursion any values stored before the recursion are reversed..
# =======================Char count =======================================
def count_char(str1):
    if str1 == "":
        return 0
    num_char = count_char(str1[1:]) + 1
    return num_char


# =======================Palindrome using recursion=======================================
def palindrome(str, str_len, i):
    if i > (str_len//2):
        return True
    return (str[i] == str[str_len-i]) and palindrome(str, str_len, i+1)


# Driver Code
if __name__ == "__main__":
    str1 = "ges p seg"
    str_len = len(list(str1))-1
    result = palindrome(str1, str_len=str_len, i=0)
    print(result)

# =======================Fibonacci printing in reverse order using recursion=======================================
# Printing Fibonacci numbers in a reverse order
def fibonacci_series(n, a, b):
    if n > 0:
        fibonacci_series(n-1, b, a+b)
    print(a)


if __name__ == "__main__":
    val = fibonacci_series(10, 0, 1)
    print(val)

# ===============Coin change repetitions allowed. ===================================
def count(coins, n, sum):
    # If sum is 0 then there is 1
    # solution (do not include any coin)
    if sum == 0:
        return 1

    # If sum is less than 0 then no
    # solution exists
    if sum < 0:
        return 0

    # If there are no coins and sum
    # is greater than 0, then no
    # solution exist
    if n <= 0:
        return 0

    # count is sum of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return count(coins, n - 1, sum) + count(coins, n, sum - coins[n - 1])


# Driver program to test above function
coins = [1, 2, 3]
n = len(coins)
print(count(coins, n, 5))


qsize = len(q.queue)
FrontToLast(q, qsize)
for i in range(qsize):
    print(q.queue[i])
# ===================== Sorting a Queue with Recursion ===============
# defining a class Queue
class Queue:

    def __init__(self):
        self.queue = []

    def append_at_last(self, item):
        self.queue.append(item)

    def remove_and_return_first_element(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peep_first_element(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return not (len(self.queue))


# Function to push element in last by popping from front until size becomes 0
def FrontToLast(q, qsize):
    # Base condition
    if qsize <= 0:
        return
    # pop front element and push  this last in a queue
    q.append_at_last(q.remove_and_return_first_element())

    # Recursive call for pushing element
    FrontToLast(q, qsize - 1)


# Function to push an element in the queue while maintaining the sorted order
def pushInQueue(q, temp, qsize):
    # Base condition
    if q.is_empty() or qsize == 0:
        q.append_at_last(temp)
        return

    # If current element is less than the element at the front
    elif q.peep_first_element() >= temp:

        # Call stack with front of queue
        q.append_at_last(temp)

        # Recursive call for inserting a front element of the queue to the last
        FrontToLast(q, qsize)

    else:

        # Push front element into last in a queue
        q_get = q.remove_and_return_first_element()
        q.append_at_last(q_get)

        # Recursive call for pushing element in a queue
        pushInQueue(q, temp, qsize - 1)

    # Function to sort the given


# queue using recursion
def sortQueue(q):
    # Return if queue is empty
    if q.is_empty():
        return
    # Get the front element which will  be stored in this variable  throughout the recursion stack
    temp = q.remove_and_return_first_element()
    # Recursive call
    sortQueue(q)
    # Push the current element into the queue according to the sorting order
    pushInQueue(q, temp, q.size())


# Driver code
qu = Queue()

# Data is inserted into Queue using put() Data is inserted at the end
qu.append_at_last(10)
qu.append_at_last(7)
qu.append_at_last(16)
qu.append_at_last(9)

qsize = len(qu.queue)
FrontToLast(qu, qsize)
for i in range(qsize):
    print(qu.queue[i])


qu.append_at_last(20)
# qu.put(5)

# Sort the queue
sortQueue(qu)

# Print the elements of the
# queue after sorting
while not qu.is_empty():
    print(qu.remove_and_return_first_element(), end=' ')

# This code is contributed by Sadik Ali
# ============= Reversing a Queue =============
from queue import Queue
def reverse_queue(q):
    if q.qsize() <= 0:
        return
    else:
        val = q.get()
        reverse_queue(q)
    q.put(val)
    return q

def print_queue(q: Queue):
    for i in range(q.qsize()):
        print(q.get())

if __name__ == "__main__":
    q = Queue()
    q.put(56)
    q.put(27)
    q.put(30)

    reverse_queue(q)
    print_queue(q)
# Note Queue can't be printed unless all items are popped.
# However it provides a method which creates a double ended queue and returns
# thats is q.queue()
# ===================== NCR using Recurison ===========
def ncr(n, r, numerator, denominator):
    if r == 0:
        return numerator / denominator
    numerator = numerator * n
    denominator = denominator * r
    val = ncr(n - 1, r - 1, numerator, denominator)
    return val


# Driver code
n, c = 5, 5
val2 = ncr(n, c, 1, 1)
print(val2)
# The above code will print NCR
# =========================================
# The below Code will give 2.5 instead of 10(10 is the correct answer)

def ncr(n, r, numerator, denominator):
    if r == 0:
        return
    numerator = numerator * n
    denominator = denominator * r
    ncr(n - 1, r - 1, numerator, denominator)
    return numerator / denominator


# Driver code
n, c = 5, 2
val = ncr(n, c, 1, 1)
print(val)

# This is because after the stack is popped the values of numerator = 5 and denominator = 2
# at the final stack reversion.
# ============= Permutations ======================
def permute(a, l, r):
    if l == r:
        print("".join(a))
    else:
        for i in range(l, r):
            a[i], a[l] = a[l], a[i]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

# Driver code
string = "ABC"
n = len(string)
a = list(string)

# Function call
permute(a, 0, n)
# ============== All Subsets for a Set =========================
def subsets_recursive(arr, subset, index):
    if index == len(arr):
        print(subset)
        return
    else:
        # Exclude the current element
        subsets_recursive(arr, subset, index + 1)
        # Include the current element
        subsets_recursive(arr, subset + [arr[index]], index + 1)

# Example usage
arr = [1, 2, 3]
subsets=[]
subsets_recursive(arr, subset=subsets, index=0)
# ===========Coin combinations ================

def coin_combinations(coins, n, sum):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    if n <= 0:
        return 0
    return coin_combinations(coins, n - 1, sum) + coin_combinations(coins, n, sum - coins[n - 1])


# Example usage
coins_data = [1,2,3]
n = len(coins_data)
print(coin_combinations(coins_data, n, 5))

# ===============  LOngest palindromic substring. =============
def longestPalindromic(strn1, i, j):
    if i > j:
        return 0
    if i == j:
        return 1
    if strn1[i] == strn1[j]:
        return 2 + longestPalindromic(strn1, i + 1, j - 1)
    else:
        return 0
    return max(longestPalindromic(strn1, i+1, j), longestPalindromic(strn1, i, j-1))


# def longest_palindromic_substr(strn2):
#     return max(longestPalindromic(strn2, 0, len(strn2)-1)

if __name__ == "__main__":
    str1 = "abac"
    print(longestPalindromic(list(str1), 0, len(str1)-1))

# /===========================
def generate_subsets(input_list):
    def generate_subsets_helper(current_index, current_subset):
        # If we have processed all elements in the input list
        if current_index == len(input_list):
            all_subsets.append(current_subset)
            return
        else:
            # Exclude the current element and explore subsets
            generate_subsets_helper(current_index + 1, current_subset)
            # Include the current element and explore subsets
            generate_subsets_helper(current_index + 1, current_subset + [input_list[current_index]])

    all_subsets = []
    generate_subsets_helper(0, [])
    return all_subsets


# Example usage
input_list = [1, 2, 3]
result_subsets = generate_subsets(input_list)
print(result_subsets)
# ================== Generate matching brackets =============
def generate_brackets(all_comb, current_set, o, c, n):
    if o == n and c == n:
        all_comb.append("".join(current_set))
        return
    if o < n:
        generate_brackets(all_comb, current_set + ["{"], o + 1, c, n)
    if c < o:
        generate_brackets(all_comb, current_set + ["}"], o, c + 1, n)

# Example usage
t = []
generate_brackets(t, [], 0, 0, 3)
print(t)
# ==============  Return Kth element without sorting  =========
from random import randint

def kthSmallest(arr_int, len_arr, k):
    pivot_element_index = randint(0, len_arr - 1)
    pivot_element = arr_int[pivot_element_index]
    left_array = [el for el in arr_int if el <= pivot_element]
    right_array = [el for el in arr_int if el > pivot_element]
    len_right_array = len(right_array)
    len_left_array = len(left_array)

    if len_left_array == k:
        # Note here actually answer is found and returned...
        return pivot_element
    elif len_left_array > k:
        #Note if there is no return statement below it returns None
        return kthSmallest(left_array, len(left_array), k)
    else:
        # Note if there is no return statement below it returns None
        return kthSmallest(right_array, len(right_array), k - len_left_array)


# Driver Code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 2
    print("K'th smallest element is",
          kthSmallest(arr, n, k))

# ================== Dutch flag sorting problem=======
from random import randint

def sort012(a, len_arr):
    lp = 0
    rp = len_arr - 1
    i = 0
    while i <= rp:
        if a[i] < a[lp]:
            a[i], a[lp] = a[lp], a[i]
            i = i - 1
        if a[lp] == 0:
            lp += 1
        if a[i] > a[rp]:
            a[i], a[rp] = a[rp], a[i]
            i = i - 1
        if a[rp] == 2:
            rp -= 1
        i = i + 1
    print(arr)

# Driver Code
if __name__ == '__main__':
    arr = [1,1,2,2]
    arr_size = len(arr)
    arr = sort012(arr, arr_size)
# ============== Generate passwords using all char in the array -========
def generatepwd(a, p, used):
    if len(p) == len(a):
        print(''.join(map(str, p)))  # Print the current permutation as a password
        return

    for i in range(len(a)):
        if not used[i]:
            p.append(a[i])    # Add an unused element
            used[i] = True    # Mark the element as used
            generatepwd(a, p, used)  # Recurse with the new state
            p.pop()           # Backtrack: remove the last element
            used[i] = False   # Unmark the element

a1 = ['a', 'b', 'c']  # Example with letters
generatepwd(a1, [], [False] * len(a1))
# ======= Print all possible permuations such that left side and right side have same number of One-s
# https://www.geeksforgeeks.org/all-possible-binary-numbers-of-length-n-with-equal-sum-in-both-halves/
from collections import Counter

def equalN(n, left="", right=""):
    rem = n - 2 * len(list(left))

    if n == 0:
        print("Can't print equal digit arrays.")
        return
    if rem == 1 or rem == 0:
        # print(left + "--" + right)
        with0 = left + "0" + right
        with1 = left + "1" + right

        # if Counter(list(left)).get('1', 0) > 0:
        if Counter(list(left)).get('1') == Counter(list(right)).get('1') and (Counter(list(left)).get('1', 0) > 0):
            # print("------------ Start Equal Sides ---------")
            print(with0, end="\n")
            print(with1, end="\n")
            # print("------------ End Equal Sides ---------")
        return

    # rem = rem // 2
    equalN(n, left + "0", right + "1")
    equalN(n, left + "1", right + "0")
    equalN(n, left + "1", right + "1")
    equalN(n, left + "0", right + "0")


# Driver Code
if __name__ == "__main__":
    n = 5  # n-bits
    equalN(5)
# =========== Print spaces between every possible combination in the letters ======\
# https://www.geeksforgeeks.org/combinations-string-digits/
def spacedLetters(a, sw, p):
    if p == len(a):
        print(sw)
        return

    if len(sw) == 0:
        sw = [a[0]]
    spacedLetters(a, sw + ["-"] + [a[p]], p + 1)

    if len(sw) == 0:
        sw = [a[0]]
    spacedLetters(a, sw + [a[p]], p + 1)


# Driver Code
if __name__ == "__main__":
    input = [1, 2, 3, 4]
    spacedLetters(input, [], 1)

# ================== count substrings with same first and last characters ==================
# https://www.geeksforgeeks.org/recursive-solution-count-substrings-first-last-characters/
from collections import deque


def subStrings(dq, n):
    if len(dq) == 0:
        return

    a = dq.copy()
    b = dq.copy()
    c = dq.copy()

    if len(a) > 0:
        a.popleft()
        subStrings(a, n - 1)

    if len(b) > 0:
        b.pop()
        subStrings(b, n - 1)

    if len(c) > 0:
        c.popleft()
        if len(c) > 0:
            c.pop()
        subStrings(c, n - 2)

    print(a)
    print(b)
    print(c)
    return


# Driver Code
if __name__ == "__main__":
    a = deque([1, 2, 3, 4, 5])
    subStrings(a, 5)
# ============ Insert elements in a stack at the right position in a sorted array ========
def insert_element_at_right_spot(s2, el):
    len_s = len(s2)
    if not s2:
        return s2.append(el)

    if s2[len_s - 1] > el:
        tp_el = s2.pop()
        insert_element_at_right_spot(s2, el)
        s2.append(tp_el)
    else:
        s2.append(el)
    return s2



def insert_element_at_right_spot(s2: List, el):
    len_s = len(s2)
    if not s2:
        return s2.append(el)

    if s2[len_s - 1] > el:
        tp_el = s2.pop()
        insert_element_at_right_spot(s2, el)
        s2.append(tp_el)
    else:
        s2.append(el)
    return s2

# ======= This continuation of the above code to sort an array using recursion ========
def stack_sort(s1, n, el1, op=None, inel=None):
    if not s1 and el1:
        return s1.append(el1)
    if not s1 and el1 is None:
        return
    if len(s1) > 0 and el1 is None:
        el1 = s1.pop()
    if op == "Pop":
        stack_sort(s1, n, None, "Pop")

    if len(s1) > 0 and el1 is not None:
        len_stack = len(s1)
        if s1[len_stack - 1] > el1:
            insert_element_at_right_spot(s1, el1)
        else:
            s1.append(el1)
    else:
        s1.append(el1)

    if n == len(s1):
        return s1


# Driver Code
if __name__ == "__main__":
    s3 = [4, 6, 0, 2, 1, -22, 234, 5423]
    new_st = stack_sort(s3, len(s3), None, op="Pop")
    # new_st = append_in_middle([4, 8, 9], 1)
    print(new_st)

# ============ The below code is reversing linked list using recursion. =========
# The trick is to return statement where we first catch the last node and repeatedly use
# it as "reversed_head"

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one node, return the head
        if head is None or head.next is None:
            return head

        # Recursively reverse the rest of the list
        # ========> This reverse head passes through each recursion stack cycle and
        # =======> saved to the last recursion cycle.
        reversed_head = self.reverseList(head.next)

        # Reverse the current node's pointer
        head.next.next = head
        head.next = None

        return reversed_head


# =====  This is using recursion to merge two lists.
def mergeTwoLists(l1, l2):
    if not l2:
        return l1
    if not l1:
        return l2

    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link the nodes to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Print the original linked list
current_node = node1
while current_node is not None:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")

# Reverse the linked list using the reverseList method
# Create nodes and form a linked list as shown in the previous answer

# Reverse the linked list using recursion
solution = Solution()
reversed_head = solution.reverseList(node1)

# Print the reversed linked list
current_node = reversed_head
while current_node is not None:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")
