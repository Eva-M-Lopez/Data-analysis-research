from tkinter import *
root = Tk() 
root.geometry("300x200") 

  
# Dropdown menu options 
Age = [ 
    "18 to 64 years",
    "65 years and over",
    "Under 5 years",
    "5 to 17 years" 
] 

Origin = [ 
    "White alone",
    "Black or African American alone",
    "American Indian and Alaska Native alone",
    "Asian alone",
    "Native Hawaiian and Other Pacific Islander alone",
    "Some other race alone",
    "Two or more races",
    "Hispanic or Latino origin (of any race)",
    "White alone, not Hispanic or Latino" ,
] 

Education = [
    "Less than high school graduate",
    "High school graduate (includes equivalency)",
    "Some college, associate's degree",
    "Bachelor's degree or higher"
]
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Choose Me" ) 
  
# Create Dropdown menu 
dropA = OptionMenu( root , clicked , *Age ) 
dropO = OptionMenu( root , clicked , *Origin ) 
dropE = OptionMenu( root , clicked , *Education ) 
dropA.pack() 
dropO.pack()
dropE.pack()

#def Calculate_pov(age: int, origin: int, education: int):
    # Create a variable to store the display text
    # display = Tk.StringVar()
    # display.set("0")

    # # Create the calculator display screen
    # display_label = Tk.Label(root, textvariable=display, font=("Arial", 24), anchor="e", background="white")
    # display_label.place(x=200, y=150)


# btnq = Button(root, text = 'Quit', command = root.destroy)
# btnc = Button(root, text = 'Calculate', command = Calculate_pov)
 
# # Set the position of button to coordinate (100, 20)
# btnq.place(x=200, y=150)
# btnc.place(x=100,y=150)

root.mainloop() 