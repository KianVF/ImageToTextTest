from PIL import ImageTk, Image
from pytesseract import pytesseract
import urllib.request
from tkinter import Tk, Frame, Label


def img_to_text_path(img_path):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(img_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    return text


def img_to_text_url(img_url):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    urllib.request.urlretrieve(img_url, "testImg.png")
    img = Image.open("testImg.png")
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    return text


# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk

print(img_to_text_path("123.png"))


img = ImageTk.PhotoImage(Image.open("testImg.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()

win.mainloop()
