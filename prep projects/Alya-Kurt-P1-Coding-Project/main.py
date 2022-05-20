

import datetime
import time 
 
current_time = datetime.datetime.now()   
hour_now=int(current_time.hour) + 3
#adding three because of turkey's timeline
hour_now_minus3=int(current_time.hour)
minute_now=current_time.minute

if hour_now_minus3==22 :
  hour_and_minute=1 + minute_now/100 

if hour_now_minus3==23 :
  hour_and_minute=2 + minute_now/100 

if hour_now_minus3==24 :
  hour_and_minute=3 + minute_now/100 

else :
  hour_and_minute=hour_now + minute_now/100 

#because adding three wouldn't work on those times I manually changed them

print("Hi! Welcome to this mini program that will help you about the curfew limitations.")
print(" ")
print("The program will ask you your age until you enter 0. So please enter 0 when you want to quit.")
print(" ")
print("And before starting thank you for using our program.")
print(" ")
#greeting and thanking the user, explaining how the program works, will make the program more user friendly
time.sleep(10)
#user has to read many thing so a ten second break between them could be better for the user
age_number=int(input("Enter your age number so that we could tell if you can go out or not :"))
print(" ")
#the programs main goal is to tell you if you can go out or not and there are three different variables affecting the limitation towards you, your age, day and time, the program already can already calculate the time so we should ask the user about their age and day

while age_number!=0 : 
  #making a while loop to stop the program when entering zero
  day_name=input("Enter the day:")

  if day_name == "monday" or day_name == "tuesday" or day_name == "wednesday" or day_name == "thursday" or day_name == "friday":
    #there are two different types of curfew limitations in one week, weekend and weekdays, so I wrote two different conditions
    if age_number < 65 and age_number > 20:
      print("you can go out")
    elif age_number > 65:
      if hour_and_minute < 13 and 10 < hour_and_minute:
        print("you can go out")
      else:
        print("you cannot go out")
    elif age_number < 20:
      if hour_and_minute < 16 and 13 < hour_and_minute:
        print("you can go out")
      else:
        print("you cannot go out")
      
      #there are three different age groups so we should write one condition for each group

  elif day_name == "saturday" or day_name == "sunday":
    if age_number < 65 and age_number > 20:
      if hour_and_minute < 20 and 10 < hour_and_minute:
        print("you can go out")
    elif age_number > 65:
      print("you cannot go out")
    elif age_number < 20:
      print("you cannot go out")
   
    #I followed what all the time and age numbers are in the introductions and wrote the suitable ones for each
  age_number=int(input("Enter your age number so that we could tell if you can go out or not :")) 

#when the user enters zero the program finishes and prints a thanking and a fact

print("Again thank you for using this program. Stay safe. Here is a fact about covid 19: COVID-19 is a contagious disease that causes mild to severe respiratory symptoms with fever, cough, and shortness of breath.")

#thanking the user again and giving them a fact about covid 19 would make the program more user friendly

quit()
