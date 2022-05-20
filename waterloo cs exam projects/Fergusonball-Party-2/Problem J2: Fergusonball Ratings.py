#https://cccgrader.com/getproblem.php?fid=783004&authcode=e4daaeda0d289e576618c54df4c62840

N=int(input()) 
b=0
for i in range(N):
  p=int(input())*5
  f=int(input())*-3

  if p+f>40:
    b+=1

if b==N:
 print(str(b)+"+")

else:
  print(b)