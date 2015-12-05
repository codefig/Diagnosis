# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_firstPage(object):
    def setupUi(self, firstPage):
        firstPage.setObjectName(_fromUtf8("firstPage"))
        firstPage.resize(411, 325)
        self.widget = QtGui.QWidget(firstPage)
        self.widget.setGeometry(QtCore.QRect(0, 10, 411, 311))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.firstDisplay = QtGui.QPlainTextEdit(self.widget)
        self.firstDisplay.setGeometry(QtCore.QRect(20, 30, 361, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Gothic"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.firstDisplay.setFont(font)
        self.firstDisplay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.firstDisplay.setAutoFillBackground(False)
        self.firstDisplay.setReadOnly(True)
        self.firstDisplay.setObjectName(_fromUtf8("firstDisplay"))
        self.startBtn = QtGui.QPushButton(self.widget)
        self.startBtn.setGeometry(QtCore.QRect(140, 260, 101, 31))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))

        self.retranslateUi(firstPage)
        QtCore.QMetaObject.connectSlotsByName(firstPage)

    def retranslateUi(self, firstPage):
        firstPage.setWindowTitle(_translate("firstPage", "Medical", None))
        self.firstDisplay.setPlainText(_translate("firstPage", "WELCOME TO OUR MEDICAL DIAGNOSIS APPLICATION. THIS APPLICATION IS TARGETED TOWARDS MALARIA AND TYPHOID. ITS GONNA HELP YOU DIAGNOSE MALARIA AND TYPHOID BY ASKING YOU SOME SERIES OF QUESTIONS.\n"
"CLICK THE START BUTTON TO START ", None))
        self.startBtn.setText(_translate("firstPage", "START DIAGNOSIS", None))

