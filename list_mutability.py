# TASK:
#
#  1.  Create three dictionaries. Insert three items in each of these dictionaries.
#  2.  Then, create a new list -- call it l1 --  which contains all three of the above dictonaries as its elements.
#  3.  Create a copy of this list using l2 = l1[:]. Now change some value in one of the dictionaries. Do you think the values will change in l2 as well?
#  4.  Take a look at l2 to verify your reasoning. If l2 does change, use deepcopy to create yet another copy -- call it l3 -- so that changing the original dictionaries does not affect l3.

# 1

d1 = {"one":"1.1" ,"two":"1.2", "three":"1.3"}
d2 = {"one":"2.1" ,"two":"2.2", "three":"2.3"}
d3 = {"one":"3.1" ,"two":"3.2", "three":"3.3"}

print("d1 = {}".format(d1))
print("d2 = {}".format(d2))
print("d3 = {}".format(d3))

# 2

l1=[d1,d2,d3]

print("l1 = {}".format(l1))

# Deep copy for step 4

import copy
l3 = copy.deepcopy(l1)

# changes for step 3

l2 = l1[:]
d1["one"]="changed"

print("l1 = {}".format(l1))
print("l2 = {}".format(l2))
print("l3 = {}".format(l3))

# 4

