#!/usr/bin/python

f1 = open("outl.out")
left = f1.readlines()
f2 = open("outr.out")
right = f2.readlines()
f3 = open("common.out", 'w')

new_list = list(set(left) & set(right))

for list_a in new_list:
    f3.write(list_a)



