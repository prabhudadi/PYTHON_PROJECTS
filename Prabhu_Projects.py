#1. CALCULATOR
print("="*20)
print("    1.CALCULATOR")
print("="*20)
num1=float(input("enter the 1st number:"))
num2=float(input("enter the 2nd number:"))
print("+,-,*,/,%,//,**")
choice=input("enter your choice of operation:")
def cal():
   

        
        
        if choice == "+":
          print(f"addition:{num1+num2}")
        elif choice == "-":
            print(f"substraction:{num1-num2}")
        elif choice == "*":
            print(f"multiplication:{num1*num2}")
        elif choice == "/":
            print(f"division:{num1/num2}")
        elif choice == "%":
            print(f"modulus:{num1%num2}")
        elif choice == "//":
            print(f"floor division:{num1//num2}")
        elif choice == "**":
            print(f"square:{num1**num2}")
        else:
            print("Invalid choice of operation")
   


cal()              



#2.PASSWORD GENERATOR
import random
print("="*30)
print("    2.PASSWORD GENERATOR")
print("="*30)
def password_generator():
   length=int(input("enter the password length:"))
   password= ""
   for i in range(length):
          password+=random.choice("abc123@#")
   print("password:",password)
  


password_generator()



#3.UNIT CONVERTER
print("="*30)
print("     3.UNIT CONVERTER")
print("="*30)
print("1.kilometers to meters\n"
           "2.meters to kilometers\n"
           "3.kilograms to grams\n"
           "4.grams to kilograms\n"
           "5.celcius to fohrenheit")
choice=int(input("enter your choice of converter:"))
value=int(input("enter the value to convert:"))
def unit_converter():

        if choice == 1:
            result=value*1000
            print(f"Result: {result:.02f}m")
        elif choice == 2:
            result=value/1000
            print(f"Result:{result:.0f}km")
        elif choice == 3:
            result=value*1000
            print(f"Result:{result:.0f}g")
        elif choice == 4:
            result=value/1000
            print(f"Result:{result:.0f}kg")
        elif choice == 5:
            result= (value*9/5)+32
            print(f"Result:{result}°k")
        else:
            print("invalid choice")



unit_converter()




#4.AGE CALCULATOR
print("="*30)
print("     4.AGE CALCULATOR")
print("="*30)
year=int(input("enter your birth year:"))
month=int(input("enter your birth month:"))
day=int(input("enter your bithday:"))
from datetime import date
def current_age():
    birth_date=date(year,month,day)
    today =date.today()
    age=today.year-birth_date.year
    if (today.month,today.day) < (birth_date.month,birth_date.day):
        age-=1
    else:
        print("Your age is:",age)


current_age()



#5.NUMBERS GUESSING GAME
print("="*30)
print("    5.NUMBERS GUESSING GAME")
print("="*30)
import random
print("CHOOSE A NUMBER :")
print("1,2,3,4,5,6,7,8,9,10")
num=int(input("enter the guessing number:"))
def guessing():
    computer=random.randint(1,10) 
    print(f"random number is :{computer}")
   
    if num==computer:
        print("you won the game !")
    elif num!=computer:
        print("you lost the game !")
    else:
        print("INVALID GUESSING NUMBER!")



guessing()




#6.ROCK PAPER SCISSOR GAME
import random
print("="*35)
print("   6.ROCK PAPER SCISSOR GAME ")
print("="*35)
print("YOUR TURN 😊")
print("ROCK","PAPER","SCISSOR ?")
txt=input("Pick your choice :").lower().casefold()
options=( "ROCK", "PAPER" , "SCISSOR" )
def game():
    computer=random.choice(options )
    print(f"MY TURN 😎:{computer}")

    if txt== "ROCK" and computer=="ROCK":
        print("ITS A TIE 🤝!")
    elif txt=="PAPER" and computer=="PAPER":
        print("ITS A TIE 🤝!")
    elif txt=="SCISSOR" and computer=="SCISSOR":
        print("ITS A TIE 🤝!")
    elif txt!=computer:
        print("YOU LOST THE GAME !")
    else:
        print("INVALID CHOICE!")


game()



#7.CURRENCY CONVERTER
print("="*30)
print("     7.CURRENCY CONVERTER")
print("="*30)
print(
      "1.INR → USD\n"	
      "2.INR → GBP\n"	
      "3.INR → EUR\n"	
      "4.INR → AED\n"
      "5.USD → INR\n"	
      "6.GBP → INR\n" )
choice=input("enter your choice of converter:")
amount=float(input("enter the amount:"))
def money():
    if choice=="1":
        result= amount / 87
        print(f"converted money:${result:.2f}")
    elif choice=="2":
        result= amount / 117
        print(f"converted money:£{result:.2f}")
    elif choice=="3":
        result= amount / 101
        print(f"converted money:€{result:.2f}")
    elif choice=="4":
        result= amount / 23.70
        print(f"converted money:AED{result:.2f}")
    elif choice=="5":
        result=amount * 87
        print(f"converted money:₹{result:.2f}")
    elif choice=="6":
        result=amount * 117
        print(f"converted money:₹{result:.2f}")
    else:
        print("INVALID CONVERTER")


money()




#8.BMI CALCULATOR
print("="*25)
print("   8.BMI CALCULATOR")
print("="*25)
weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in meters:"))
def bmi():
    body_mass_index=weight/pow(height,2)
    print(f"YOUR BMI RESULT:{body_mass_index:.2f}")
    if body_mass_index < 19:
        print("under weight")
    elif body_mass_index < 25:
        print("normal")
    elif body_mass_index < 30:
        print("over weight")
    else:
        print("obese")


bmi()
    
    

#9.TEMPERATURE CONVERTER
print("="*30)
print("   9.TEMPERATURE CONVERTER")
print("="*30)
print(
      "1.Celsius → Fahrenheit\n"
      "2.Fahrenheit → Celsius\n"	
      "3.Celsius → Kelvin\n"	
      "4.Kelvin → Celsius\n"	
      "5.Fahrenheit → Kelvin\n"	
      "6.Kelvin → Fahrenheit\n")
choice=input("Enter your choice of conversion:")
temp=float(input("Enter the value to convert:"))
def temperature():
    if choice=="1":
        result=(temp* 9/5)+32
        print(f"Result:{result:.2f} F")
    elif choice=="2":
        result=(temp - 32) * 5/9
        print(f"Result:{result:.2f} C")
    elif choice=="3":
        result=temp + 273.15
        print(f"Result:{result:.2f} K")
    elif choice=="4":
        result= temp - 273.15
        print(f"Result:{result:.2f} C")
    elif choice=="5":
        result= (temp - 32) * 5/9 + 273.15
        print(f"Result:{result:.2f} K")
    elif choice=="6":
        result=(temp - 273.15) * 9/5 + 32
        print(f"Result:{result:.2f} F")
    else:
        print("INVALID CHOICE")

temperature()        
        
        
        
#10.STOP WATCH
print("="*20)
print("   10.STOP WATCH")
print("="*20)
import time
input("press enter to start the stop watch:")
start_time=time.time()
input("press enter to stop the stop watch:")
end_time=time.time()
total_time=end_time-start_time
print(f"Your total time is:{total_time:.0f}seconds")





#11. SIMPLE AND COMPOUND INTREST CALCULATOR
print("="*40)
print(" SIMPLE AND COMPOUND INTREST CALCULATOR ")
print("="*40)
print("INTREST CALCULATOR:")
print(
      "1.simple intrest\n"
      "2.compond intrest\n")
choice=input("enter your choice:")
def intr():
    if choice=="1":
        print("====SIMPLE INTREST CALCULATOR====")
        principal=float(input("enter principal amount:"))
        rate=float(input("enter rate of intrest:"))
        time=float(input("enter time in years:"))
        intrest= (principal*rate*time)/100
        print(f"Your simple intrest:{intrest:.2f}")
    elif choice=="2":
        print("====COMPOUND INTREST CALCULATOR====")
        principal=float(input("enter principal amount:"))
        rate=float(input("enter rate of anual intrest:"))
        time=float(input("enter time in years:"))
        a = principal * (1 + rate/100) ** time
        intrest= a - principal
        print(f"Your compound intrest:{intrest:.2f}")
    else:
        print("INVALID CHOICE")


intr()



#12.ALARM CLOCK
print("="*25)
print("   12.ALARM CLOCK")
print("="*25)
import time
alarm=input("enter the alarm time(HH:MM):")
def clock():
    current_time=time.strftime("%H:%M")
    print(f"current time is:{current_time}")
    if alarm==current_time:
        print("ALARM RINGS")
    else:
        print("NO ALARM")

clock()





#13.DIGITAL CLOCK
print("="*25)
print("   13.DIGITAL CLOCK")
print("="*25)

import time

try:
    while True:
        current_time = time.strftime("%I:%M:%S %p")
        print(f"\rCurrent time is: {current_time}", end="", flush=True)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nClock stopped.")





#14.RANDOM QUOTE GENERATOR
print("="*30)
print("  14.RANDOM QUOTE GENERATOR")
print("="*30)

import random
print("RANDOM QUOTE GENERATOR:")
input("press enter to generate a quote:")
quote=[
       "Dream big, start small, act now.","Success begins where comfort ends.","Don't stop when you're tired; stop when you're done.","Small steps every day lead to big results.",
       "Your only limit is your mindset.","Work hard in silence; let success make the noise.","Discipline beats motivation.","Believe in yourself, even when nobody else does.",
       "Great things take time.","Every expert was once a beginner." ]

result=random.choice(quote)
print(f"your quote of the day is: {result}")





#15.QUIZ GAME
print("="*15)
print("  15.QUIZ GAME")
print("="*15)

print(" ARE YOU READY FOR QUIZ?:")
Q1=input("What is the capital of Japan?")
Q2=input("Which is the largest planet in our Solar System?")
Q3=int(input("How many bones are there in a typical adult human body?"))
Q4=input("Who wrote the Indian national anthem, Jana Gana Mana?")

def game():
    score=0
    if Q1.lower().casefold()=="Tokyo".lower().casefold():
        print("Q1 :Correct")
        score+=1
    else:
        print("Q1 :Wrong")
    if Q2.lower().casefold()=="Jupiter".lower().casefold(): 
         print("Q2 :Correct")
         score+=1
    else:
        print("Q2 :Wrong")
    if Q3==206:
        print("Q3 :Correct")
        score+=1
    else:
        print("Q3 :Wrong")
    if Q4.lower().casefold()=="Rabindranath Tagore".lower().casefold():
         print("Q4 :Correct")
         score+=1
    else:
        print("Q4 :Wrong answer")
    print(f"Your final score:{score}/4")
game()
        
        
        

#16.NOTE TAKING APP
print("="*20)
print(" 16.NOTE TAKING APP")
print("="*20)
def write_note():
    note=input("Enter your note:")
    f=open("notes.txt","a")
    f.write(note+ "\n")
    f.close()
    print("NOTE SAVED SUCCESSFULLY!")

def view_note():
    f=open("notes.txt","r")
    note=f.read()
    f.close()
    print("\n======YOUR NOTE======")
    print(note)

def note_app():
    print("\n======NOTE TAKING APP======")
    print(
          "1.Write a note\n"
          "2.View all the notes\n"
          "3.exit the note\n")
    choice=input("Enter yor choice:")

    if choice== "1":
        write_note()

    elif choice== "2":
        view_note()
    elif choice== "3":
        print("Thank you for using the NOTE TAKING APP")
    else:
        print("INVALID CHOICE")

note_app()
        
    


#17.QR CODE GENERATOR 
print("="*20)
print("17.QR CODE GENERATOR ")
print("="*20)
import qrcode
txt=input("enter the text or URL:")
image=qrcode.make(txt)
image.save("my_qr.png")
print("QR code created successfully!")





#18.STUDENT GRADE CALCULATOR  
print("=="*25)
print("            STUDENT GRADE CALCULATOR    ")
print("=="*25)
name=input("enter your name:")
maths=int(input("enter your maths marks:"))
english=int(input("enter your english marks:"))
science=int(input("enter your science marks:"))
hindi=int(input("enter your hindi marks:"))
total_marks=(maths+english+science+hindi)
outoff_marks=int(input("enter your outoff marks:"))
percentage=total_marks/outoff_marks*100
if percentage>=90 and percentage<=100:
    print("Grade:","A+")
elif percentage>=80 and percentage<=89:
    print("Grade:","A")
elif percentage>=70 and percentage<=79:
    print("Grade:","B")
elif percentage>=60 and percentage<=69:
    print("Grade:","C")
elif percentage>=50 and percentage<=59:
    print("Grade:","D")
elif percentage>=0 and percentage<=49:
    print("Grade:","FAIL")
else:
    print("invalid percentage")








# 19. EXPENSE TRACKER

expenses = []

print("=" * 25)
print("  19. EXPENSE TRACKER")
print("=" * 25)

print("1. Add Expense")
print("2. View Expenses")
print("3. Show Total Expenses")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))

    if amount <= 0:
        print("Enter an amount greater than zero.")
    else:
        expenses.append({
            "name": name,
            "amount": amount
        })
        print("Expense added successfully!")

elif choice == "2":
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\n----- YOUR EXPENSES -----")

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i}. {expense['name']} - "
                f"₹{expense['amount']:.2f}"
            )

elif choice == "3":
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: ₹{total:.2f}")

elif choice == "4":
    print("Thank you for using Expense Tracker!")

else:
    print("Invalid choice. Try again.")







# 20. PERSONAL BUDGET MANAGER

print("=" * 30)
print("   20.PERSONAL BUDGET MANAGER")
print("=" * 30)

budget = float(input("Enter your monthly budget: ₹"))
income = float(input("Enter your total income: ₹"))
expenses = []

print("\n1. Add Expense")
print("2. View Expenses")
print("3. Check Budget")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: ₹"))

    if amount <= 0:
        print("Enter an amount greater than zero.")
    else:
        expenses.append({
            "name": name,
            "amount": amount
        })
        print("Expense added successfully!")

elif choice == "2":
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\n----- EXPENSE DETAILS -----")

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i}. {expense['name']} - "
                f"₹{expense['amount']:.2f}"
            )

elif choice == "3":
    total_expenses = sum(
        expense["amount"] for expense in expenses
    )
    balance = budget - total_expenses

    print(f"Monthly Budget: ₹{budget:.2f}")
    print(f"Total Income: ₹{income:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Remaining Budget: ₹{balance:.2f}")

    if balance < 0:
        print("Warning: You have exceeded your budget!")
    else:
        print("You are within your budget.")

elif choice == "4":
    print("Thank you for using Personal Budget Manager!")

else:
    print("Invalid choice. Try again.")
    




    



    






        
        
        
        
    


        




           







