import json
py_dic = {"name":"Anib","age":0}
json_dic = json.dumps(py_dic)
print(py_dic)
print(json.loads(json_dic))