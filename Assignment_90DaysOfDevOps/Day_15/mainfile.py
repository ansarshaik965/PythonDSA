import json
import yaml

json_file_name="service.json" #jason file : which is going to have thisdict as string"
yaml_file_name="service.yml"  # yaml file : which data is going to  retrieve in python file
yaml_to_json="y2j.json" # json file : whuch is going to have yaml file data in it

# Function for creating service.json file 
def python_dict_to_json(python_dict):
    with open(json_file_name,'w') as file:
       json.dump(python_dict, file)
       return "python_dict_to_json Successful"

# Function for Reading service.yml data
def yaml_to_python_dict(yaml_file_name):
    with open(yaml_file_name, 'r') as file:
      data=yaml.safe_load(file)
      return data

# function for converting service.yml to json file y2j.json
def yaml_to_json_(yaml_data):
    with open(yaml_to_json,'w') as file:
       json.dump(yaml_data, file)
       return "yaml_to_json Successful"
   
  

thisdict = {
    "services": {
      "aws": {
        "name": "EC2",
        "type": "pay per hour",
        "instances": 500,
        "count": 500
      },
      "azure": {
        "name": "VM",
        "type": "pay per hour",
        "instances": 500,
        "count": 500
      },
      "gcp": {
        "name": "Compute Engine",
        "type": "pay per hour",
        "instances": 500,
        "count": 500
      }
    }
  }


result_1=python_dict_to_json(thisdict)
print(result_1)

data=yaml_to_python_dict(yaml_file_name)
print(data['services']['aws'])

result_2=yaml_to_json_(data)
print(result_2)




    