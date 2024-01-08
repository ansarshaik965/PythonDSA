list_of_fruits=['apple','kiwi','mango','banana','orange']
list_of_animals=['dog','cat','hen','goat','lion']
list_of_numbers=[1,2,2,3,5,7,45,2,5,7,8,45,800]
#-----List Operations----------

list_of_animals.append('Tiger')  # append() will append 'Tiger' at the end of list
print(list_of_numbers.count(2)) # count() gives the count of 2 in list
list_2=list_of_numbers.copy() # copy() will copy the list_of_numbers to list_2
list_of_fruits.extend(list_of_animals) # extend() Merges two lists
list_of_numbers.pop() # pop() removes last element of the list
list_of_fruits.clear() # it will clear all the elements from list
list_of_numbers.remove(1) # remove() removes given number 
list_of_numbers.insert(0,222) # insert(index,element) places element at your desired index
print(dir(list_2)) # dir(list) gives all the operations related do list

#-------slicing of List------------
list_of_players=['virat','rohit','hardik','shubham','jadeja']

print(list_of_players[0:5]) # Prints elemets from index 0 to index 4
print(list_of_players[::-1]) # Reverse of List
print((list_of_players[0][::-1]).split()) # Reversing string of list and making that as list