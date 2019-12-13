# Grouping Anagrams 
# using defaultdict() + sorted() + values() 
from collections import defaultdict 
  
# initializing list 
test_list = [{'lump':1}, {'eat':2},  {'me':3},  {'tea':4}, {'em':5}, {'plum':6}] 
  
# printing original list 
print("The original list : " + str(test_list))  
# using defaultdict() + sorted() + values() 
# Grouping Anagrams 
temp = defaultdict(list) 
for ele in test_list: 
    for key in ele:
        temp[str(sorted(key))].append(ele) 
res = list(temp.values()) 
  
# print result 
print("The grouped Anagrams : " + str(res)) 

a = []
b = {1:'one'}
c = {2:'two'}
a.append(b)
a.append(c)
print(a)