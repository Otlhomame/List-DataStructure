# List items are enclosed in square brackets
# Lists are ordered
# Lists are mutable
# List elements do not need to be unique.
# Elements can be of different data types.

'''
Creating Lists
'''
# list= [1, 'hello', 5.7]
# print(list)

'''
List Indexing
'''
# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# print(fruits[0])

# fruits= ['orange', 'apple', ['pear', 'apple', 'banana']]
# print(fruits[2][0])


'''
How to Slice Lists in Python
'''
fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# print(fruits[:])
# print(fruits[2:5])
# print(fruits[::4])
# print(fruits[::-2])

'''
Add Elements To a List
'''

# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# # fruits[0]='Berries'
# # print(fruits)

# # fruits[1:4]= ['Mandarins', 'Peaches', 'Plums']
# # print(fruits)

# fruits.append('limes')
# print(fruits)

'''
Remove or Delete List Items
'''
# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# del fruits[0]
# print(fruits)
# del fruits[1:5]
# print(fruits)
# del fruits
# print(fruits)

'''
Python List Methods
'''
# print(dir(list))
# print(help(list.insert))
# print(dir(set))

# ==============
# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# # fruits.append('Cashew')
# print(fruits)

# ==============
# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# fruits.insert(0,'Guava')
# print(fruits)

# =============
# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# fruits.clear()
# print(fruits)

# =============
# fruits= ['orange', 'apple', 'pear', 'apple', 'banana']
# # fruits.pop(-1)
# pos= (fruits.index('apple'))
# fruits.pop(pos)
# print(fruits)

#==============
# fruits= ['orange', 'apple', 'banana','banana', 'pear', 'apple', 'banana']

# print(fruits.count('banana'))

# result={}
# for x in fruits:
#    result[x]=fruits.count(x)
# print(result)

# from collections import Counter

# print(Counter(fruits))

"""
List Membership Test
"""

fruits= ['orange', 'apple', 'banana','banana', 'pear', 'apple', 'banana']

print('apple' not in fruits)
