import json


some_data = '''
{
 "people":[
{
    "name":"Kyle",
    "email":"Kyle@gmail.com",
    "phone":"408-wew-werw",
    "employed":false}
,{AKIAVQK4DLTENKJWXXT6
    "name": "Henry",
    "email": "htruong@gmail.com",
    "phone": "605-wew-werw"}
]}
'''
print(some_data)
data = json.loads(some_data)
print(data)