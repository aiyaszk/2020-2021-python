#https://cccgrader.com/getproblem.php?fid=783022&authcode=ec97f66cf59fe9acb64db5d743997cce

n=input()
a=0
b="0123456789"
k=0
for i in range(len(n)):
  if n[i]=="+":
    c=n[i+1]
    for j in range(len(b)):
      if n[i+2]==b[j]:
        k=n[i+2]
        a=i+3
    print((n[:i]), "tighten", c*10+k)
    if k==0:
      print((n[a:i]), "tighten", c)
    a=i+2
  elif n[i]=="-":
    c=n[i+1]
    print((n[a:i]), "loosen", c)
    a=i+2
  elif a!=0:
    if n[i]=="+":
      c=n[i+1]
      print((n[a:i]), "tighten", c)
