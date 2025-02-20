# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(246, 255, 142);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Encender = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Encender.setGeometry(QtCore.QRect(110, 440, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_Encender.setFont(font)
        self.btn_Encender.setStyleSheet("background-color: rgb(101, 255, 78);\n"
"")
        self.btn_Encender.setObjectName("btn_Encender")
        self.btn_Apagar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Apagar.setGeometry(QtCore.QRect(520, 440, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_Apagar.setFont(font)
        self.btn_Apagar.setStyleSheet("background-color: rgb(255, 65, 65);")
        self.btn_Apagar.setObjectName("btn_Apagar")
        self.lb_Stream = QtWidgets.QLabel(self.centralwidget)
        self.lb_Stream.setGeometry(QtCore.QRect(150, 80, 481, 291))
        self.lb_Stream.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lb_Stream.setObjectName("lb_Stream")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 20, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Encender.setText(_translate("MainWindow", "Encender"))
        self.btn_Apagar.setText(_translate("MainWindow", "Apagar"))
        self.lb_Stream.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Video con PyQt5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
