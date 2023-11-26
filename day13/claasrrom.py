# შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 40 სიმბოლოიანი, სადაც აუცილებლად 6 სიმბოლო იქნება !##%(#)^#, 25 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 9 სიმბოლო იქნება ციფრები 215346347347
# მაგ: !n8391k*
import random 
my_arr = []
chars = list("qwertyuiopasdfghjklzxcvbnm")
symbols = list("!@#$%^&*")
numbers = list("1234567890")
for i in range(9):
    random_num = random.choice(numbers)
    my_arr.append(random_num)
    numbers.remove(random_num)
    
for i in range(25):
    random_char = random.choice(chars)
    my_arr.append(random_char)
    chars.remove(random_char)
    
for i in range(6):
    random_symbol = random.choice(symbols)
    my_arr.append(random_symbol)
    symbols.remove(random_symbol)


print("the program chose these characters:" , my_arr)
final_password = ""
for i in range(len(my_arr)):
    current_char = random.choice(my_arr)
    final_password += current_char
    my_arr.remove(current_char) #რათა my_arr სიაში არსებული ყველა სიმბოლო ერთხელ გამოვიყენოთ
    
print("the final password is:", final_password)



#დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.
#რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 
#10 ქულა  tu arasworad-daakldes 5 qulaდა გადავალთ შემდეგზე(ოღონდ ეს ვეღარ 
#უპასუხებს იმ დღეს ნუ remove დაგჭირდებათ
import random
students = ["giorgi","rati","salome","anri","demetre"]
point = [5,10]
points = 0
for i in range(5):
    student = random.choice(students)
    print(student)
    answer = input("did the student answer correctly?: ")
    if answer == "yes":
        points += 10
        print(student ," has plus 10 points and the next student is: ")
        students.remove (student)
    elif answer == "no":
        points = points - 5
        print("the student has minus 5 points and the next student is: ")
    else:
        print("yes or no")
print("quiz is over and the students have overall points",points)