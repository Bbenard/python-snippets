import  json
data=[]
file =open("MOCK_DATA.json","r")
with file as  name:
	data1=json.load(name)
#data.append("first_name")
for k in data1:
	data.append(k.get("first_name"))
data.sort()
print data
