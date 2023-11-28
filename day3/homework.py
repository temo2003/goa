# my_name = "temo"

# if 10>5:
#     int("zzz")

# if "e" in my_name:
#     print("sheicavs t-s")
# my_name = "temo"
# my_surname = "solomnishvili"
# my_age = 19

# my_sentence = "aa {2} bb {0} cc {1}".format(my_name, my_surname, my_age)

# print(my_sentence)



#my_name = "temo"
# my_surname = "solomnishvili"
# my_age = 19
# my_santence = "me var {0}  {1}   {2} wlis ".format(my_name, my_surname, my_age)

# print(my_santence)

# if "z" in my_name:
#      print("sheicavs z-s")
# else: 
#      print( "ar sheicavdes z-s")

#input
#output

# my_name = input(" chemi saxelia temo ")

# print("chemi saxelia " + my_name)
# my_age = 19
# my_age += 7
#  print(my_age)
# my_age = input("enter your age: ")
# my_name = input("enter your name: ")
# my_surname = input("enter your surname: ")
# print("my name is {} my surname is {} my age is {}".format(my_name, my_surname, my_age,))

# new_age  = int(my_age) + 3
# print("after 3 years i am now {} years old".format(new_age))
# print(2+2)
# print("2" + 2)
# print("2" + "2" + "3")

# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))

# product = num1 * num2

# if product > 100:
#     print(product)
# else:
#     print("you lose")


# #6*3=18  20-18=2 %გვიბრუნებს ნაშთს

#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი 
#აქედან მხოლოდ კენტები შეიკრიბოს და დაპრინტოს ჯამი


num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

my_sum = 0

if num1 % 2 == 1: 
    my_sum += num1

if num2 % 2 == 1:
    my_sum += num2

if num3 % 2 == 1:
    my_sum += num3 

print("the sum of odd numbers i {}".format(my_sum))
