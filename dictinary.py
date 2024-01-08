dict_1={} #Empty dict
print(type(dict_1)) #<class 'dict'>

my_dict={'name':'ansar',   #In dict Everything will be in Key and Value Pairs
        'place':'bengaluru', # Keys Can Not Be REPEATED 
        'number':'2170'}    # Keys Can Have same  Value

print(my_dict['name']) # Method 1 
print(my_dict.get('name')) # Method 2

#------Adding Elements----------
my_dict['hobby']='exercise'
print(my_dict)
#{'name': 'ansar', 'place': 'bengaluru', 'number': '2170', 'hobby': 'exercise'}
my_dict.update({'colour':'fair'})
print(my_dict)
#{'name': 'ansar', 'place': 'bengaluru', 'number': '2170', 'hobby': 'exercise', 'colour': 'fair'}
my_dict['name']='shaikansar'
print(my_dict)
#{'name': 'shaikansar', 'place': 'bengaluru', 'number': '2170', 'hobby': 'exercise', 'colour': 'fair'}
#---------------Delete Element---------------

my_dict.pop('colour')
print(my_dict)
#{'name': 'ansar', 'place': 'bengaluru', 'number': '2170', 'hobby': 'exercise'}

#----------Accessing Elements-------------

print(my_dict.keys())
#dict_keys(['name', 'place', 'number', 'hobby'])
print(my_dict.values())
#dict_values(['shaikansar', 'bengaluru', '2170', 'exercise'])
print(my_dict.items())
#dict_items([('name', 'shaikansar'), ('place', 'bengaluru'), ('number', '2170'), ('hobby', 'exercise')])

#-------------iteration--------------
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key,value in my_dict.items():
    print(key,value)