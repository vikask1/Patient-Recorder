from tkinter import *

def program():
    root1 = Tk()

    root1.title("Patient Recorder")
    root1.minsize(600, 400)
    root1.geometry("1200x1000")

    heading = Label(root1, text="Add New Patient Detail", font="comicsense 30 bold")
    heading.pack()

    l1 = Label(root1, text="Enter full name", fg="grey", font="comicsense 25 bold")
    l1.pack()

    name = StringVar()
    nameEntry  = Entry(root1, textvariable=name)
    nameEntry.pack()

    def search_data():
        try:
            with open(f"{nameEntry.get().lower()}"+".txt", "r") as file:
                data = file.read()
                global d1
                d1 = Label(root1, text=data, fg="black", font="comicsense 15 bold")
                d1.pack()
        except FileNotFoundError as e:
            global d2
            d2 = Label(root1, text="Patient Not Found", fg="black", font="comicsense 15 bold")
            d2.pack()


    b1 = Button(root1, text="Search", fg="white", bg="green", font="comicsense 15 bold", command=search_data)
    b1.pack()


    root1.mainloop()

run_search = program()