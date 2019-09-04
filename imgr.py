# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import base64
import json
import sys

import self as self
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import urllib, urllib.request, sys
import ssl
#这里输入自己获取的AK和SK
API_KEY ="EhygL9yAyYnBlF5jDZtanFYG"
SECRET_KEY ="IYpGuTXgRzMELaBHeGbnFSXy29OHWfrx"

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 492)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(89, 40, 181, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
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
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 90, 281, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 50, 241, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setStyleSheet("background-color: rgb(218, 255, 187);")
        # self.label_4.setStyleSheet("border-width:1px; border-style:solid;border-color:rgb(0,0,0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        # self.listView_2 = QtWidgets.QListView(self.verticalLayoutWidget)
        # self.listView_2.setStyleSheet("background-color: rgb(205, 210, 255);")
        # self.listView_2.setObjectName("listView_2")
        # self.verticalLayout.addWidget(self.listView_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(205, 255, 252);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 150, 271, 291))
        # self.label.setStyleSheet("background-color: rgb(247, 216, 255);")
        self.label.setStyleSheet("border-width:1px; border-style:solid;border-color:rgb(0,0,0);")
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像识别工具"))
        self.label_2.setText(_translate("Form", "选择类别"))
        self.comboBox.setItemText(0, _translate("Form", "银行卡"))
        self.comboBox.setItemText(1, _translate("Form", "植物"))
        self.comboBox.setItemText(2, _translate("Form", "动物"))
        self.comboBox.setItemText(3, _translate("Form", "通用票据"))
        self.comboBox.setItemText(4, _translate("Form", "营业执照"))
        self.comboBox.setItemText(5, _translate("Form", "身份证"))
        self.comboBox.setItemText(6, _translate("Form", "车牌号"))
        self.comboBox.setItemText(7, _translate("Form", "驾驶证"))
        self.comboBox.setItemText(8, _translate("Form", "行驶证"))
        self.comboBox.setItemText(9, _translate("Form", "车型"))
        self.comboBox.setItemText(10, _translate("Form", "Logo"))
        self.label_3.setText(_translate("Form", "选择将识别的图片"))
        self.pushButton.setText(_translate("Form", "选择"))
        self.pushButton_2.setText(_translate("Form", "复制到剪切板"))
        self.label.setText(_translate("Form", "显示图片"))
        self.pushButton.clicked.connect(self.openfile)

        self.pushButton_2.clicked.connect(self.copyText)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label_4.text())


    def openfile(self):
        self.download_path = QFileDialog.getOpenFileName(self.horizontalLayoutWidget_2,"选择要识别的图片","/","Image File(*.jpg *.png)")
        #判断是否选择了图片

        if not self.download_path[0].strip():
            pass  #未选择，无操作
        else:
            #已选择，显示图片路径
            self.lineEdit.setText(self.download_path[0])
            #解析图片

            pixmap =QPixmap(self.download_path[0])
            scarePixmap = pixmap.scaled(QSize(311,300),aspectRatioMode=Qt.KeepAspectRatio)

            self.label.setPixmap(scarePixmap)

            self.typeTp()


    def typeTp(self):
        #银行卡识别
        if self.comboBox.currentIndex()==0:
            #self.get_token()
            self.get_bankcard(self.get_token())
            pass
        #植物
        if self.comboBox.currentIndex() == 1:
            self.get_plant(self.get_token())
            pass
        #动物
        if self.comboBox.currentIndex() == 2:
            pass
        #...
        if self.comboBox.currentIndex() == 10:
            pass


    def get_token(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        if (content):
            print(content)
            self.access_token = json.loads(content)['access_token']
            return self.access_token

    def get_plant(self,access_token):
        '''
        植物识别
        '''
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
        # 二进制方式打开图片文件
        f = open(self.download_path[0], 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')

        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            print(content)
            plants = json.loads(content)
            strover = '识别结果：   \n'
            try:
                i=1
                for plant in plants['result']:
                    strover += '{} 植物名称： {} \n'.format(i,plant['name'])
                    i+=1
            except BaseException:
                strover += '解析错误'
            self.label_4.setText(strover)



    def get_bankcard(self,access_token):
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard?access_token=' + access_token
        f = open(self.download_path[0], 'rb')  # 二进制方式打开图文件
        img = base64.b64encode(f.read())
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request = urllib.request.Request(url, params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if (content):
            print(content)
            bankcard = json.loads(content)

            strover = '识别结果:\n'
            try:
                if bankcard['result']['bank_card_type'] == 0:
                    bank_card_type = '不能识别'
                elif bankcard['result']['bank_card_type'] == 1:
                    bank_card_type = '借记卡'
                elif bankcard['result']['bank_card_type'] == 2:
                    bank_card_type = '信用卡'

                strover += '卡号:   {}\n 银行:  {}\n 类型:  {}'.format(bankcard['result']['bank_card_number'],
                                                                 bankcard['result']['bank_name'], bank_card_type)

            except BaseException:
                strover += '解析错误'
            self.label_4.setText(strover)


if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow =QtWidgets.QMainWindow()
    #初始化窗体
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    #显示
    MainWindow.show()
    #退出
    sys.exit(app.exec_())