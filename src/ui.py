# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(832, 499)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 180, 331, 231))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.xinfang = QtWidgets.QLabel(self.groupBox_2)
        self.xinfang.setGeometry(QtCore.QRect(30, 50, 291, 171))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xinfang.setFont(font)
        self.xinfang.setAutoFillBackground(False)
        self.xinfang.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.xinfang.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.xinfang.setText("")
        self.xinfang.setScaledContents(False)
        self.xinfang.setWordWrap(True)
        self.xinfang.setObjectName("xinfang")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 180, 331, 231))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.xinlv = QtWidgets.QLabel(self.groupBox_3)
        self.xinlv.setGeometry(QtCore.QRect(30, 50, 291, 171))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xinlv.setFont(font)
        self.xinlv.setAutoFillBackground(False)
        self.xinlv.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.xinlv.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.xinlv.setText("")
        self.xinlv.setScaledContents(False)
        self.xinlv.setWordWrap(True)
        self.xinlv.setObjectName("xinlv")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.path = QtWidgets.QLabel(Form)
        self.path.setGeometry(QtCore.QRect(60, 100, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.path.setFont(font)
        self.path.setAutoFillBackground(False)
        self.path.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.path.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.path.setScaledContents(False)
        self.path.setAlignment(QtCore.Qt.AlignCenter)
        self.path.setWordWrap(True)
        self.path.setObjectName("path")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 430, 731, 51))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "非接触式心率监测及心房震颤检测"))
        self.groupBox_2.setTitle(_translate("Form", "呼吸频率（RF）"))
        self.groupBox_3.setTitle(_translate("Form", "心率（HR）"))
        self.pushButton.setText(_translate("Form", "请选择一个文件"))
        self.path.setText(_translate("Form", "（请点击按钮选择一个视频文件）"))
