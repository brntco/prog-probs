my_3list = list(range(0, 1000, 3))
my_5list = list(range(0, 1000, 5))
my_3list.extend(my_5list)
in3s = set(my_3list)
print(in3s)
print(sum(in3s))
