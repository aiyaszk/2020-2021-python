'''''
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

''''

h = list(s)

vowel = 0 

i=len(h)

for a in range(0,i):
  if h[a]=="a" or h[a]=="o" or h[a]=="u" or h[a]=="i" or h[a]=="e" :
    vowel+=1
  else:
    vowel+=0

print("Number of vowels:", vowel)


'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2

'''

h = list(s)
numBob = 0

x="bob"
y=list(x)

i=len(h)

for a in range(0,i-2):

  if h[a]=="b":
    if h[a+1]=="o":
      if h[a+2]=="b":
        numBob+=1
  else:
    numBob+=0

print("Number of bob:", numBob)
