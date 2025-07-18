
# 🌍 Language Translation Tool

A simple Python-based language translator GUI using `Tkinter` and `deep-translator`.


Features

- Translate text from one language to another.
- Supports major languages like English, Hindi, Kannada, etc.
- GUI interface using Tkinter.
- Copy translated text to clipboard.
- Optional Text-to-Speech functionality (via `gTTS` and `playsound`).


How It Works

1. Enter your text in the input box.
2. Specify the source and target languages (e.g., `english`, `hindi`, `kannada`).
3. Click "Translate" to see the translated text.
4. Use "Copy" or "Speak" to interact with the output.

---

 Screenshot

Below is a screenshot of the working tool:

![Screenshot](screenshot.png)


Run the Project

bash
pip install deep-translator gtts playsound pyperclip
python languagetranslator.py

 File Structure

language_translation_tool/
│
├── languagetranslator.py       # Main application
├── README.md                   # Project readme
└── screenshot.png              # UI screenshot

 License

Free to use and modify.
