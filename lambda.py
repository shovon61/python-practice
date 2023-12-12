
#for add
x = lambda a : a + 10
c = x ( 2 )
print("for adding result : " , c)

#for sub
v=lambda a,b,c,d:a-b-c-d
print("The sub result is : ",v(20,10,5,1))

#for multiple
y=lambda b,c :b*c
print( "for multiple result : ",y(5,4))

#for divide
z = lambda d,e,f:d/e/f
print("The divide result is : ",z(12,2,3))

#for lambda function
# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print("mydoubler output is : ",mydoubler(11))
print("mydoubler output is : ",mytripler(11))