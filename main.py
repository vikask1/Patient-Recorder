from tkinter import *

root = Tk()

root.title("Patient Recorder")
root.minsize(600, 400)
root.geometry("1200x1000")

def open_search():
    import search
    search.run_search

def open_new_patient():
    import new_patient
    new_patient.run_new_patient
        

heading = Label(root, text="Patient Recorder", font="comicsense 40 bold")
heading.pack(pady=20)

l1 = Label(root, text="what do you want to do ?", font="comicsense 25 bold")
l1.pack()

b1 = Button(root, text="Search Patient", fg="white", bg="green", font="comicsense 23 bold", command=open_search)
b1.pack(pady=20)
b2 = Button(root, text="Add New Patient", fg="white", bg="green", font="comicsense 23 bold", command=open_new_patient)
b2.pack(pady=20)



root.mainloop()