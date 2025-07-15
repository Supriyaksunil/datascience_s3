user_input = input("Enter a tuple of key-value pairs, e.g. (('a',1), ('b',2)): ")

tuple_data = eval(user_input)

result_dict = dict(tuple_data)

print("Converted dictionary:", result_dict)