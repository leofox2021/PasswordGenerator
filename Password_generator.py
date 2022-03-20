import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

#Setting everything up
Form, Window = uic.loadUiType("password_generator.ui")

#Window and variables
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
button = form.pushButton
passwd_display = form.lineEdit
quantity = form.label_2
dial = form.dial
password_value = ''
dial_value = 0

dial.setRange(10, 20)
quantity.setText(f'{dial.value()}')

def displayDial():
    quantity.setText(f'{dial.value()}')

#Copy value from the dial
def returnValue():
    global dial_value
    dial_value = dial.value()
    return dial_value


#Generate a password
def passwordGeneration():
    global password_value
    password_value = ''
    for var in range(int(returnValue())):
        a = random.choice(range(48, 123))
        if a < 58 or a > 64 and a < 91 or a > 96:
            password_value += chr(a)


#Display a password_value
def onButtonClick():
    passwordGeneration()
    global password_value
    passwd_display.clear()
    passwd_display.setText(f'{password_value}')

#Connecting signals
dial.valueChanged.connect(displayDial)
button.clicked.connect(onButtonClick)

#App execution
window.show()
app.exec()
