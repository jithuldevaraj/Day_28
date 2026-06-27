import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        time_label.config(text="Work",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    cout_min = math.floor(count / 60)
    cout_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{cout_min:02d}:{cout_sec:02d}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")  # set window title
window.config(padx=150, pady=100, bg=YELLOW)  # Padding.

# window.minsize(width=500, height=300)  # Minimum size of a window `
canvas = tkinter.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)  # inside the window Create a Canvas(canvas object)
tomato_img = tkinter.PhotoImage(file="tomato.png")  # loads an image file into tkinter.Creates a tkinter PhotoImage object
canvas.create_image(100, 112, image=tomato_img)  # displays the image on the canvas at position (100, 112)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Tkinter assigns it a unique ID. timer_text allows you to easily update or change the text later
canvas.grid(column=1, row=1)

time_label = tkinter.Label(window, text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
time_label.grid(row=0, column=1)

start_button = tkinter.Button(text="start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

tick_label = tkinter.Label(window, text="✔", fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)



window.mainloop()
