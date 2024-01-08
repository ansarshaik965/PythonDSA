x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
n=int(input("enter n:"))

"""for x in range(0,x+1):
    for y in range(0,y+1):
        for z in range(0,z+1):
            if(x+y+z)!=n:
                print([x,y,z])"""


list_1=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if(i+j+k)!=n]
print(list_1)