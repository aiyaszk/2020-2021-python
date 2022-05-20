'''

A function that meets the specifications below.

t, tuple or list
Each element of t is either an int, a tuple, or a list
No tuple or list is empty
Returns the maximum int in t or (recursively) in an element of t

max_val((5, (1,2), [[1],[2]])) returns 5.

'''

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    
    emptyL=[]
    emptyL2=[]
    if t==[] or ():
      return emptyL
    else:
      for i in range(len(t)):
        if type(t[i])==int:
          emptyL2.append(t[i])      
        if type(t[i])==list or type(t[i])==tuple:
          for j in range(len(t[i])):
            emptyL.append(t[i][j])
            if type(t[i][j])==int:
              emptyL2.append(t[i][j])     
            if type(t[i][j])==list or type(t[i][j])==tuple:
              for k in range(len(t[i][j])):
                emptyL2.append(t[i][j][k])
                if type(t[i][j][k])==int:
                  emptyL2.append(t[i][j][k])
                if type(t[i][j][k])==list or type(t[i][j][k])==tuple:
                  for t in range(len(t[i][j][k])):   
                    emptyL2.append(t[i][j][k][t])  
                
    
    print(max(emptyL2))

max_val((5, (1,2), [[1],[2]]))
#max_val((5, (1,2), [[1],[9]]))