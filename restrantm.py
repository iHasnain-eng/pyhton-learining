#resturant management system


menu={
    "Dal Bukhara":5000,
    "Panki Chatni":9000,
    "Filter Coffee":300,
    "Rogan Josh":1500,
    "tandoor-grilled":8000
}

#greet 
print("welcome to gareeb resturant")
print("Dal Bukhara :₹5000\n Panki Chatni :₹9000\n Filter Cofee :₹300\n Roghan Josh :₹1500\n tandoor-grilled:₹8000  ")

order_total=0

dish_1=input("Enter the name of dish you want to order:-")
if dish_1 in menu:
    order_total += menu[dish_1]
    print(f"your dish{dish_1} has been added to your order")

else:
    print(f"the orderd dish {dish_1}is not avaialble yet !")

second_time=input("do you want to add another item? (yes/no)")
if second_time=="yes":
    dish_2=input("Enter the name of second dish:-")
    if dish_2 in menu:
        order_total+=menu[dish_2]
        print(f"dish {dish_2}has been added to order")
    else:
        print(f"Orderd dish {dish_2}is not avaialble")
print(f"the total amount of dishes to pay is {order_total}")

print("__________________THANK YOU FOR ORDER_________________")