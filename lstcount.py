lst=[10,10,20]
for x in lst:
    print(x,'-->',lst.count(x))

print([lst.count(x) for x in lst])

#using sets to count the list [remove the duplicate value]
lst=[10,10,20]
for x in set(lst):
    print(x,'-->',lst.count(x))

print([lst.count(x) for x in set(lst)])




