#!/usr/bin/python

f1 = open("outl_test.out")
left = f1.readlines()
f2 = open("outr_test.out")
right = f2.readlines()
#f3 = open("diff_test.out", 'w')


test_diff = list(set(right) - set(left))

for list_d in test_diff:
    print(list_d)
