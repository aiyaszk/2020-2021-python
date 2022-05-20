'''

Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

'''

def uniqueValues(aDict):
  '''
  aDict: a dictionary
  '''    
  a=aDict.keys()
  a=list(a)
  a1=list(a)
  a2=[]
  v=aDict.values()
  v=list(v)
  v1=list(v)

  for i in range(len(v)):
    if v.count(v[i])>1:
      v1.remove(v[i])
      a1.remove(a[i])
      
  for j in range(len(a1)):
    a2.append(min(a1))
    a1.remove(min(a1))
  print(a2)
  
uniqueValues({2: 2, 3: 3, 4: 4})
#uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0})