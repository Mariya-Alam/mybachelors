from queue import PriorityQueue

t1 = (1,2,3)
print(t1[::-1])
t3 = (200,"a",[4,5],3.2)
print(t3)
t4 = t1+t3
print(t4)
for i in t4:
    #for y in i:
        print(i,end="")
print()

def func1(t):
    t=t*2
t = (1,2,3)
print(t)
func1(t)
print(t)