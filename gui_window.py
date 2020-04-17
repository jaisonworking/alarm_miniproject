#The alarm clock in Python3
import time
import tkinter as tk
#defining the function for displaying time.
def timefunction(initial_time=''):
    # get the current local time from the PC
    current_machine_time = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if current_machine_time != initial_time:
        initial_time = current_machine_time
        clock.config(text=current_machine_time)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, timefunction)
window = tk.Tk()
clock = tk.Label(window, font=('courier', 20, 'bold'), bg='green')
clock.pack(fill='both', expand=1)
window.title("Alarms and Clock..!")
window.geometry('525x375')
timefunction()
window.mainloop()
