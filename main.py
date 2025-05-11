
from tkinter import *
from math import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
LIGHT_BLUE = "#5BBCFF"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK= "✔"
TIMER_TEXT = (FONT_NAME,45,"bold")


reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    #stopping the window.after method
    window.after_cancel(timer)
    # reset the timer countdown
    canvas.itemconfig(timer_text,text ="00:00")
    #changing the label TIMER
    timer_label.config(text="TIMER" ,font = TIMER_TEXT , fg=LIGHT_BLUE ,bg=YELLOW)
    #changing the check label
    check_label.config(text ="")





# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_term_break_sec = SHORT_BREAK_MIN*60
    long_term_break_sec = LONG_BREAK_MIN*60


    # if it is 8th rep then,
    if reps == 8:
        count_down(long_term_break_sec)
        timer_label.config(text="long \nbreak" ,fg=RED)
        reps = 0

    #if it is 1st/3rd/5th/7th rep then,
    elif reps %2 ==1:
        count_down(work_sec)
        timer_label.config(text="work" , fg=GREEN)



    # if it is 2ns/4th/6th rep then,
    else:
        count_down(short_term_break_sec)
        timer_label.config(text="short \nbreak" ,fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    """00:00"""
    count_minutes = floor(count/60)
    count_seconds = (count%60)

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"


    canvas.itemconfig(timer_text, text =f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000,count_down , count-1)

    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx = 100, pady=50 ,bg=YELLOW)


tomato_img = PhotoImage(file ="tomato.png")

canvas = Canvas(width=200,height=224 , bg=YELLOW , highlightthickness=0)
canvas.create_image(100,112 , image = tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font =(FONT_NAME, 35, "bold"))
canvas.grid(column =1 , row=1)

# labels and two buttons plus check mark
timer_label = Label(text="TIMER" ,font = TIMER_TEXT , fg=LIGHT_BLUE ,bg=YELLOW)
timer_label.grid(column =1 ,row =0)

start_button = Button(text="start" , highlightbackground=YELLOW , command=start_timer )
start_button.grid(column = 0,row= 2)

restart_button = Button(text="stop",highlightbackground=YELLOW , command=reset)
restart_button.grid(column = 2 , row = 2 )

check_label = Label(fg=GREEN, bg= YELLOW)
check_label.grid(column = 1, row= 3)





window.mainloop()