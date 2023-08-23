s1 = {1,2,5,4,2}
s2 = {7,4,8,9}

s3 = s1.union(s2)
#s3 = s1.intersection(s2)

print(s3)  # =>{1, 2, 4, 5, 7, 8, 9}    # s1 and s2 are not changed

# s1.update(s2)
# print(s1)  # =>{1, 2, 4, 5, 7 , 8, 9}   #s1 will be updated(changed)


#   Symmetric_deffernce  : which value are same is not comming

print(s1.symmetric_difference(s2))   #here 4 is common in both the sets so its not comming

print(s1.difference(s2))   #those value in set A is not appearing in set B

print(s1.isdisjoint(s2))   #is intersection between set A and set B is null then it is True else it is False

print(s1.issuperset(s2))  #superset

print(s1.issubset(s2))  #subset

s1.add("het")
s1.remove("het")  # it is throwing an error
s1.discard("het")  # it is not throwing any errors

# del s1 delete set
#s1.clear()  # delete all elements

# s1.pop()  remove random one element




