# #loops
# count=1
# while count<= 10 :
#     print("doctor")
#     count+= 1 #===iterator
    
# print(count)

#iterator 
# num=5
# while num<6:   #its not be created infinite loops
#     print(num)
#     num-=1
# print("end here")


# n=100
# while n>= 1:      #stopping condition 
#     print(n)
#     n-=1

#qs 2
# n=int(input("enter your number:"))
# i=1
# while i<=10:
#     print(i*17)
#     i+=1
# print("your table is here ")


#qs3
# nums = [1,4,9,16,25,36,49,64,81,100]
# founder=["royal","ironman","thor","batman"]
# idx=0
# while idx< len(founder):
#     print(founder[idx])
#     idx+=1






# while idx < len(nums):
#     print(nums[idx])
#     idx+= 1



#break
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1


# i=0
# while i<=10:
#     if(i%2 !=0):
#         i+=1
#         continue
#     print(i)
#     i+=1


#FOR LOOPS____________________________\
# vegitables=["tomato","potato","ginger","garlis"]
# for val in vegitables:
#     print(val)

# tuples=(1,2,3,4,5,6)
# for el in tuples:
#     print(el)


# str="thinkgreat"
# for char in str:
#     if(char=="g"):
#         print("g is found")
#         break
#     print(char)
# else:
#     print("end")



nums=[1,4,9,16,25,36,49,64,81,100,81]
x=81

idx=0
for el in nums:
    if(el==x):
        print("number found",idx)
        break
    idx+=1
 