# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'actis.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Actis(object):
    def setupUi(self, Actis):
        Actis.setObjectName("Actis")
        Actis.resize(380, 319)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Actis.sizePolicy().hasHeightForWidth())
        Actis.setSizePolicy(sizePolicy)
        Actis.setStyleSheet("")
        self.fichero_Actis = QtWidgets.QLineEdit(Actis)
        self.fichero_Actis.setGeometry(QtCore.QRect(20, 50, 137, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fichero_Actis.sizePolicy().hasHeightForWidth())
        self.fichero_Actis.setSizePolicy(sizePolicy)
        self.fichero_Actis.setStyleSheet("border:(5px)")
        self.fichero_Actis.setText("")
        self.fichero_Actis.setFrame(True)
        self.fichero_Actis.setClearButtonEnabled(False)
        self.fichero_Actis.setObjectName("fichero_Actis")
        self.botonBrowse = QtWidgets.QPushButton(Actis)
        self.botonBrowse.setGeometry(QtCore.QRect(170, 50, 21, 21))
        self.botonBrowse.setObjectName("botonBrowse")
        self.boton_Si = QtWidgets.QRadioButton(Actis)
        self.boton_Si.setGeometry(QtCore.QRect(40, 140, 95, 20))
        self.boton_Si.setChecked(True)
        self.boton_Si.setObjectName("boton_Si")
        self.boton_No = QtWidgets.QRadioButton(Actis)
        self.boton_No.setGeometry(QtCore.QRect(40, 180, 95, 20))
        self.boton_No.setObjectName("boton_No")
        self.frame = QtWidgets.QFrame(Actis)
        self.frame.setGeometry(QtCore.QRect(30, 109, 161, 101))
        self.frame.setStyleSheet("background-color:rgb(254, 255, 192)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 141, 16))
        self.label.setObjectName("label")
        self.boton_OK = QtWidgets.QPushButton(Actis)
        self.boton_OK.setGeometry(QtCore.QRect(90, 250, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.boton_OK.setFont(font)
        self.boton_OK.setStyleSheet("background-color:rgb(203, 203, 203)")
        self.boton_OK.setObjectName("boton_OK")
        self.boton_Cancel = QtWidgets.QPushButton(Actis)
        self.boton_Cancel.setGeometry(QtCore.QRect(200, 250, 93, 28))
        self.boton_Cancel.setStyleSheet("background-color:rgb(203, 203, 203)")
        self.boton_Cancel.setObjectName("boton_Cancel")
        self.label_2 = QtWidgets.QLabel(Actis)
        self.label_2.setGeometry(QtCore.QRect(224, 65, 131, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/actis.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame.raise_()
        self.fichero_Actis.raise_()
        self.botonBrowse.raise_()
        self.boton_Si.raise_()
        self.boton_No.raise_()
        self.boton_OK.raise_()
        self.boton_Cancel.raise_()
        self.label_2.raise_()

        self.retranslateUi(Actis)
        QtCore.QMetaObject.connectSlotsByName(Actis)

    def retranslateUi(self, Actis):
        _translate = QtCore.QCoreApplication.translate
        Actis.setWindowTitle(_translate("Actis", "Conversor Actis - Direct"))
        self.fichero_Actis.setPlaceholderText(_translate("Actis", "Fichero ACTIS"))
        self.botonBrowse.setText(_translate("Actis", "..."))
        self.boton_Si.setText(_translate("Actis", "Sí"))
        self.boton_No.setText(_translate("Actis", "No"))
        self.label.setText(_translate("Actis", "<html><head/><body><p><span style=\" font-weight:600;\">¿Cambiar a SPS-GEN?</span></p></body></html>"))
        self.boton_OK.setText(_translate("Actis", "OK"))
        self.boton_Cancel.setText(_translate("Actis", "Cancelar"))

import icons_rc
