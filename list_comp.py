import list_op
#-----------list comprehension----------
         # Normal
list_1=[]
for i in range(1,10):
    list_1.append(i) 
print(list_1)

        # Comprehension

list_2=[i for i in range(1,6)] # One liner to create list
print(list_2)

list_odd=[i for i in range(1,10,2) ]
print(list_odd)