from tkinter import *
import json
import random


class QuotesInterface:
    def __init__(self):
        self.background_color = "#f5d0d6"
        self.text_color = "#333333"

        self.window = Tk()
        self.window.title("The Office Quotes Generator")
        self.window.config(padx=50, pady=50, bg=self.background_color, highlightthickness=0)

        self.canvas = Canvas(width=300, height=414, bg=self.background_color, highlightthickness=0)
        self.background_img = PhotoImage(file="images/background.png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.canvas.grid(row=1, column=0, columnspan=3)
        self.quote_text = self.canvas.create_text(150, 190, text="Click on Dwight to generate a quote", width=250,
                                                  font=("Helvetica", 16, "bold"), fill=self.text_color)
        self.author_text = self.canvas.create_text(150, 320, text="", width=250, font=("Helvetica", 16, "italic"),
                                                   fill=self.text_color)

        self.dwight_icon = PhotoImage(file="images/dwight_icon.png")
        self.quotes_button = Button(image=self.dwight_icon, highlightthickness=0, command=self.display_quote)
        self.quotes_button.grid(column=1, row=3)

        self.window.mainloop()

    def display_quote(self):
        with open("quotes.json") as file:
            quotes = json.load(file)

        random_quote = random.choice(quotes)

        self.canvas.itemconfig(self.quote_text, text=random_quote["quote"])
        self.canvas.itemconfig(self.author_text, text=random_quote["name"])
