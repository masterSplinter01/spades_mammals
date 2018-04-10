#!/usr/bin/python

f1 = open("outl.txt")
left = f1.readlines()
f2 = open("outr.txt")
right = f2.readlines()
f3 = open("diff.txt")
diff = f3.readlines()

exclude = set(diff)

paired_left = [x for x in left if x not in exclude]

paired_right = [y for y in right if y not in exclude]

f4 = open("paired_outl.txt", 'w')
f5 = open("paired_outr.txt", 'w')

for list_l in paired_left:
    f4.write(list_l)

for list_r in paired_right:
    f5.write(list_r)

# Testing

test_exclude = set(paired_right)

test_diff = [z for z in paired_left if z not in test_exclude]

f6 = open("test_diff.txt", 'a')

for list_d in test_diff:
    f6.write(list_d)

test_exclude2 = set(paired_left)

test_diff2 = [k for k in paired_right if k not in test_exclude2]

for list_d in test_diff:
    f6.write(list_d)

