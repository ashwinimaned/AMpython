from collections import Counter 
test_dict={'dict1':{"1":"name1", "2":"name2", "3":"name3"},'dict2':{"1":50, "2":60, "3":70}}
print("The original dictionary : " + str(test_dict)) 
  
 
res = [] 
for key, val in test_dict.items(): 
    cnt = Counter(val) 
    res.append({key : cnt.most_common(1)[0]}) 
      
  
print("Maximum element key : " + str(res))
