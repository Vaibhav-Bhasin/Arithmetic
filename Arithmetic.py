student=input("Please Enter Your Name :: \n")
print("Questions:: \n")
import random
for questions in range(10):
  a= random.randint(0,5000)
  b= random.randint(0,5000)
  opt = computer=random.choice([ "-" , "+" , "*" , "/" ])
  print(a,opt,b)
  if opt=="+":
    ans=float(a+b)
  elif opt=="-":
    ans=float(a-b)
  elif opt=="*":
    ans=float(a*b)
  elif opt=="/":
    ans=float(a/b)  
