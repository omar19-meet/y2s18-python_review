# Write your solution for 1.2 here!
# a=0
# for i in range(101):
#     if i%2==0: 
#         a=a+i
# print(a)        
for i in range(1000,0,-1):
    if i%6==2:
        if i**3%5==3:
            print(i)
            break