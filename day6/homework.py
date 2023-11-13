user1 = int(input("enter user1 score: "))
user2 = int(input("enter user2 score: "))
user3 = int(input("enter user3 score: "))
user4 = int(input("enter user4 score: "))
user_arithmetic_avarage = (user1 + user2 + user3 + user4) / 4
if user_arithmetic_avarage > 9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")    
elif user_arithmetic_avarage < 5:
    print("გილოცავ გაექეცი მატრიცას")
elif user_arithmetic_avarage in range(5,9):
    print("you are mid")
elif user_arithmetic_avarage > 10:
    print("there is something wrong with you ")
elif user_arithmetic_avarage < 0:
    print("there is something wrong with you")
else:
    print("me vvar temo")

# momxmarebeli1 = int(input("your salary is "))
# if momxmarebeli1 > 10000:
#     print("GOA-ში სწავლობდი?")
# elif momxmarebeli1 in range (1000,10000):
#     print("you mid")
# elif momxmarebeli1 < 1000:
#     print("შემოსულიყავი GOA-ში მატრიცელო")




