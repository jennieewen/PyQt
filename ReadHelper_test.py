from ReadHelper import ReadHelper

importFile = "./json_test.txt"


rh = ReadHelper(importFile)

print(rh.content)
print(rh.path)
print(rh.name)
print(rh.key_list)
print(rh.get_value('dog'))
print(rh.get_picUrl('dog'))