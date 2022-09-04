from tkinter import *
def program():
    
    root2 = Tk()

    root2.title("Patient Recorder")
    root2.maxsize(600, 500)
    root2.minsize(600, 500)
    root2.geometry("600x500")


    heading = Label(root2, text="Add New Patient Detail", font="comicsense 30 bold")
    heading.grid(row=1, column=0)

    l1 = Label(root2, text="Full Name", font="comicsense 20 bold", fg="red")
    l2 = Label(root2, text="Father's Name", font="comicsense 20 bold", fg="red")
    l3 = Label(root2, text="Phone Number", font="comicsense 20 bold", fg="red")
    l4 = Label(root2, text="Address", font="comicsense 20 bold", fg="red")
    l5 = Label(root2, text="Problem", font="comicsense 20 bold", fg="red")



    name = StringVar()
    father_name = StringVar()
    phone_number = StringVar()
    address = StringVar()
    problem = StringVar()

    nameEntry = Entry(root2, textvariable=name)
    father_nameEntry = Entry(root2, textvariable=father_name)
    phone_NumberEntry = Entry(root2, textvariable=phone_number)
    addressEntry = Entry(root2, textvariable=address)
    problemEntry = Entry(root2, textvariable=problem)

    l1.grid(row=3, column=0)
    l2.grid(row=4, column=0)
    l3.grid(row=5, column=0)
    l4.grid(row=6, column=0)
    l5.grid(row=7, column=0)

    nameEntry.grid(row=3, column=1)
    father_nameEntry.grid(row=4, column=1)
    phone_NumberEntry.grid(row=5, column=1)
    addressEntry.grid(row=6, column=1)
    problemEntry.grid(row=7, column=1)

    def save_data():
        with open(f"{nameEntry.get().lower()}"+".txt", "a") as file:
            file.write(f"Name: {nameEntry.get()}")
            file.write(f"\nFather's Name: {father_nameEntry.get()}")
            file.write(f"\nPhone Number: {phone_NumberEntry.get()}")
            file.write(f"\nAddress: {addressEntry.get()}")
            file.write(f"\nProblem: {problemEntry.get()}")
            file.close()

    saveButton = Button(root2, text="Save", fg="white", bg="green", font="comicsense 15 bold", command=save_data)
    saveButton.grid(row=8)

    root2.mainloop()

run_new_patient = program()