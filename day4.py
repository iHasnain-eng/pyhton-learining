information={
    "1st order" : "pyhton",
    "2nd order": "learning",
    "3rd order" : "[2,4,5,6]",
     "age"  : "43",
     "tuples":("mango","bannnan"),
     "lists":[1,3,4,6],
     "value":"true"
}

# information["1st order"]="hasnain","kaif"
# information["2nd order"]="1200"
# print(information)
# numm_dict={}
# numm_dict["marks"]="50.43"
# print(numm_dict)


# student={
#     "name": "hamza madari",
#     "subjects": {
#         "phy": "10",
#         "maths":"2",
#         "chem":"00"
#     }
# }
# print(student)
# dictonary={
#     "name":"hasnain",
#     "marks":"94.76%",
#     "subject marks":{
#         "physics":"89",
#         "maths":"89",
#         "english":"90",
#         "biology":"70"
#     }
# }
# print(dictonary["subject marks"]["biology"])

# empty_dic={}
# empty_dic["word"]="alphabate"
# empty_dic["numbers"]="787878787878"
# print(type(empty_dic))

# student_info={
#     "name":"surya",
#     "age":"17",
#     "city":"kanpur"
# }
# print(student_info["city"])


# marks_access={
#     "maths":90,
#     "physics":89,
#     "chemestry":90
# }

# print(marks_access["maths"])

# student_practice={
#     "name":"Ali",
#     "age":17,
#     "city":"bhiwandi"
# }
# new_word={"percentage":90,}
# student_practice.update(new_word)
# print(student_practice)

















# print(pairs[0])
# key=list(student_practice.keys())
# print(key[1])
# value=list(student_practice.values())
# print(value[0])





#methods in dictionary 



#___________________________sets___________________


# nums= set()
# value=set()
# print(type(value))

#set muttable but element is immutible 



# nums= set()
# nums.add("ramakrishna ")
# nums.add((1,2,3))

# nums.add("KARIM BHAI ")
# # nums.remove((1,2,3))
# nums.pop()
# num(s.pop()     #random value pi ckig
# # nums.clear()
# # print(nums)
# num1={1,2,3}
# num2={3,4,5}
# print(num1.intersection(num2))
# print(num1)
# print(num2)




# marks of students 

marks={}

a=int(input("enter marks of phy:"))
marks.update({"phy": a})

b=int(input("enter marks of maths:"))
marks.update({"maths": b})

c=int(input("enter chem marks:"))
marks.update({"chem":c})

d=int(input("enter english marks:"))
marks.update({"english":d})

e=int(input("enter IT marks:"))
marks.update({"IT":e})

f=int(input("enter biology marks:"))
marks.update({"IT":f})


print(marks)
percentage=((a+b+c+d+e+f)/600)*100

print("your percentage is :",percentage)
print("your combined marks is here")


    