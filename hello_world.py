##print("Hello world");

# if
# x= int(input("Please enter a number: "));
# if x< 0:
#     x=0;
#     print('X is less than zero');
# elif  x==0:
#     print('X is zero')
# elif x==1:
#     print('x = 1');
# else :
#     print('X is more')

 

# for n in range(2,10):
#     for x in range(2,n):
#         if n%x==0:
#             print(n,'is prime')
#             break

#     else :
#         print(n ,'is not prime')

# functions

# fibonacci
#def fin(n):
    #a=0
    #b=1
    #while a<n:
     #   print(a,end=' ')
      #  a=b
       # b=a+b
    #print()

#reading and writing files
#with open('test.txt','r') as reader:
    #process
#opening in read mode

with open('test.txt','r') as reader:
    for line in reader.readlines():
       print(line, end='')
#opening in write mode.

with open('test.txt','r') as reader:
    text=reader.readlines()
with open('test_write.txt','w') as writer:
    for bread in reversed(text):
        writer.write(bread)





