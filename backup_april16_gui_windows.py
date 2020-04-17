from tkinter import * #Python library for gui

window = Tk()

window.title("Alarm Application")

lbl_1_alarm = Label(window, text="Hope you are doing well...!!", font=("Arial Bold", 30))

lbl_1_alarm.grid(column=5, row=5)

window.geometry('600x250') #Deciding the size of the application window

window.mainloop()
