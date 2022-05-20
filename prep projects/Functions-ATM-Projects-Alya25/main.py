#Application Title: Alya Bank's ATM Machine App
#Creator's Name: Alya Kurt
#App's Description: Here is the brand new ATM program with all these special time delays, input, and print statements designed just for you. First, the program will show you the login page, which will ask your passcode to move on to the menu. The menu will display 5 options that you could choose from. Do not forget that if you want to leave the program the only thing you should do is to enter quit.

import time

#I imported the time function in order to have time-delays for users.

print("Welcome to our Tech Company's new ATM Machine Program!")
time.sleep(2)
print("Our application's name is 'Alya Bank's ATM Machine App', it's given by the creator of the program Alya Kurt.")
time.sleep(3)
print("Our main focus is to make your experience as comfortable as possible. So, we made the most user-friendly program you can find! There are special time-delays, input and print statements just for you.")
time.sleep(5)
print("Now you will see the login page, which will ask your passcode to move on to the menu. In the menu, it will display 5 options that you could choose. Don't forget that if you want to leave the program you could enter quit. Hope you enjoy the program!")
time.sleep(6)

#A warm greeting and a quick description of the app, just to make the program more user-friendly I started with those print statements, and the time delays are to make it easier for the user to read.

balance=globals()['balance']=int(18527)

#Here I defined the global balance as demonstrated in the youtube video we watched. This will provide us the have one main balance in all the functions, which is a must-do in this program because the user has one general balance.

def deposit_cash():
	time.sleep(1)
	addition=int(input("Please enter the amount of many you want to deposit :"))
	globals()['balance']=addition+balance
	balance_inquiry()

#As mentioned in the rubric I created functions for each part, and here is the deposit cash one. It's at the top because the program needs to read it before the menu and passcode function. If it doesn't it will display an error message. It has a time delay to make it user-friendly. Then I added an input statement to explain to the user clearly what to do. Next, I used the global balance function, I did that because we are doing calculations on one main balance. Lastly, I directed the user to the balance inquiry function to see the change in the balance.

def withdraw_cash():
 
  time.sleep(1)
  withdraw=int(input("Please enter the amount you want to withdraw :"))
  
  if balance>=withdraw :
    globals()['balance']=balance-withdraw
    balance_inquiry()

  elif balance<withdraw :
    time.sleep(1)
    print("Error, there is not enough cash in the account.")
    balance_inquiry()

#Here is the withdraw cash function, the only differences from the deposit cash function are the if statements and error message. In this function, we should create an error message because if the user enters more than what she/he has then it will cause a problem. That why I made an if statement and wrote an error message. Either way, the user will be directed to see the total balance, to see the changes, or to know their total balance. 

def balance_inquiry():
  time.sleep(1)
  print("Your total balance is", balance)

  while (True) :
    time.sleep(1)
    continue_program=int(input("Enter 1 for menu and 2 for quit :"))

    if continue_program==1 :
      time.sleep(1)
      print("Menu will be displayed...")
      menu()

    elif continue_program==2 :
      program_quit()

    else :
      print("Please enter a valid option.")
      
#Here is the most popular function, balance inquiry. Almost all the other functions end up with this one because it will be easier for the user to see the total balance after making changes on it. This function's purpose is to show the total balance in the bank. Then it asks you to either quit or return to the menu, and if you make a typo and enter 3 because of the infinite while loop the program will ask the question again and will continue to work.

def pay_bill():
  time.sleep(1)
  print("Bill types will be displayed...")
  time.sleep(2)
  print("water")
  time.sleep(1)
  print("electricity")
  time.sleep(1)
  print("gas")
  time.sleep(1)
  print("phone")
  time.sleep(1)

  while (True) :
    time.sleep(1)
    bill=input("Please enter the type of bill you would like to pay :")
    time.sleep(1)

    if bill=="water" :
      water_bill=int(input("Please enter the amount of the water bill :"))
    
      if balance>=water_bill :
        globals()['balance']=balance-water_bill
        time.sleep(1)
        print("Your payment is successful.")
        balance_inquiry()

      elif balance<water_bill :
        time.sleep(1)
        print("Error, there is not enough cash in the account.")
        balance_inquiry()
    
  
    elif bill=="electricity":
      electricity_bill=int(input("Please enter the amount of electricity bill :"))
      
      if balance>=electricity_bill :
        globals()['balance']=balance-electricity_bill
        time.sleep(1)
        print("Your payment is successful.")
        balance_inquiry()

      elif balance<electricity_bill :
        time.sleep(1)
        print("Error, there is not enough cash in the account.")
        balance_inquiry()
  
    elif bill=="gas":
      gas_bill=int(input("Please enter the amount of the gas bill :"))
      
      if balance>=gas_bill :
        globals()['balance']=balance-gas_bill
        time.sleep(1)
        print("Your payment is successful.")
        balance_inquiry()

      elif balance<gas_bill :
        time.sleep(1)
        print("Error, there is not enough cash in the account.")
        balance_inquiry()
  
    elif bill=="phone":
      phone_bill=int(input("Please enter the amount of the gas bill :"))
    
      if balance>=phone_bill :
        globals()['balance']=balance-phone_bill
        time.sleep(1)
        print("Your payment is successful.")
        print(balance-phone_bill)

      elif balance<phone_bill :
        time.sleep(1)
        print("Error, there is not enough cash in the account.")
        balance_inquiry()
  
    else:
      time.sleep(1)
      print("Please enter a valid bill type.")

#Longest function in the program, but still it's user-friendly. There is an infinite while loop for your typos, lowercase letters to make it easier to write, and time delays for your comfort. This function will firstly display every bill type and then ask you to chose one and pay. Don't worry you don't have to go to the menu again, the program will direct you to balance inquiry and you will see your total balance even though you could have entered more than your cash.

def program_quit():
  time.sleep(1)
  print("Thank you for using Alya ATM's new program. See you next time :) ")
  time.sleep(1)
  quit()

#The simplest function, program quit. This function contains time-lapses for user friendliness and a thank you message as a print statement for the user.

def menu():
  time.sleep(2)
  print("deposit cash")
  time.sleep(1)
  print("withdraw cash")
  time.sleep(1)
  print("balance inquiry")
  time.sleep(1)
  print("pay bill")
  time.sleep(1)
  print("quit")
  time.sleep(1)

  while (True) :
    time.sleep(1)
    option=input("Please enter an option which is displayed above :")

    if option=="deposit cash" :
      deposit_cash()
  
    elif option=="withdraw cash" :
      withdraw_cash()

    elif option=="balance inquiry" :
      balance_inquiry()

    elif option=="pay bill" :
      pay_bill()

    elif option=="quit" :
      program_quit()

    else :
      time.sleep(1)
      print("Please enter a valid option.")

#A simple function to display the items/options in the menu. Don't worry, if you make a typo the program will continue to work and will ask the question again. Also for user-friendliness, it also includes time delays and lowercase letters to make it easier to write your option.

def passcode():
  time.sleep(1)
  passcode=input("Enter your 4 digit passcode :")

  counter=3
  while passcode!="1782" :
    counter=counter-1
    time.sleep(1)

    if counter==0 :
      print("Your account is blocked.")
      program_quit()
    
    elif counter==1 or counter==2:
      print("Your passcode is incorrect, you have", counter ,"tries left.")
      time.sleep(1)
      passcode=input("Enter your 4 digit passcode again :")

  time.sleep(1)
  print("Your passcode is correct, welcome to Alya Bank!")
  
  while (True) :
    time.sleep(1)
    continue_program=int(input("Enter 1 for menu and 2 for quit :"))

    if continue_program==1 :
      time.sleep(1)
      print("Menu will be displayed...")
      menu()

    elif continue_program==2 :
      program_quit()

    else :
      print("Please enter a valid option.")

#In the passcode function the user should enter their passcode and they only have 3 tries for safety reasons. If the user enters their passcode wrong for three times the program will be blocked which means it will automatically quit. To make this possible I added a counter variable and created a while loop to descend the counter by 1 in every turn. Like all of the functions above it also includes time delays for user-friendliness and as in the balance inquiry function it asks you to either quit or return to the menu, and if you make a typo it will still continue to work.

passcode()

#The functions don't work unless we call them, so here I wrote passcode() to make the login page work, because it is the first function to work we should write "passcode()" outside of any function.