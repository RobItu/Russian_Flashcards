from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
current_card = None
# --------------------------- Reading from CSV --------------------- #

words_list = pandas.read_csv("data/russian_words.csv").to_dict(orient="records")

# -----------------------------Button Functions --------------------- #


def update_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    canvas.itemconfig(canvas_image, image=front_card_image)
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="black")
    flip_timer = window.after(3000, switch)


def switch():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_card_image)

# --------------------------- GUI --------------------------------------------------- #


window = Tk()
window.title("Russian Practice Cards 1")
window.config(background=BACKGROUND_COLOR, padx=40, pady=20)
window.minsize(width=900, height=700)

flip_timer = window.after(3000, switch)

front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 150, text="Russian", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


right_button = Button(image=right_image, highlightthickness=0, command=update_word)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=update_word)
wrong_button.grid(column=0, row=1)

update_word()

window.mainloop()
