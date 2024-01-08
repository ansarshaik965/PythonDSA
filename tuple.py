test_tuple=1, #tuple is a sequence
print(type(test_tuple)) #<class 'tuple'>
test_tuple_1=(1,)
print(type(test_tuple_1)) #<class 'tuple'>

my_tuple=(1,2,3,4)
#my_tuple[1]=4
#TypeError: 'tuple' object does not support item assignment

print(my_tuple[0]) # my_tuple[1]=4

tuple_of_list=([1,2,3],90,4.5,'ansar')
tuple_of_list[0].append(22)
print(tuple_of_list)
#([1, 2, 3, 22], 90, 4.5, 'ansar')
#------- Slicing------------
print(tuple_of_list[0:3])
#([1, 2, 3, 22], 90, 4.5)