import tkinter as tk
# First of all, to work with Tkinter we should import the program.

window=tk.Tk() 
# Then, we should import a window to create the graphical user interface.

calculate_label = None
error_label = None
# At the start of the program, I identified them as None to make the program work without the error and calculate labels. Later on, this statement will help me to write an if statement which is, "if they are not equal to None". After that, the program will clear them when the user presses the clear or another button.

# Starting Message
intro_frame=tk.Frame(master=window, width=30, bg="#FAA795")
intro_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
# To make my code look more organized and user-friendly I created a frame for the first three introduction labels. Also, I added a "expand True" to every frame, to make the program expandable.

label1=tk.Label(master=intro_frame, text="Welcome to Curfew Assistant", width=50, height=2, bg="#FAA795")
# Here is the first label for the intro, which is colored to have a more aesthetic look. Also, it makes the program more user-friendly because it greets the user.

label2=tk.Label(master=intro_frame, text="Please enter the data and click Calculate to see your results", width=50, height=2)
# Here is the second label for the intro, it also makes the program more user-friendly because it gives a brief introduction of the program.

line_label1=tk.Label(master=intro_frame, text="--------------------------------------------------------------------", bg="#FAA795")
# Then here is the third label for the intro, which only exists to make the graphical user interface more good looking.

label1.pack()
label2.pack()
line_label1.pack()
# Next, in order for labels to work, I wrote pack codes for each of them.

# Age Section
age_frame=tk.Frame(master=window, width=200, height=100)
age_frame.pack(fill=tk.BOTH, expand=True)
# To make my code look more organized and user-friendly I created a second frame for the "enter_age_label" label and "age_entry" entry widget.

enter_age_label=tk.Label(master=age_frame, text="Enter age:", height=2, width=25, bg="lightblue")
# Here is the label for the age frame, it is colored to have a more aesthetic look. Also, it makes the program more user-friendly because it gives instructions to the user.

age_entery_box=tk.Entry(master=age_frame, width=10)
# Here is the entry section for the user to input their age.

enter_age_label.pack()
age_entery_box.pack()
# Next, in order for the label and entry widget to work, I wrote pack codes for each of them.

# Day Section
day_frame=tk.Frame(master=window, width=200, height=100)
day_frame.pack(fill=tk.BOTH, expand=True)
# To make my code look more organized and user-friendly I created a third frame for the "select_day_label" label and "day_selection" option menu.

select_day_label=tk.Label(master=day_frame, text="Select the day:", height=2, width=25, bg="lightgreen")
# Here is the label for the day frame, it is colored to have a more aesthetic look. Also, it makes the program more user-friendly because it gives instructions to the user.

# Optionmenu for days
days=["Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday", "Sunday"]
# Here I wrote all the days of week because the user will be chosing one of them.
weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday"]
weekend=["Saturday", "Sunday"]
# Then I added two shortcuts to make the calculation process shorter and easier.
day_selection=tk.StringVar(master=day_frame)
day_selection.set(days[0]) 
dropdown=tk.OptionMenu(window,day_selection,*days)

select_day_label.pack()
dropdown.pack()
# Next, in order for the label and day option menu to work, I wrote pack codes for each of them.

# Time section
time_frame=tk.Frame(master=window, width=200, height=100)
time_frame.pack(fill=tk.BOTH, expand=True)
# To make my code look more organized and user-friendly I created a fourth frame for the "select_day_label" label and "day_selection" option menu.

select_time_label=tk.Label(master=time_frame, text="Select a time:", height=2, width=25, bg="lightyellow")
# Here is the label for the time frame, it is colored to have a more aesthetic look. Also, it makes the program more user-friendly because it gives instructions to the user.

# Optionmenu for times
day_time=["Morning", "Noon", "Evening", "Night"]
day_time_selection=tk.StringVar()
day_time_selection.set(day_time[0])
dropdown=tk.OptionMenu(window,day_time_selection,*day_time)

select_time_label.pack()
dropdown.pack()
# Next, in order for the label and day-time option menu to work, I wrote pack codes for each of them.

#results
result_frame=tk.Frame(master=window, height=20, bg="#FAA795")
result_frame.pack(fill=tk.BOTH, expand=True)
# To make my code look more organized and user-friendly I created a fifth frame for all the result labels.

label3=tk.Label(master=result_frame, text="Your result:", bg="#FAA795")
line_label2=tk.Label(master=result_frame, text="--------------------------------------------------------------------", bg="#FAA795")
# This label only exists to make the graphical user interface more good looking.

label3.pack()
line_label2.pack(side=tk.BOTTOM)
# Next, in order for labels to work, I wrote pack codes for each of them.

# Error statement if age is not written
def error():
  global error_label
  # "error_label" is used outside of this function so I stated it as global.
  error_label=tk.Label(master=result_frame, text="The age part can't be empty!", bg="#FAA795")
  # This layer will pop up if the user forgets to enter the age, it will display a simple warning message.
  error_label.pack()

#calculate
def calculate():
  global calculate_label
  # "calculate_label" is used outside of this function so I stated it as global.
  age_entery=age_entery_box.get()
  # To use the data that we collected from the age section we need to write ".get" code.
  
  if len(age_entery)==0:
    error()
    #This if statement is for when the user forgets to enter the age, it will send the user to the error function and then a simple message will be displayed.
  
  else:
    day_value=day_selection.get()
    # To use the data that we collected from the day section we need to write ".get" code.
    time_value=day_time_selection.get()
    # To use the data that we collected from the time section we need to write ".get" code.

    if day_value in weekend:
      result="You can't go out, there is a curfew on weekend."
    # In weekends there is a curfew for everyone at all times of the day, so nobody can go out.
    
    elif day_value in weekdays and time_value=="Night":
      result="You can't go out, there is a curfew at night times."
    # Like weekend days, every night there is a curfew for everybody too.
    
    elif day_value in weekdays and time_value=="Morning" and 18<int(age_entery)<65:
      result="You can go out, there isn't a curfew."
    # There isn't a curfew for adults on weekday's mornings.

    elif day_value in weekdays and time_value=="Noon" and int(age_entery)<18:
      result="You can go out, there isn't a curfew."
    # There isn't a curfew for children on weekday's noons.

    elif day_value in weekdays and time_value=="Noon" and 18<int(age_entery)<65:
      result="You can go out, there isn't a curfew."
    # There isn't a curfew for adults on weekday's noons too.

    elif day_value in weekdays and time_value=="Evening" and 18<int(age_entery)<65:
      result="You can go out, there isn't a curfew."
    # There isn't a curfew for adults on weekday's evenings too.

    elif day_value in weekdays and time_value=="Evening" and 65<int(age_entery):
      result="You can go out, there isn't a curfew."
    # There isn't a curfew for elders on weekday's evenings too.
    
    else:
      result="You can't go out, there is a curfew."
    # To write less if statements I just wrote the times every age group can go out, and here is the other times when they can't go outside.

    calculate_label=tk.Label(master=result_frame, text=result, bg="#FAA795")
    calculate_label.pack()
    # Here I determined the text as "result", and wrote different conditions for every result.

    if error_label != None: 
      error_label.pack_forget()
    #Here I wrote a code to erase the error label if one already exist, it was to make the program more user-friendly.

# Clear and another function
def clear_another():
  age_entery_box.delete(0, tk.END)
  day_selection.set(days[0])
  day_time_selection.set(day_time[0])
  # All of these clear commands reset the data so there isn't a error if they have been used or not. Unlike the calculate and error label, they both need to get deleted (not reseted) so there is a if statement for them.

  if calculate_label != None:
    calculate_label.pack_forget()
  #This part of the function is to delete the calculate layer if there is one before.

  if error_label != None: 
    error_label.pack_forget()
  #This part of the function is to delete the error layer if there is one before.

# Program quit
def program_quit():
  quit()
  # It will close the whole program.

#button section
button_frame=tk.Frame(master=window)
button_frame.pack(fill=tk.BOTH, expand=True)
# This is the last frame for all the buttons.

clear_button=tk.Button(master=button_frame, text="CLEAR", command=clear_another)
clear_button.pack(side=tk.LEFT)
# When the user clicks this button it'll use the "clear_another" function to reset all the data that was been written.

calculate_button=tk.Button(master=button_frame, text="CALCULATE", command=calculate)
calculate_button.pack(side=tk.LEFT)
# When the user clicks this button it'll use the "calculate" function to calcutale if the user can go out or not.

quit_button=tk.Button(master=button_frame, text="QUIT", command=program_quit)
quit_button.pack(side=tk.RIGHT)
# When the user clicks this button it'll use the "program_quit" function to close the program.

another_button=tk.Button(master=button_frame, text="ANOTHER", command=clear_another)
another_button.pack(side=tk.RIGHT)
# When the user clicks this button it'll use the "clear_another" function to reset all the data that was been written.

window.mainloop()
#Finally, to finish the code we should put everything in a mainloop.