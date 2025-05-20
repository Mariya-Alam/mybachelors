# z= {5,6,7,8}
# y= {1,2,3,"foo",1,5}
# k = z & y #5
# j= z | y #all
# m = y-z #
# n = z-y
# p=z  #56789
# q= set(z) #8567
# z.add(9)
# z.remove
# print(z)

# odd = {x for x in range(1,15) if x % 2 != 0}
# print(odd)
#
# odd_2 = {x for x in range(1,15,2) if x % 2 != 0}
# print(odd_2)
#
# type(odd)

# list1 = [1,2,3,4,5]
# list2 = [6,7,3,4,5]
# common_elements = set(list1) & set (list2)
# print(common_elements)
# s1 = []
# for i in list2:
#     if i in list1:
#         s1.append(i)
# s1 = [i for i in list2 if i in list1]
# print(s1)

# z = lambda a,b,c : a-b-c
# print(z(5,3,2))

def myfunc(n):
    return lambda a:a*n
myfunc(9)(7)

s1 = {1,2,3,4,5}
l1 = (1,2,3,4,5)
d1 = [1,2,3,4,5]

zipped = zip(s1,l1,d1)

for a,b,c in zipped:
    print(a,b,c)

    
