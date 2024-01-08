import array

arr=array.array('i',[]) #empty
print(arr)
#-----Adding Elements--------
for i in range(1,6):
    arr.append(i)
print(arr)

#-----Removing last Element------
arr.pop()
print(arr)

#-----Removing given indexed element-----
arr.pop(2)
print(arr)
