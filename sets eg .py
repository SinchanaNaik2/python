sql={1,2,3,4,5}
python={1,6,7,8}
print(sql.union(python))
print(python.difference(sql))
print(sql.difference(python))
print(sql.intersection(python))
print(sql.intersection(python))
print(sql.symmetric_difference(python))