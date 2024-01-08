test_set=set() #Empty
print(type(test_set)) #<class 'set'>

set_of_fruits={'mango','apple','banana','orange','kiwi','mango','papaya'}
another_set_of_fruits={'pinapple','watermealon','lichi','apple','mango'}
print(set_of_fruits)# unordered & stores unique values
#{'orange', 'kiwi', 'apple', 'papaya', 'mango', 'banana'}
set_of_fruits.add('graphes')
print(set_of_fruits)
#{'banana', 'papaya', 'graphes', 'apple', 'orange', 'kiwi', 'mango'}
set_of_fruits.remove('banana')
print(set_of_fruits)
#{'mango', 'orange', 'papaya', 'apple', 'kiwi', 'graphes'}

#---------------Union-----------------
A={1,2,3,4,5,6} 
B={1,2,7,8} 
union_set3=A.union(B)
print(union_set3)
#{1, 2, 3, 4, 5, 6, 7, 8}

#---------------Intersection----------
A={1,2,3,4,5,6}
B={1,2,7,8}
intersection_set4=A.intersection(B)
print(intersection_set4)
#{1, 2}

#---------------Difference-----------
A={1,2,3,4,5,6}
B={1,2,7,8}
diff_set5=A.difference(B)
print(diff_set5)
#{3, 4, 5, 6}

#---------------Sub-set---------------
set_1={1,2,3,4,5,6,7} #Superset
set_2={1,2} #Subset
print(set_2.issubset(set_1)) # True
print(set_1.issubset(set_2)) # False