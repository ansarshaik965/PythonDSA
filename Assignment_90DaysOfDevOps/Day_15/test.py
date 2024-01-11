import json

dictinory={
            "name":"ansar",
            "work":"devOps engineer"
           }

json_dict=json.dumps(dictinory)

print("JSON:",json_dict,"   ",type(json_dict))

my_dict=json.loads(json_dict)

print("PYTHON:",my_dict,"   ",type(my_dict))


      
