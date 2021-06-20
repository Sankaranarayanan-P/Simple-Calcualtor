from typing import Text
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon("E:\logo.ico"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(341, 455)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Seven_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("7"))
        self.Seven_Button.setGeometry(QtCore.QRect(10, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Seven_Button.setFont(font)
        self.Seven_Button.setObjectName("Seven_Button")
        self.Eight_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("8"))
        self.Eight_Button.setGeometry(QtCore.QRect(90, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Eight_Button.setFont(font)
        self.Eight_Button.setObjectName("Eight_Button")
        self.Nine_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("9"))
        self.Nine_Button.setGeometry(QtCore.QRect(170, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Nine_Button.setFont(font)
        self.Nine_Button.setObjectName("Nine_Button")
        self.Divide_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("/"))
        self.Divide_Button.setGeometry(QtCore.QRect(260, 90, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Divide_Button.setFont(font)
        self.Divide_Button.setObjectName("Divide_Button")
        self.Four_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("4"))
        self.Four_Button.setGeometry(QtCore.QRect(10, 230, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Four_Button.setFont(font)
        self.Four_Button.setObjectName("Four_Button")
        self.Six_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("6"))
        self.Six_Button.setGeometry(QtCore.QRect(170, 230, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Six_Button.setFont(font)
        self.Six_Button.setObjectName("Six_Button")
        self.Five_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("5"))
        self.Five_Button.setGeometry(QtCore.QRect(90, 230, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Five_Button.setFont(font)
        self.Five_Button.setObjectName("Five_Button")
        self.Multiple_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("*"))
        self.Multiple_Button.setGeometry(QtCore.QRect(260, 160, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Multiple_Button.setFont(font)
        self.Multiple_Button.setObjectName("Multiple_Button")
        self.Two_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("2"))
        self.Two_Button.setGeometry(QtCore.QRect(90, 300, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Two_Button.setFont(font)
        self.Two_Button.setObjectName("Two_Button")
        self.Minus_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("-"))
        self.Minus_Button.setGeometry(QtCore.QRect(260, 230, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Minus_Button.setFont(font)
        self.Minus_Button.setObjectName("Minus_Button")
        self.Three_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("3"))
        self.Three_Button.setGeometry(QtCore.QRect(170, 300, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Three_Button.setFont(font)
        self.Three_Button.setObjectName("Three_Button")
        self.One_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("1"))
        self.One_Button.setGeometry(QtCore.QRect(10, 300, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.One_Button.setFont(font)
        self.One_Button.setObjectName("One_Button")
        self.Dot_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("."))
        self.Dot_Button.setGeometry(QtCore.QRect(170, 370, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Dot_Button.setFont(font)
        self.Dot_Button.setObjectName("Dot_Button")
        self.Plus_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("+"))
        self.Plus_Button.setGeometry(QtCore.QRect(260, 300, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Plus_Button.setFont(font)
        self.Plus_Button.setObjectName("Plus_Button")
        self.Zero_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("0"))
        self.Zero_Button.setGeometry(QtCore.QRect(10, 370, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Zero_Button.setFont(font)
        self.Zero_Button.setObjectName("Zero_Button")
        self.Equalto_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("="))
        self.Equalto_Button.setGeometry(QtCore.QRect(260, 370, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Equalto_Button.setFont(font)
        self.Equalto_Button.setObjectName("Equalto_Button")
        self.Percentage_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("%"))
        self.Percentage_Button.setGeometry(QtCore.QRect(170, 90, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Percentage_Button.setFont(font)
        self.Percentage_Button.setObjectName("Percentage_Button")
        self.Clear_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("C"))
        self.Clear_button.setGeometry(QtCore.QRect(90, 90, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Clear_button.setFont(font)
        self.Clear_button.setObjectName("Clear_button")
        self.Clear_Entry_Button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.on_click("CE"))
        self.Clear_Entry_Button.setGeometry(QtCore.QRect(10, 90, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Clear_Entry_Button.setFont(font)
        self.Clear_Entry_Button.setObjectName("Clear_Entry_Button")
        self.Output_Box = QtWidgets.QLineEdit(self.centralwidget)
        self.Output_Box.setGeometry(QtCore.QRect(10, 12, 320, 61))
        self.Output_Box.setObjectName("Output_Box")
        textbox_font = QtGui.QFont()
        textbox_font.setFamily("Arial")
        textbox_font.setPointSize(30)
        textbox_font.setBold(False)
        textbox_font.setWeight(50)
        self.Output_Box.setFont(textbox_font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 341, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click(self, clicked):
        Error_font = QtGui.QFont()
        Error_font.setFamily("Arial")
        Error_font.setPointSize(20)
        Error_font.setBold(False)
        Error_font.setWeight(30)

        if clicked == "C":
            self.Output_Box.setText("0")
        else:
            #If Output Box Contain the Zero, Then this will delete it.
            if self.Output_Box.text() == "0" :
                self.Output_Box.setText("")

            #Concatenate the clicked value with what was there already.
            self.Output_Box.setText("{}{}".format(self.Output_Box.text(), clicked))
        try:
            if clicked == "=":  
                value  = self.Output_Box.text().replace("=", "")
                result = eval(value)
                self.Output_Box.setText(str(result))
                
        except ZeroDivisionError:
            self.Output_Box.setFont(Error_font)
            self.Output_Box.setText("Cannot Divide by Zero")
        except SyntaxError or TypeError:
            self.Output_Box.setFont(Error_font)
            self.Output_Box.setText("Invalid Input")
        except OverflowError:
            self.Output_Box.setText(Error_font)
            self.Output_Box.setText("Result is out of Range")
        except NameError:
            self.Output_Box.setText("0")


        if clicked == "CE":
            value = self.Output_Box.text().replace("CE", "")
            length = len(value)
            result = value.rstrip(value[length-1])
            self.Output_Box.setText(result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Calcualtor"))
        self.Seven_Button.setText(_translate("MainWindow", "7"))
        self.Eight_Button.setText(_translate("MainWindow", "8"))
        self.Nine_Button.setText(_translate("MainWindow", "9"))
        self.Divide_Button.setText(_translate("MainWindow", "/"))
        self.Four_Button.setText(_translate("MainWindow", "4"))
        self.Six_Button.setText(_translate("MainWindow", "6"))
        self.Five_Button.setText(_translate("MainWindow", "5"))
        self.Multiple_Button.setText(_translate("MainWindow", "X"))
        self.Two_Button.setText(_translate("MainWindow", "2"))
        self.Minus_Button.setText(_translate("MainWindow", "-"))
        self.Three_Button.setText(_translate("MainWindow", "3"))
        self.One_Button.setText(_translate("MainWindow", "1"))
        self.Dot_Button.setText(_translate("MainWindow", "."))
        self.Plus_Button.setText(_translate("MainWindow", "+"))
        self.Zero_Button.setText(_translate("MainWindow", "0"))
        self.Equalto_Button.setText(_translate("MainWindow", "="))
        self.Percentage_Button.setText(_translate("MainWindow", "%"))
        self.Clear_button.setText(_translate("MainWindow", "C"))
        self.Clear_Entry_Button.setText(_translate("MainWindow", "CE"))
        self.Output_Box.setText(_translate("MainWindow", "0"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





