#The alarm clock in Python3
import time
import tkinter as tk
#defining the function for displaying time.
def timefunction(time1=''):
    # get the current local time from the PC
    current_machine_time = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if current_machine_time != time1:
        time1 = current_machine_time
        clock.config(text=current_machine_time)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, timefunction)
window = tk.Tk()
clock = tk.Label(window, font=('courier', 20, 'bold'), bg='green')
clock.pack(fill='both', expand=1)
timefunction()
window.mainloop()

