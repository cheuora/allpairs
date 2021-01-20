import itertools

input = ('Brand Y', '2000') + ('Brand Y', 'Internal') + ('Brand Y', 56) 

print(input)

kkk = set(input)
print(kkk)

l = list(itertools.combinations(kkk,2))
print(l)
