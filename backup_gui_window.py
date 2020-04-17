from tkinter import * #Python library for gui
import time #library to display time.

window = Tk()
current_time_of_machine = ''
clock = Label(window, font=('times', 20, 'bold'), bg='green')
clock.pack(fill=BOTH, expand=1)

window.title("Alarm Application")

#Disabled since we can't use both label and time function at the same time.
#lbl_1_alarm = Label(window, text="Simple Alarm Mini Project..!!", font=("Arial Bold", 10))
#lbl_1_alarm.grid(column=5, row=5)

window.geometry('600x250') #Deciding the size of the application window

def timefunction():
    global current_time_of_machine #Getting current time from the pc
    updated_time = time.strftime('%H:%M:%S')  #strftime python function to convert time to different formats.
    #Writing cond to check if time has changed and if so, update the time.
    if updated_time != current_time_of_machine:
       current_time_of_machine = updated_time
       clock.config(text=updated_time)

       #calling function every 200ms to update time - Please don't reduce below this time since display won't be nice.
      # clock.after(200, timefunction)

timefunction()
window.mainloop()
