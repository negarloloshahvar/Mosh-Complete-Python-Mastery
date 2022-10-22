d = {1: '001', 2: '010', 3: '011'}
# get() Method returns the value for the given key
print(d.get(1))

d[4]= d.get(4, 0) + 1

print(d)