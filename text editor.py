
from PySide2.QtWidgets import *
from PySide2 import *
import speech_recognition as sr
from tkinter import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("text editor")
        global texts
        texts = QTextEdit(self)
        b = QPushButton("voice" , self)
        b.clicked.connect(self.voice)
        b.move(100,0)
        texts.move(0,100)
        texts.setGeometry(40,40,700,400)
        b1 = QPushButton("save",self)
        b1.clicked.connect(self.save)
        global mytext
        

        self.show()
    def voice(self):
        import speech_recognition as sr
        voice = sr.Recognizer()
        with sr.Microphone() as mic:
            voice.adjust_for_ambient_noise(mic)
            audio = voice.listen(mic)
            text = voice.recognize_google(audio)
            ef = str(text)
            texts.setText(ef)
    def save(self):
        def savea():
            savl = sa.get()
            mytext = texts.toPlainText()
            #text1 = str(mytext)
            #text2 = bytes(text1)
            with open(savl , "w") as f:

                f.write(texts.toPlainText())
        win = Tk()
        win.title("save file")
        sa = Entry(win)
        sa.pack()
        b3 = Button(win , text = "save" , command = savea)
        b3.pack()
        win.mainloop()

app = QApplication()
window = MainWindow()
window.show()
app.exec_()