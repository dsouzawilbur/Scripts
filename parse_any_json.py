import json
 
# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
 
# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
 
print(employee_dict['name'])
