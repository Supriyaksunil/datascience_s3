dict1 = dict(eval(input("Enter first dictionary as tuple pairs, e.g. (('a',1), ('b',2)): ")))

dict2 = dict(eval(input("Enter second dictionary as tuple pairs, e.g. (('b',3), ('c',4)): ")))

dict1.update(dict2)
# merged_dict = dict1 | dict2

print("Merged dictionary:", dict1)
# print("Merged dictionary:", merged_dict)
