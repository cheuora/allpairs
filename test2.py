import itertools

input = ('Brand X', '2000')+('2000', 'Modem') + ('Modem', 45)

print(input)

kkk = set(input)
print(kkk)

l = list(itertools.combinations(kkk,2))
print(l)
