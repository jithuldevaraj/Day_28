import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")  # set window title
window.config(padx=150, pady=100, bg=YELLOW)  # Padding.

# window.minsize(width=500, height=300)  # Minimum size of a window `
canvas = tkinter.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)  # inside the window Create a Canvas(canvas object)
tomato_img = tkinter.PhotoImage(file="tomato.png")  # loads an image file into tkinter.Creates a tkinter PhotoImage object
canvas.create_image(100, 112, image=tomato_img)  # displays the image on the canvas at position (100, 112)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

time_label = tkinter.Label(window, text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
time_label.grid(row=0, column=1)

reset_button = tkinter.Button(text="start", activeforeground="red", activebackground=PINK, highlightthickness=0)
reset_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="reset", activeforeground="red", activebackground=PINK, highlightthickness=0)
reset_button.grid(row=2, column=2)

tick_label = tkinter.Label(window, text="✔", fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)



window.mainloop()
