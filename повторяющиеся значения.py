name = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
name2 = list(set(name))
for i in range(len(name2)):
    print(name.count(name2[i]))
