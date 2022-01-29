name = str([int(number) for number in input().split(', ')])
print(type(name))
print(set(name))
name2 = set(filter(str.isdigit, name))
print(name2)
print(len(name2))

