import tkinter as tk
from tkinter import messagebox
import random

messages = [
    "Does worrying help you out at all?",
    "First priorities, then fun!",
    "Remember why you chose to learn Softwaredevelopment/IT!",
    "Stop doubting the choice, there's no way you will go back now!",
    "The way it is now, and will look in the future, is 1kX better than how it used to look like!",
    "Always make do with what you have and stop crying!"
    ]


def display_message():
    message = random.choice(messages)
    messagebox.showinfo("Motivational Message", message)

display_message()
