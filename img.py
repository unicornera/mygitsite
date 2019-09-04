# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 414)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 30, 211, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(27, 100, 331, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 331, 231))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgb(252, 233, 79);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 50, 160, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "选择识别类型："))
        self.comboBox.setItemText(0, _translate("Form", "银行卡"))
        self.comboBox.setItemText(1, _translate("Form", "动物"))
        self.comboBox.setItemText(2, _translate("Form", "植物"))
        self.comboBox.setItemText(3, _translate("Form", "通用票据"))
        self.comboBox.setItemText(4, _translate("Form", "营业执照"))
        self.comboBox.setItemText(5, _translate("Form", "身份证"))
        self.comboBox.setItemText(6, _translate("Form", "车牌号"))
        self.comboBox.setItemText(7, _translate("Form", "驾驶证"))
        self.comboBox.setItemText(8, _translate("Form", "行驶证"))
        self.comboBox.setItemText(9, _translate("Form", "车型"))
        self.comboBox.setItemText(10, _translate("Form", "Logo"))

        self.label_2.setText(_translate("Form", "选择要识别的图片"))
        self.pushButton.setText(_translate("Form", "选择"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "复制到剪切版"))
        self.pushButton.clicked.connect(self.openfile)

    def openfile(self):
        self.download_path = QFileDialog.getOpenFileName(self.horizontalLayoutWidget_2,"选择要识别的图片","/","Image File(*.jpg *.png)")

        if not self.download_path[0].strip():
            pass
        else :
            self.lineEdit.setText(self.download_path[0])
            pixmap = QPixmap(self.download_path[0])

            scarePixmap = pixmap.scaled(QSize(311,300),aspectRatiMode=Qt.KeepAspectRatio)
            self.label_3.setPixmap(scarePixmap)

            #self.typeTp()
    # def typeTp(self):
    #     #银行卡
    #     if self.comboBox.currentIndex()==0:
    #         get_bankcard(self.get_token())



    #def get_token(self):



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
