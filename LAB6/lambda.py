# Code cell 9
seq = ['data','salt' ,'dairy','cat', 'dog']
justD = list(filter(lambda x: x[0] == 'd', seq))

print(justD)

toUpper = list(map(lambda x: x.upper(), justD))
print(toUpper)