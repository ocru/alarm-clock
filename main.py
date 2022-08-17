from tkinter import *
from datetime import datetime,timedelta
from playsound import playsound
import time
from threading import Thread
now = datetime.now()

tk=Tk()
tk.title("hello")
tk.geometry("600x400")

label = Label(tk,text = now.strftime("%H:%M:%S"),font=("Arial Italic",80))
label.pack()

set_alarm = Label(tk,text= "Set Alarm:",font=("Arial Italic",40))
set_alarm.place(x='0',y='100')

colon = Label(tk,text=":",font = ("Arial Italic",20))
colon.place(x='335',y='120')

hour_list = list(range(0,24))
minute_list = list(range(0,60))
hour_options = list(range(0,24))
minute_options = ["00","15","30","45"]

#Initialize alarm option, these hold value of dropdown menu
hours =  StringVar()
minutes = StringVar()
hours.set("0")
minutes.set("00")

hour_drop = OptionMenu(tk,hours,*hour_options)
hour_drop.place(x='280',y="125")

minute_drop = OptionMenu(tk,minutes,*minute_options)
minute_drop.place(x='350',y='125')

#gets current time and updates it per second

def update_time():
    global now
    global play_now
    now = datetime.now()
    label.configure(text=now.strftime("%H:%M:%S"))
    play_alarm(hours.get(),minutes.get())
    label.after(1000, update_time)



#for compairson with current time
def format_time(hour, minutes):
    str_hour = hour
    str_minutes = minutes

    if (int(hour) < 10):
        return "0{}:{}".format(str_hour, str_minutes)
    else:
        return "{}:{}".format(str_hour, str_minutes)

def play_alarm(hours,minutes):
    if(format_time(hours,minutes)==now.strftime("%H:%M")):
        alarm()

def alarm():

    play = Thread(target=playsound('C:\\Users\grade\Desktop\Downloads 2.0\mixkit-digital-clock-digital-alarm-buzzer-992.wav'))
    play.start()









update_time()

play_alarm(hours.get(),minutes.get())


tk.mainloop()
print(hours.get())
print(minutes.get())
print(format_time(hours.get(),minutes.get()))
print(now.strftime("%H:%M"))
print(now.strftime("%H:%M")==format_time(hours.get(),minutes.get()))


















