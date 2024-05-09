
# Import necessary modules
from random import *       #Importing random to select an option
from tkinter import *      # Importing tkinter for GUI
import tkinter.messagebox  # Importing messagebox for displaying messages

# Create the main window
root = Tk()
root.title("Decision Maker")  # Set the title of the window

# Function to get the number of choices from the user
def get_val():
    global opt_list
    opt_list = []  
    n = int(e.get())  # Get the number of choices from the entry field
    for i in range(n):
        Label(root, text=f"Choice {i + 1} is:").pack()  # Display label for each choice
        e1 = Entry(root, bg='white', fg='black')         # Create an entry field for each choice
        e1.pack()
        Button(root, text="Submit", command=lambda e1=e1: get_choice(e1)).pack()  # Button to submit each choice

# Function to append choices to the opt_list
def get_choice(entry):
    opt_list.append(entry.get())  

# Function to randomly choose and display one of the choices
def give_output():
    global opt_list  
    if opt_list:                                 
        ind = randint(0, len(opt_list) - 1)  # Generate a random index within the range of choices
        Label(root, text=f"The choice made is {opt_list[ind]}").pack()  # Display the chosen choice
    else:
        Label(root, text="No choice has been made yet").pack()  # Display message if no choices are available

# Function to handle exit button click event
def OnClick_exit():
    conv_Exit = tkinter.messagebox.askyesno("Decision Maker", "Do you want to exit ?")  # Display exit confirmation message
    if conv_Exit > 0:
        root.destroy()  # Close the application if user confirms

# Label and Entry field to get the number of choices from the user
Label(root, text="The number of choices :").pack()
e = Entry(root, font=('Ariel', 20, 'bold'), bg='white', fg='black', width=28, bd=30, justify=RIGHT)
e.pack()

# Button to submit the number of choices
Button(root, text="Submit", command=get_val).pack()

# Button to randomly choose and display a choice
Button(root, text="Get the choice", command=give_output).pack()

# Exit button
bt_exit = Button(root, text='      Exit      ', command=OnClick_exit, fg='#101820', bg='#FEE715',
                 font=('Ariel', 10, 'bold'))
bt_exit.pack()

# Start the main event loop
root.mainloop()
