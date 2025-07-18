from tkinter import *
from deep_translator import GoogleTranslator
from gtts import gTTS
import playsound
import pyperclip

def translate_text():
    src = src_lang.get()
    tgt = tgt_lang.get()
    input_text = input_box.get("1.0", END).strip()

    if input_text:
        try:
            translated = GoogleTranslator(source=src, target=tgt).translate(input_text)
            output_box.delete("1.0", END)
            output_box.insert(END, translated)
        except Exception as e:
            output_box.delete("1.0", END)
            output_box.insert(END, f"Error: {str(e)}")

def copy_text():
    text = output_box.get("1.0", END).strip()
    pyperclip.copy(text)

def speak_text():
    text = output_box.get("1.0", END).strip()
    if text:
        tts = gTTS(text)
        tts.save("output.mp3")
        playsound.playsound("output.mp3")

# GUI Setup
root = Tk()
root.title("Language Translation Tool")
root.geometry("500x500")

Label(root, text="Enter Text:").pack()
input_box = Text(root, height=5, width=50)
input_box.pack()

Label(root, text="From Language (e.g. 'english')").pack()
src_lang = Entry(root)
src_lang.insert(0, "english")
src_lang.pack()

Label(root, text="To Language (e.g. 'hindi')").pack()
tgt_lang = Entry(root)
tgt_lang.insert(0, "hindi")
tgt_lang.pack()

Button(root, text="Translate", command=translate_text).pack(pady=10)
Label(root, text="Translated Text:").pack()
output_box = Text(root, height=5, width=50)
output_box.pack()

Button(root, text="Copy", command=copy_text).pack(side=LEFT, padx=10, pady=10)
Button(root, text="Speak", command=speak_text).pack(side=RIGHT, padx=10, pady=10)

root.mainloop()

